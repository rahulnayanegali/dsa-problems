
# •Problem 2: Given two strings s and t , write a function to determine if t is an anagram of s.
# •Example: Input: s = "anagram", t = "nagaram” Output: true

# Approach 1
 # sort both s and t n logn
 # loop throught both and check if s[i] != t[i] return False else True
 
# Approach 2
 # split both s and t
 # for loop s:
      # if(s[i] in t):
          # remove t[s[i]]
    
  #if len(t) return False
  #else return True


def is_anagram(s, t):
  if len(s) != len(t):
    return False
  
  # s_arr = s.split('')
  # t_arr = t.split('')
  s_sorted = sorted(s)
  t_sorted = sorted(t)
  # return s
  for i in range(len(s_sorted)):
    if(s_sorted[i] != t_sorted[i]):
      return False
  
  return True

print(is_anagram("anagram", "nagaram"))