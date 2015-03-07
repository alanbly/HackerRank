def substrings(string) :
  if len(string) == 1 :
    return [string];
  subs = substrings(string[1:]);
  return [string[0]+i for i in subs]+subs+[string[0]];

#substrings("xyz")


def subTail(string, prefix = "") :
  if len(string) == 1 :
    return [prefix, prefix+string];
  return subTail(string[1:], prefix)+subTail(string[1:], prefix+string[0])

#subTail("xyz")[1:]


# The first line contains the number of test cases T. T testcases follow. 
# Each testcase has 2 lines. The first line is an integer N ( the length of the string). 
# The second line contains the string S.

number = int(raw_input())

strings = []
for i in range(number) :
  length = int(raw_input())
  strings.append(raw_input())

for string in strings :
  sub = substrings(string)
  sub.sort()
  for i in sub : print i