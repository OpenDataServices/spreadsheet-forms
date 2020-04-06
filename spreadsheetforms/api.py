from shutil import copyfile

import openpyxl


def _is_content_a_guide_field(content):
    return content and content.startswith("SPREADSHEETFORM:")


def _get_guide_field_spec_from_content(content):
    if content and content.startswith("SPREADSHEETFORM:SINGLE:"):
        return {"mode": "single", "path": content[23:]}

    if content and content.startswith("SPREADSHEETFORM:DOWN:"):
        bits = content.split(":")
        return {
            "mode": "down",
            "list_path": bits[2],
            "item_path": bits[3],
        }

    return None


def make_empty_form(guide_filename, out_filename):
    copyfile(guide_filename, out_filename)
    workbook = openpyxl.load_workbook(out_filename)

    for worksheet in workbook.worksheets:
        for row_idx in range(1, worksheet.max_row + 1):
            for cell in worksheet[row_idx]:
                if _is_content_a_guide_field(cell.value):
                    worksheet[cell.coordinate] = ""

    workbook.save(out_filename)


def _build_all_configs_in_excel_sheet(worksheet):
    single_configs = {}
    down_configs = {}

    for row_idx in range(1, worksheet.max_row + 1):
        for cell in worksheet[row_idx]:
            guide_field_spec = _get_guide_field_spec_from_content(cell.value)
            if guide_field_spec:
                guide_field_spec["coordinate"] = cell.coordinate
                guide_field_spec["column_letter"] = cell.column_letter
                guide_field_spec["row"] = cell.row
                if guide_field_spec["mode"] == "single":
                    single_configs[guide_field_spec["path"]] = guide_field_spec
                elif guide_field_spec["mode"] == "down":
                    if guide_field_spec["list_path"] in down_configs:
                        down_configs[guide_field_spec["list_path"]].append(
                            guide_field_spec
                        )
                    else:
                        down_configs[guide_field_spec["list_path"]] = [guide_field_spec]

    # TODO could check that every down config for each list_path is on the same row. Things will get odd if they are not.

    return single_configs, down_configs


def get_data_from_form(guide_filename, in_filename):
    data = {}
    guide_workbook = openpyxl.load_workbook(guide_filename, read_only=True)
    in_workbook = openpyxl.load_workbook(in_filename, read_only=True)

    for worksheet in guide_workbook.worksheets:

        # Step 1: build details of all configs on this sheet
        single_configs, down_configs = _build_all_configs_in_excel_sheet(worksheet)

        # Step 2: Process single configs (easy ones)
        for single_config in single_configs.values():
            # TODO this only does top level paths - we should add so it can do paths with several levels
            data[single_config["path"]] = in_workbook[worksheet.title][
                single_config["coordinate"]
            ].value

        # Step 3: Process Down Configs
        for down_config in down_configs.values():
            start_row = down_config[0]["row"]
            max_row = in_workbook[worksheet.title].max_row + 1
            # TODO this only does top level paths - we should add so it can do paths with several levels
            data[down_config[0]["list_path"]] = []
            for row in range(start_row, max_row + 1):
                item = {}
                found_anything = False
                for this_down_config in down_config:
                    # TODO this only does top level paths - we should add so it can do paths with several levels
                    cell = in_workbook[worksheet.title][
                        this_down_config["column_letter"] + str(row)
                    ]
                    item[this_down_config["item_path"]] = cell.value
                    if item[this_down_config["item_path"]]:
                        found_anything = True
                if found_anything:
                    # TODO this only does top level paths - we should add so it can do paths with several levels
                    data[down_config[0]["list_path"]].append(item)

    return data


def put_data_in_form(guide_filename, data, out_filename):
    copyfile(guide_filename, out_filename)
    workbook = openpyxl.load_workbook(out_filename)

    for worksheet in workbook.worksheets:

        # Step 1: build details of all configs on this sheet
        single_configs, down_configs = _build_all_configs_in_excel_sheet(worksheet)

        # Step 2: Process single configs (easy ones)
        for single_config in single_configs.values():
            # TODO this only does top level paths - we should add so it can do paths with several levels
            worksheet[single_config["coordinate"]] = data.get(single_config["path"])

        # Step 3: Process Down Configs
        for down_config in down_configs.values():
            datas_to_insert = data.get(down_config[0]["list_path"], [])
            if isinstance(datas_to_insert, list):
                if len(datas_to_insert) == 0:
                    # we still want to remove the special values from the output spreadsheet
                    for this_down_config in down_config:
                        # TODO this only does top level paths - we should add so it can do paths with several levels
                        worksheet[this_down_config["coordinate"]] = ""
                else:
                    extra_row = 0
                    for data_to_insert in datas_to_insert:
                        for this_down_config in down_config:
                            # TODO this only does top level paths - we should add so it can do paths with several levels
                            worksheet[
                                this_down_config["column_letter"]
                                + str(this_down_config["row"] + extra_row)
                            ] = data_to_insert.get(this_down_config["item_path"])
                        extra_row += 1

    workbook.save(out_filename)
