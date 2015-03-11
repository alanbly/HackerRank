# https://www.hackerrank.com/contests/w14/challenges/number-list

from itertools import *
from math import *
import random

def subArrays(N, memo = {}) :
  if N <= 0 :
    return []
  if N in memo :
    return memo[N]
  memo[N] = []
  for i in range(N) :
    for j in range(i, N) :
      memo[N].append((i, j+1))
  return memo[N]

def maxBeatsK(sequence, K) :
  for i in sequence :
    if i > K :
      return True
  return False

def countBrute(sequence, K, memo = {}) :
  return sum(1 for i in ifilter(lambda x: maxBeatsK(x, K), imap(lambda x: islice(sequence, x[0], x[1]), subArrays(len(sequence), memo))))

# countBrute(range(1, 4), 2) # 3
# countBrute(range(1, 4), 1) # 5
# countBrute([1, 3, 3, 5, 6], 2) # 14
# countBrute([random.randint(1,1000) for i in range(10**6)], 500) # ~4486536


# return a tuple containing: the number of subArrays that finish at the end of this sequence which include a value larger than k
#                            the number of subArrays that finish at the end of this sequence which do not include a value larger than k
#                            the number of subArrays that finish before the end of this sequence which include a value larger than k
def subArrays(sequence, K) :
  next = [0, 0, 0]
  for i in sequence :
    next[2] += next[0]; 
    if i > K :
      next[0] += next[1]+1
      next[1] = 0
    else :
      next[1] += 1
    #print next
  return next

# subArrays(range(1, 4), 2) # 3
# subArrays(range(1, 4), 1) # 5
# subArrays([1, 3, 3, 5, 6], 2) # 14
# subArrays([random.randint(1,1000) for i in range(10**6)], 500) # ~4486536



T = long(raw_input())
for i in range(T) :
  (N, K) = map(long, raw_input().split(" "))
  sequence = map(long, raw_input().split(" "))
  counts = subArrays(sequence, K)
  print counts[0]+counts[2]