import sys
import logging
from collections import Counter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def analyze_log(file_path):
    try:
        with open(file_path, "r") as file:
            logs = file.readlines()
    except FileNotFoundError:
        logging.error("Log file not found")
        sys.exit(1)

    levels = Counter()

    for line in logs:
        if "ERROR" in line:
            levels["ERROR"] += 1
        elif "WARNING" in line:
            levels["WARNING"] += 1
        elif "INFO" in line:
            levels["INFO"] += 1

    logging.info("Log analysis completed")
    return levels

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.error("Usage: python log_analyzer.py <log_file>")
        sys.exit(1)

    result = analyze_log(sys.argv[1])
    for level, count in result.items():
        print(f"{level}: {count}")
