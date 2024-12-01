import sys

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

distance = sum([abs(l - r) for [l, r] in zip(sorted(left), sorted(right))])

print(distance)
