import sys

prev_key = None
sum = 0
for line in sys.stdin:
    data = line.split('\t')
    key, count = data
	If prev_key and key != prev_key:
		print '{0}\t{1}'.format(prev_key, sum)
        sum = 0

    prev_key = key
	sum += int(count)

if prev_key != None:
    print '{0}\t{1}'.format(prev_key, sum)


