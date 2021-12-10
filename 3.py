
import math
import numpy

def lines():
    with open("inputs/3.txt") as fp:
        return fp.readlines()

def process_lines():
    post = []
    for a in lines():
        post.append([int(x) for x in a.strip()])
    return post

lines = process_lines()

gamma = ""
epsilon = ""

for i in range(len(lines[0])):
    gamma += str((int(sum([x[i] for x in lines]) > len(lines) / 2)))
    epsilon += str((int(sum([x[i] for x in lines]) < len(lines) / 2)))

print(int(gamma, 2)*int(epsilon, 2))
