# https://www.hackerrank.com/contests/w14/challenges/palindromic-border

modVal = 10**9+7

def isPalindrome(string, start, end) :
  half = (end-start+1)/2
  # print "%d %d %d"%(start, half, end)
  for i in range(half) :
    if string[start + i] != string[end-i-1] :
      return False
  return True

# isPalindrome("acba", 0, 4)


def countPalindromesBad(string) :
  return sum(1 for i in range(1,len(string)+1) if isPalindrome(string[:i])) % modVal

# countPalindromesBad("a") # 1
# countPalindromesBad("abab") # 3
# countPalindromesBad("lololo") # 3


def countPalindromes(string, start, end) :
  longest = end
  while not isPalindrome(string, start, longest) :
    longest -= 1
  return sum(1 for i in range(start,end) if string[i] == string[start] and isPalindrome(string, start, i+1)) # 24s

# countPalindromes("a", 0, 1) # 1
# countPalindromes("abab", 0, 4) # 2
# countPalindromes("lololo", 0, 6) # 3
# countPalindromes("lololol", 0, 6) # 3


def getBorders(string, start, end) :
  biggest = start
  offset = end+start-1
  while biggest < end and string[biggest] == string[offset-biggest] :
    biggest += 1;
  return 0 if biggest == 0 else countPalindromes(string, start, min(end,biggest+1)-1) % modVal # 12s

# getBorders("abca", 0, 4) # 1
# getBorders("ababa", 0, 5) # 2
# getBorders("lololol", 0, 7) # 3
# getBorders("ababa", 1, 4) # 1
# getBorders("abcacb", 1, 6) # 1
# getBorders("abcacb", 0, 4) # 1


def substringsBad(string) :
  for i in range(len(string)) :
    for j in range(len(string), i+1, -1) :
      if string[i] == string[j-1] : 
        yield string[i:j] # 11 sec if we limit to 8 chars

# tuple(substrings("abcacb"))


def substrings(string) :
  if len(string) == 1 :
    yield string
    return
  for i in range(len(string)) : # reduce 10x gets a 5x speedup
    for j in range(len(string), i+1, -1) : # reduce 10x gets a 80x speedup
      if string[i] == string[j-1] : 
        yield (i,j) # 11 sec if we limit to 8 chars

# tuple(substrings("abcacb"))


def palindromicBordersBad(string) :
  return sum(map(getBorders, substrings(string))) % modVal

# start = time()
# palindromicBordersBad("abcacb") # 3
# palindromicBordersBad("ababa") # 5
# palindromicBordersBad("".join(["abcdefgh"[randint(0,7)] for i in range(10**3)])) # ~0.4 sec
# palindromicBordersBad("".join(["abcdefgh"[randint(0,7)] for i in range(10**4)])) # ~40 sec
# time() - start


def palindromicBorders(string) :
  return sum(getBorders(string, i[0], i[1]) for i in substrings(string)) % modVal

# start = time()
# palindromicBorders("abcacb") # 3
# palindromicBorders("ababa") # 5
# palindromicBorders("".join(["abcdefgh"[randint(0,7)] for i in range(10**3)])) # ~0.4 sec
# palindromicBorders("".join(["abcdefgh"[randint(0,7)] for i in range(10**4)])) # ~40 sec
# palindromicBorders("".join(["abcdefgh"[randint(0,7)] for i in range(10**5)])) # ~2156 sec
# time() - start


string = raw_input()

print palindromicBorders(string)

