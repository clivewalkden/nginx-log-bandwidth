# Python Nginx Scan Log

[![GitHub issues](https://img.shields.io/github/issues/clivewalkden/nginx-log-bandwidth?style=flat-square)](https://github.com/clivewalkden/nginx-log-bandwidth/issues)
[![Known Vulnerabilities](https://snyk.io/test/github/clivewalkden/nginx-log-bandwidth/badge.svg?style=flat-square)](https://snyk.io/test/github/clivewalkden/nginx-log-bandwidth)
[![GitHub license](https://img.shields.io/github/license/clivewalkden/nginx-log-bandwidth?style=flat-square)](https://github.com/clivewalkden/nginx-log-bandwidth/blob/master/LICENSE)

This script scans a Nginx log and calculates the Bandwidth used. The output shows the number of lines scanned, lines not included and the total bandwidth consumed in a human readable format.

## Usage
Simply run the script and pass in a file to scan through
```python
python ./nginx_scanlog/main.py test-access.log
```

You will be returned a result including the number of lines in the file, rows matching the expected regex, number of rows skipped (as they didn't match the regex) and the bandwidth usage for the log file. The output will be similar to that shown below.

```python
## Loading File
## Reading file
## Calculating Bandwidth
Scanning rows: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 4505.16it/s]

## Log file recorded:
 - Total lines: 3
 - 3 rows included, 0 rows skipped.
-----------------------------------
 - 136.40KiB of bandwidth usage.
-----------------------------------

```

## Changelog
See the [Changelog](./CHANGELOG.md) for more information.

## Security
Click for more information on our [Security Policy](./SECURITY.md)