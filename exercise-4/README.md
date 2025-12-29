# Exercise 4 – Log Analysis Automation Script

## Overview
This script automates the analysis of application log files by scanning for common log levels such as INFO, WARNING, and ERROR. The goal is to provide a quick summary that helps engineers identify issues without manually inspecting large log files.

## How the Script Works
The script reads a log file provided as a command-line argument and counts the occurrences of different log levels. Logging is used to track script execution and report errors such as missing files.

## Error Handling and Logging
Basic error handling is implemented to handle missing or invalid input files. Python’s logging module is used instead of print statements to provide structured and timestamped logs, which is a common practice in production tooling.

## Configuration
The script is configurable via command-line arguments, allowing it to be easily integrated into automation workflows or CI/CD pipelines.

## Testing
A basic unit test is included to validate log parsing logic. This ensures that changes to the script do not break expected behavior.

## Use Case
This type of script is useful during incident investigation or routine log reviews, where quick insights into error patterns can significantly reduce troubleshooting time.
