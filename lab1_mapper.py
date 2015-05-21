import sys

for line in sys.stdin:
    for data in line.strip().split(','):
        print '{0}\t{1}'.format(data[2], data[4])
