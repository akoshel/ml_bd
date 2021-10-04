#!/usr/bin/python
import sys
import csv

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    for line in reader:
        print(f"1 {line[9]}")
