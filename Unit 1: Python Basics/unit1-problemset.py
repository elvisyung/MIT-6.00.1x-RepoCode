# Problem Sets

# Problem Set 1 
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print: 
# Number of vowels: 5

s = "azcbobobegghakl"
count = 0
vowels = ['a' , 'e' , 'i' ,'o' , 'u']
for letter in s:
    if letter in vowels: 
        count += 1
print ('Number of vowels: ' + str(count)) 

# ---------------------------------------------

# Problem Set 2 
# Write a program that prints the number of times the string 'bob' occurs in s:
s = "azcbobobegghakl"
count = 0
for n in range(len(s)):
    if s[n:n+3] == "bob":
        count += 1
print("Number of times bob occurs is:" + str(count))

#----------------------------------------------

# Problem Set 2
# Write a program that prints the longest substring of s in which the letters
# occur in alphabetical order.

count = 0
maxcount = 0
result = 0

for char in range(len(s) - 1):
    if (s[char] <= s[char + 1]):
        count += 1
        if count > maxcount:
            maxcount = count
            result = char + 1
    else:
        count = 0
startposition = result - maxcount
print('Longest substring in alphabetical order is:', s[startposition:result + 1])



