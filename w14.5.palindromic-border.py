# https://www.hackerrank.com/contests/w14/challenges/palindromic-border

modVal = 10**9+7

def isPalindrome(num) :
  string = str(num)
  bottomHalf = len(string)/2
  topHalf = (len(string)-1)/2
  return string[:bottomHalf] == string[:topHalf:-1]


def countPalindromesBad(string) :
  return sum(1 for i in range(1,len(string)+1) if isPalindrome(string[:i])) % modVal

# countPalindromesBad("a") # 1
# countPalindromesBad("abab") # 3
# countPalindromesBad("lololo") # 3


def countPalindromes(string) :
  longest = len(string)
  while not isPalindrome(string[:longest]) :
    longest -= 1
  return sum(1 for i in range(0,len(string)) if string[i] == string[0] and isPalindrome(string[:i+1])) # 24s

# countPalindromes("a") # 1
# countPalindromes("abab") # 2
# countPalindromes("lololo") # 3


def getBorders(string) :
  biggest = 0
  limit = len(string)
  # print limit
  while biggest < limit and string[biggest] == string[-1-biggest] :
    # print "%s = %s" % (string[biggest], string[-1-biggest])
    biggest += 1;
  # print biggest
  # print string[:biggest]
  return 0 if biggest == 0 else countPalindromes(string[:min(limit,biggest+1)-1]) % modVal # 12s

# getBorders("abca") # 1
# getBorders("ababa") # 2
# getBorders("lololol") # 3


def substrings(string) :
  for i in range(len(string)) :
    for j in range(len(string), i+1, -1) :
      if string[i] == string[j-1] : 
        yield string[i:j] # 11 sec if we limit to 8 chars

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
  return sum(map(getBorders, substrings(string))) % modVal

start = time()
# palindromicBorders("abcacb") # 3
# palindromicBorders("ababa") # 5
# palindromicBorders("".join(["abcdefgh"[randint(0,7)] for i in range(10**3)])) # ~0.4 sec
palindromicBorders("".join(["abcdefgh"[randint(0,7)] for i in range(10**4)])) # ~40 sec
# palindromicBorders("".join(["abcdefgh"[randint(0,7)] for i in range(10**5)])) # ~40 sec
time() - start


string = raw_input()

print palindromicBorders(string)