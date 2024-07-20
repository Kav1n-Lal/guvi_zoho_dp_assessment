# Question 2: Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


def group_anagram(str_list):
  s=str_list
  s1=[]
  for i in s:
    r=sorted(list(i))
    y=''.join(r)
    if y not in s1:
      s1.append(y)

  group={}
  for j in s1:
    group[j]=[]

  for k in s:
    r=sorted(list(k))
    y=''.join(r)
    group[y].append(k)

  print(list(group.values()))

#s=["eat","tea","tan","ate","nat","bat"]
s=input().split()
group_anagram(s)