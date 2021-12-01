# import math
# import numpy

# def lines():
#     with open("inputs/1.txt") as fp:
#         return fp.readlines()

# def process_lines():
#     post = []
#     for a in lines():
#         post.append(int(a.strip()))
#     return post

# lines = process_lines()

# count = 0
# for a in range(len(lines)):
#     try:
#         if lines[a+1] > lines[a]:
#             count += 1
#     except:
#         pass


# print(count)

import math
import numpy

def lines():
    with open("inputs/1.txt") as fp:
        return fp.readlines()

def process_lines():
    post = []
    for a in lines():
        post.append(int(a.strip()))
    return post

lines = process_lines()

count = 0
for a in range(len(lines)):
    try:
        x = lines[a+2] + lines[a+1] + lines[a]
        y = lines[a+3] + lines[a+2] + lines[a+1]
        if y > x:
            count += 1
    except:
        pass


print(count)