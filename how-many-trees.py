import math
from itertools import *

# T(N, L) = Labelled trees with N nodes and L leaves

# total trees = N^(N-2)

# T(N, 2) = N!/2
# T(N, N-1) = N
# T(N, L) = T(N-1, L) with a new node in place of each edge (N-2)
#                                     just outside each leaf (L)
#                                     splitting each branch into each possible partition (This means generating at least some of the trees)
#                                       (branches less than 3 nodes have no valid partitions)

# T(N, L) = T(N, L+1) 

# T(4, 2) = 24/2 = 12
# T(5, 2) = 120/2 = 60

# T(3, {2}) = {3}
# T(4, {2, 3}) = {12, 4}
# T(5, {2, 3, 4}) = {60, 60, 5}
# T(6, {2, 3, 4, 5}) = {360, 720, 210, 6}
modVal = pow(10, 9)+7


def trees(N) :
  return product(range(1,N+1), repeat=N-2)

def countLeaves(tree) :
  return len(tree)+2-len(set(tree))

def treeBrute(N, L) :
  if N - L == 1 :
    return long(N%modVal)
  if L == 2 :
    return long(factorial(N)/2%modVal)
  prufers = trees(N)
  return long(sum([1 if countLeaves(i) == L else 0 for i in prufers]) % modVal);

# treeBrute(4, 2);
# treeBrute(4, 3);
# treeBrute(5, 2);
# treeBrute(5, 3);
# treeBrute(5, 4);


def choose(n, k):
  """
  A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
  """
  if 0 <= k <= n:
    ntok = 1
    ktok = 1
    for t in xrange(1, min(k, n - k) + 1):
      ntok *= n
      ktok *= t
      n -= 1
    return ntok // ktok
  else:
    return 0

def partition(count, memo = {}) :
  if count in memo :
    return memo[count]
  splits = {}
  for i in range((count+1)/2, count) :
    splits[i+1] = choose(count, i)
  memo[count] = splits;             # {5: {3: 10, 4: 5}}
  return splits

def treeRecurse(N, L, branches = {}, partitions = {}) :
  if N not in branches :
    branches[N] = {}
  if N - L == 1 :
    branches[N][L] = N*[{(N-1): 1}]   # [{4: 1}, {4: 1}, {4: 1}, {4: 1}, {4: 1}]
    #print "%d,%d:" % (N, L)
    #print branches[N][L]
    return long(N%modVal)
  if L == 2 : 
    branches[N][L] = []
    return long(factorial(N)/2%modVal)
  oneLess = treeRecurse(N-1, L, branches, partitions)
  newNode = treeRecurse(N-1, L-1, branches, partitions)
  branches[N][L] = []
  #print branches[N-1][L]
  for tree in branches[N-1][L] :
    for branchCount, number in tree.items() :
      newPartitions = partition(branchCount, partitions)
      # print "%d*%d:" % (branchCount, number)
      # print newPartitions
      branches[N][L].extend(number*[newPartitions])
  newBranches = sum([sum(i.values())%modVal for i in branches[N][L]])
  # print "%d,%d:" % (N, L)
  # print branches[N][L]
  # print "  %d*%d + %d + %d*%d" % (oneLess, (N-2 + L), newBranches, newNode, (N-L))
  return long((oneLess * (N-2 + L) + newBranches + newNode*(N-L))%modVal)

# treeRecurse(4, 2);     #12
# treeRecurse(4, 3);     #4
# treeRecurse(5, 2);     #60
# treeRecurse(5, 3);     #60
# treeRecurse(5, 4);     #5
# treeRecurse(8, 4);     #109200
# treeRecurse(1000, 16); #421013870

def modSum(values) :
  return sum(i%modVal for i in values)%modVal

def completePermutation(length, items, memo = {}) :
  if length not in memo :
    memo[length] = {}
  if items == 1 :
    return 1
  if items > length :
    return 0
  total = pow(items, length, modVal)
  for i in range(items) :
    choose(items, i)
    completePermutation(length, i, memo)
  memo[length][items] = (total-modSum(choose(items, i)*completePermutation(length, i, memo) for i in range(items)))%modVal
  return memo[length][items]

def treesWithLeaves(N, L) :
  return choose(N, L)*completePermutation(N-2, N-L)

def treeSmart(N, L) :
  if N - L == 1 :
    return long(N%modVal)
  if L == 2 :
    return long(factorial(N)/2%modVal)
  return long(treesWithLeaves(N, L) % modVal);

treeSmart(4, 2);     #12
treeSmart(4, 3);     #4
treeSmart(5, 2);     #60
treeSmart(5, 3);     #60
treeSmart(5, 4);     #5
treeSmart(8, 4);     #109200
treeSmart(1000, 16); #421013870


(N,L) = [long(i) for i in raw_input().split(" ")]

print treeBrute(N, L)
