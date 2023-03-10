# Problem 1: Anagram Checker
'''Solution'''

def is_anagram(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


print("Anagram Checker Program ")
str1 = input("Enter your first Word\n")
str2 = input("Enter your Second Word\n")
if(is_anagram(str1,str2)):
    print("Thay are Anagram Words")
else:
    print("Thay are Not Anagram Words")
    

