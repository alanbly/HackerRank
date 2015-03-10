# https://www.hackerrank.com/contests/w14/challenges/worst-permutation

def badPermute(N, K, sequence) :
  if K >= N :
    return range(N,0,-1)
  swaps =  dict((sequence[i], i) for i in range(N))
  next = N
  add = 0
  #print "Swapping:"
  for i in range(K) :
    while i+add < N and sequence[i+add] == next :
      add += 1;
      next -= 1
    if i+add >= N :
      return sequence
    #print "  %d for %d" % (next, sequence[i])
    sequence[swaps[next]] = sequence[i+add]
    swaps[sequence[i+add]] = swaps[next]
    sequence[i+add] = next
    #print sequence
    #print swaps
    next -= 1
  return sequence

badPermute(5, 1, [4, 2, 3, 5, 1]) # 5, 2, 3, 4, 1
badPermute(3, 1, [2, 1, 3]) # 3, 1, 2

badPermute(5, 2, [4, 2, 3, 5, 1]) # 5, 4, 3, 2, 1

badPermute(3, 5, [1, 2, 3]) # 3 2 1
badPermute(10, 2, [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) #10 9 8 3 4 5 6 7 2 1



(N, K) = [long(i) for i in raw_input().split(" ")]

sequence = [long(i) for i in raw_input().split(" ")]

print " ".join(str(i) for i in badPermute(N, K, sequence))
