#!/usr/bin/python3

import sys

for line in sys.stdin:
    columns = line.strip().split(',')
    # Check which table is being read
    if len(columns) == 10:  # 'Books Ratings' table
        title = columns[0]  # Extract the book title
        other_data = ','.join(columns[1:])  # Join all other data columns
        print(f"{title}\t{other_data}\tD\n")

    else:  # 'Books Rating' table
        title = columns[0]  # Extract the book title
        # Join all other data columns
        other_data = ','.join(columns[1:])
        print(f"{title}\t{other_data}\tR\n")