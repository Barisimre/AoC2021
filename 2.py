
import math
import numpy

def lines():
    with open("inputs/2.txt") as fp:
        return fp.readlines()

def process_lines():
    post = []
    for a in lines():
        post.append(a.split())
    return post

lines = process_lines()

h = 0
v = 0
aim = 0

for d, a in lines:
    if d == "forward":
        h += int(a)
        v += aim*int(a)
    elif d == "down":
        aim += int(a)
    else:
        aim -= int(a)

print(h*v)

