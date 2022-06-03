 
str1 = list(input())
  
str2 = list(input())
  
str1.sort()
  
str2.sort()
  
if str1 == str2:
    print("Anagram")
else:
    print("not Anagram")