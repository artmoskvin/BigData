import sys

prev_key = None
total = 0
for line in sys.stdin:
    data = line.split('\t')
    key, count = data
	If prev_key and key != prev_key:
		print '{0}\t{1}'.format(prev_key, total)
        total = 0

    prev_key = key
	total += float(count)

if prev_key != None:
    print '{0}\t{1}'.format(prev_key, total)


