from math import *
from itertools import *

# T(N, L) = Labelled trees with N nodes and L leaves

# total trees = N^(N-2)

# T(N, 1) = (N-1)!
# T(N, N-1) = 1
# T(N, L) = T(N-1, L)*(N-1-1 + L + L-1)  > N+2L-3                                                            + T(N-1, L-1)*(N-1-(L-1))
#           T(N-1, L) with the new node above each but the root, below each leaf, or in place of each branch + number with one less leaf and one less node with the new node added to each non-leaf node

# T(4, 2) = 1        *()  >5<                                                                                + 2*(3-1) >4<
# T(5, 2) = 9        *()  >6<                                                                                + 6*(4-1) >18<  + 6?

# T(3, {1, 2}) = {2, 1}
# T(4, {1, 2, 3}) = {6, 9, 1}
# T(5, {1, 2, 3, 4}) = {24, 60, , 1}

def treesRecurse(N, L, memo = {}) :
  if N not in memo :
    memo[N] = {}
  if L in memo[N] :
    return memo[N][L]
  if N - L == 1 :
    memo[N][L] = 1
    return memo[N][L] 
  if L == 1 : 
    memo[N][L] = factorial(N-1)
    return memo[N][L]
  print "%d*%d + %d" % (treesRecurse(N-1, L, memo), (N+2*L-3), treesRecurse(N-1, L-1, memo)*(N-L))
  return treesRecurse(N-1, L, memo)*(N+2*L-3) + treesRecurse(N-1, L-1, memo)*(N-L)

treesRecurse(4, 1);
treesRecurse(4, 2);
treesRecurse(4, 3);
treesRecurse(5, 2);


def countLeaves(tree) :
  return len(tree)+1-len(set(tree))

def treeBrute(N, L, prufers = {}) :
  if N not in prufers :
    prufers[N] = [i for i in product(range(1,N+1), repeat=N-1)]
  return sum([1 if countLeaves(i) == L else 0 for i in prufers[N]]);

treeBrute(4, 1);
treeBrute(4, 2);
treeBrute(4, 3);
treeBrute(5, 2);

(N,L) = [int(i) for i in raw_input().split(" ")]

print treeBrute(N, L)