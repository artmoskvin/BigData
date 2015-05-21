import sys

for line in sys.stdin:
    for token in line.strip().split():
        clean_token = ''.join(char for char in token if char.isalnum()).lower()
        print(clean_token + "\t1")
