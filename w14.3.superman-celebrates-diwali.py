# https://www.hackerrank.com/contests/w14/challenges/superman-celebrates-diwali
from collections import Counter
from random import *

test1 = {1: {1: 3, 4: 1, 10: 1}, 2: {3: 1, 5: 1, 7: 2, 8: 2, 9: 2}, 3: {3: 1, 4: 1, 5: 1, 6: 1, 9: 1}}

def howMany(people, building, height) :
  if building not in people or height not in people[building] :
    return 0;
  return people[building][height]

def bestJump(people, count, building, height, drop, memo = {}) :
  if height < 1 :
    return 0
  if building not in memo :
    memo[building] = {}
  if height == 1 :
    memo[building][height] = howMany(people, building, height)
  else :
    jumps = [bestJump(people, count, i, height-drop, drop, memo) for i in range(1, building)]+ \
            [bestJump(people, count, building, height-1, drop, memo)]+ \
            [bestJump(people, count, i, height-drop, drop, memo) for i in range(building+1, count+1)]
    best = reduce(max, jumps)
    #print "  going to building %d with %d" %(best[0], best[1][2])
    memo[building][height] = best+howMany(people, building, height)
  return memo[building][height];

# bestJump(test1, 4, 2, 8, 2) # 10

def findBestPathRecurse(people, count, height, drop) :
  jumpMemo = {}
  bests = [bestJump(people, count, i, height, drop, jumpMemo) for i in range(1,count+1)]
  return reduce(max, bests)

# findBestPathRecurse(test1, 4, 1, 2) # 3
# findBestPathRecurse(test1, 4, 15, 2) # 12


def findBestPath(people, count, height, drop) :
  bests = dict((i, howMany(people, i, 1)) for i in range(1, count+1))
  jump = {1: max(bests.values())}
  jumpTo = 2-drop
  # print bests
  # print jump[1]
  for i in range(2, height+1) :
    for j in range(1, count+1) :
      next = howMany(people, j, i)
      # print "add %d Jump to %d or %d" % (next, jump[jumpTo], bests[j])
      bests[j] = next + (bests[j] if jumpTo < 1 or jump[jumpTo] < bests[j] else jump[jumpTo])
    jump[i] = max(bests.values())
    jumpTo += 1
    # print bests
    # print jump[i]
  return jump[height]

# findBestPath(test1, 4, 1, 2) # 3
# findBestPath(test1, 4, 15, 2) # 12
# findBestPath(dict((i, dict((j, randint(0,1900)) for j in range(1,1900,randint(1,7)))) for i in range(1, 1900)), 1900, 1900, 2)


def countPeople(locations) :
  return Counter(locations)

# 5 1 1 1 4 10
# 8 9 5 7 7 3 9 8 8
# 5 9 5 6 4 3
# 0


(buildings, height, drop) = map(long, raw_input().split(" "))
people = dict((i, countPeople(map(long, raw_input().strip().split(" "))[1:])) for i in range(1,buildings+1))

print findBestPath(people, buildings, height, drop)
