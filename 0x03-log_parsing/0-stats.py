#!/usr/bin/python3

"""Import some modules"""

import sys
import signal


"""Store total file size and status code counts"""
file_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_statistics(signal=None, frame=None):
    """Print the current statistics."""
    global file_size, status_codes
    print("File size:", file_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
    if signal:
        sys.exit(0)


"""Setup a signal handler to catch CTRL+C"""
signal.signal(signal.SIGINT, print_statistics)

"""Process the input lines"""
counter = 0
for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 9:
            continue
        size = int(parts[-1])
        status_code = parts[-2]
        file_size += size
        if status_code in status_codes:
            status_codes[status_code] += 1
        counter += 1
        if counter % 10 == 0:
            print_statistics()
    except ValueError:
        pass

"""Final print if the input didn't end in a multiple of 10"""
if counter % 10 != 0:
    print_statistics()
