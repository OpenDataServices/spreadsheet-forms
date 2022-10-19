# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]


### Added

- What happens when getting data from a form and a worksheet is missing? New parameter `missing_worksheet_action` to `get_data_from_form` and `get_data_from_form_with_guide_spec`. New Enum `GetDataFromFormMissingWorksheetAction`. Default and old behavior is `RAISE_EXCEPTION`. New option available is `SET_NO_DATA`. New exception class `MissingWorksheetException`.

### Fixed

- Broken link in get_data_from_form_with_guide_spec function docs page 

## [0.4.1] - 2020-08-12

### Fixed

- Fixed a crash on a integer cell

## [0.4.0] - 2020-08-04

### Added

- new functions get_guide_spec and get_data_from_form_with_guide_spec
- added right option as well as down

## [0.3.0] - 2020-05-27

### Added

- added date_format to get_data_from_form

## [0.2.1] - 2020-05-22

### Fixed

- put_data_in_form: on a DOWN set of fields, where the list did not exist in the data at all, the field configs were not cleared

## [0.2.0] - 2020-05-15

### Changed

- Can handle deep JSON paths

## [0.1.0] - 2020-04-06

### Changed

- First Version

