import sys
from itertools import groupby

input_file_name = sys.argv[1]
if input_file_name is None:
    print("Please provide a file path")
    sys.exit(1)

lines = [line.rstrip() for line in open(input_file_name).readlines()]

left = []
right = []

for line in lines:
    if line == '':
        continue
    l, r = [int(el) for el in line.split()]
    left.append(l)
    right.append(r)

right_index_counts = {x: len(list(g)) for [x, g] in groupby(sorted(right), lambda x: x)}

similarity = sum([l * right_index_counts.get(l, 0) for l in left])

print(similarity)
