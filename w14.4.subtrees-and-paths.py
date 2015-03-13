# https://www.hackerrank.com/contests/w14/challenges/subtrees-and-paths
from random import randint

def buildTree(nodes, adjacencies) :
  adjacencyMap = [[] for i in range(nodes+1)]
  for (a, b) in adjacencies :
    adjacencyMap[a].append(b)
    adjacencyMap[b].append(a)
  distance = [None for i in range(nodes+1)]
  distance[1] = 0
  toVisit = set([1])
  visited = set()
  while len(toVisit) > 0 :
    next = toVisit.pop()
    newNodes = set(adjacencyMap[next]) - visited
    for i in newNodes :
      distance[i] = 1+distance[next]
    visited.add(next)
    toVisit |= newNodes
  tree = [[] for i in range(nodes+1)]
  for (a, b) in adjacencies :
    if distance[a] < distance[b] :
      tree[a].append(b)
    else:
      tree[b].append(a)
  return tree

# simple = buildTree(5, [(1, 2),(2, 3),(2, 4),(5, 1)]) # {1: [2, 5], 2: [3, 4], 3: [], 4: [], 5: []}
# big = buildTree(99999, [(i, i+1) for i in range(1, 99999, 2)]+[(i, i+2) for i in range(2, 99997, 2)])

# completeAdj = []
# for i in range(1, 50000) :
#   completeAdj.append((i, i*2))
#   completeAdj.append((i*2+1, i))

# complete = buildTree(99999, completeAdj)


def buildPaths(tree) :
  paths = [None for i in range(len(tree)+1)]
  for node in range(len(tree)) :
    for i in tree[node] :
      paths[i] = node
  return paths

# bigPaths = buildPaths(big)
# completePaths = buildPaths(complete)


def addVal(tree, values, node, val) :
  if val == 0 :
    return
  i = 0
  nodes = [node]
  while i < len(nodes) :
    values[nodes[i]] += val
    nodes.extend(tree[nodes[i]])
    i += 1

# bigVals = dict((i, 0) for i in range(1,100000))
# addVal(big, bigVals, 99990, 10000)
# addVal(big, bigVals, 99992, 1000)
# addVal(big, bigVals, 99995, 100)
# addVal(big, bigVals, 99997, 10)

# completeVals = dict((i, 0) for i in range(1,100000))

# for i in range(10**5) :
#   addVal(complete, completeVals, randint(1,99999), 1)



def getPath(paths, node, memo = {}) :
  if memo[node] != None :
    return memo[node]
  if node == 1 :
    return [1]
  path = []
  next = node
  while paths[next]!= None :
    path.append(next)
    next = paths[next]
  memo[node] = path[::-1]
  return memo[node]

# getPath(bigPaths, 30) # [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
# getPath(bigPaths, 99998)

# getPath(completePaths, 20000)
# getPath(completePaths, 40000)
# getPath(completePaths, 60000)
# getPath(completePaths, 80000)

def maxPath(paths, values, a, b, memoParent, memoPath) :
  (pathA, pathB) = (getPath(paths, a, memoPath), getPath(paths, b, memoPath))
  lastCommon = 1
  shortest = min(len(pathA), len(pathB))
  while lastCommon < shortest and pathA[lastCommon] == pathB[lastCommon] :
    lastCommon += 1
  lastCommon -= 1
  return max(max(values[i] for i in pathA[lastCommon:]), max(values[i] for i in pathB[lastCommon:]))

nodes = long(raw_input())

memoParent = [{} for i in range(nodes+1)]
memoPath = [None for i in range(nodes+1)]
# maxPath(completePaths, completeVals, 99999, 40000, memoParent, memoPath) #


adjacencies = [map(long, raw_input().split(" ")) for i in range(nodes-1)]
tree = buildTree(nodes, adjacencies)

paths = buildPaths(tree)

values = dict((i, 0) for i in range(1,nodes+1))
tests = long(raw_input())
for i in range(tests) :
  inputs = raw_input().split(" ")
  command = inputs[0]
  (a, b) = map(long, inputs[1:])
  if command == "add" :
    addVal(tree, values, a, b)
  else :
    print maxPath(paths, values, a, b, memoParent, memoPath) 

