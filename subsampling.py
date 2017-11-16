import random
# to handle gzipped FASTQ sequence files
import gzip
# to handle and check input files
import sys
import os

while True:
    read1_file = input("Enter the path to read1 file: ")
    if os.path.exists(read1_file):
        break
    else:
        print("Couldn't find: "+read1_file)
        continue

while True:
    barcode_file = input("Enter the path to barcode file: ")
    if os.path.exists(barcode_file):
        break
    else:
        print("Couldn't find: "+barcode_file)
        continue

while True:
    try:
        number_to_sample = int(input("Enter number of sequences to be sampled (integer)"))
    except ValueError:
        print('Not an integer')
        continue
    if number_to_sample <= 0:
        print("Shouldn't be negative or zero")
        continue
    else:
        break

with gzip.open(read1_file) as input:
    num_lines = sum([1 for line in input])
total_records = int(num_lines / 4)

print("sampling " + str(number_to_sample) + " out of " + str(total_records) + " records")
percent = (number_to_sample / total_records) * 100
print("sampling " + str(percent) + " % of records")
records_to_keep = set(random.sample(range(total_records + 1), number_to_sample))

record_number = 0
with gzip.open(read1_file, "rt") as input:
    with open("read1.fastq", "w") as output:
        for line1 in input:
            line2 = next(input)
            line3 = next(input)
            line4 = next(input)
            if record_number in records_to_keep:
                output.write(line1)
                output.write(line2)
                output.write(line3)
                output.write(line4)
            record_number += 1

record_number = 0
with gzip.open(barcode_file, "rt") as input:
    with open("barcode.fastq", "w") as output:
        for line1 in input:
            line2 = next(input)
            line3 = next(input)
            line4 = next(input)
            if record_number in records_to_keep:
                output.write(line1)
                output.write(line2)
                output.write(line3)
                output.write(line4)
            record_number += 1
