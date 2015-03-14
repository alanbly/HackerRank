# https://www.hackerrank.com/contests/w14/challenges/palindromic-border

def isPalindrome(num) :
  string = str(num)
  bottomHalf = len(string)/2
  topHalf = (len(string)-1)/2
  return string[:bottomHalf] == string[:topHalf:-1]

def getBorders(string) :
  biggest = 0
  limit = len(string)
  # print limit
  while biggest < limit and string[biggest] == string[-1-biggest] :
    # print "%s = %s" % (string[biggest], string[-1-biggest])
    biggest += 1;
  # print biggest
  # print string[:biggest]
  return 0 if biggest == 0 else sum(1 for i in range(1,min(limit,biggest+1)) if isPalindrome(string[:i]))

# getBorders("abca") # 1
# getBorders("ababa") # 2
# getBorders("lololol") # 3


def substrings(string) :
  for i in range(len(string)) :
    for j in range(i+1, len(string)+1) :
      yield string[i:j]

# tuple(substrings("abcacb"))


def palindromicBorders(string) :
  return sum(map(getBorders, substrings(string)))

# palindromicBorders("abcacb") # 3
# palindromicBorders("ababa") # 5


string = raw_input()

print palindromicBorders(string)