from math import *
from itertools import *

# T(N, L) = Labelled trees with N nodes and L leaves

# total trees = N^(N-2)

# T(N, 2) = N!/2
# T(N, N-1) = N
# T(N, L) = T(N-1, L) with a new node in place of each   

# T(4, 2) = 24/2 = 12
# T(5, 2) = 120/2 = 60

# T(3, {2}) = {3}
# T(4, {2, 3}) = {12, 4}
# T(5, {2, 3, 4}) = {60, 60, 5}
# T(6, {2, 3, 4, 5}) = {360, , , 6}


def trees(N) :
  return product(range(1,N+1), repeat=N-2)

def countLeaves(tree) :
  return len(tree)+2-len(set(tree))

def treeBrute(N, L) :
  if L == 2 :
    return factorial(N)/2
  prufers = trees(N)
  return sum([1 if countLeaves(i) == L else 0 for i in prufers]);

# treeBrute(4, 2);
# treeBrute(4, 3);
# treeBrute(5, 2);
# treeBrute(5, 3);
# treeBrute(5, 4);

(N,L) = [int(i) for i in raw_input().split(" ")]

print treeBrute(N, L)