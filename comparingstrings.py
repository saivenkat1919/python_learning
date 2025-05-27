# every character has a UNICODE value
# "A"=65 and "z"=122
# "1"=49 , "*"=42

# printing ascii value of "A"
# using "ord"
print(ord("A"))

# printing character with ASCII value
# using chr
print(chr(75))
# output : K

# Unicode Ranges
# 48 - 57 -> Number Digits (0 - 9)
# 65 - 90 -> Capital Letters (A - Z)
# 97 - 122 -> Small Letters (a - z)

# printing characters from A(65) to Z(90)
for unicode_value in range(65,91):
    print(chr(unicode_value))


# Comparing Strings
# In Python, strings are compared considering unicode
print("A" < "B")
# Output: True
# As unicode value of A is 65 and B is 66,
# which internally compares 65 < 66 . So the output should be True


# Character by Character Comparison
# In Python, String Comparison is done character by character.
print("BAD" >= "BAT")
# output : False

# print unicode values
# input : code
# output =
# 99
# 111
# 100
# 101
s=input()
for i in s:
    print(ord(i))


# count of characters
# input :
# google
# 111
# output:
# 2
s=input()
n=int(input())
count=0
for i in s:
    if ord(i)==n:
        count+=1
print(count)


# print smallest letter in a word
s=input()
small=200
for i in s:
    if ord(i)<small:
        small=ord(i)
print(chr(small))


# Unicode value of first capital letter in word
# input : proGrammeR
# output : 71
s=input()
ans=''
for i in s:
    if i.isupper():
        ans=i
        break
print(ord(ans))


# take input of unicode of letters and print the word
# input
# 3
# 67 97 114
# output:
# Car
n=int(input())
for i in range(n):
    m=int(input())
    print(chr(m),end='')


# Next Characters
s=input()
for i in s:
    print(chr(ord(i)+1))

# previous characters
s=input()
for i in s:
    if i==' ':
        continue
    else:
        print(chr(ord(i)-1))


# first word in dictionary order
# input : He is bit slow
# Output : bit
s = input()

first_word = s
word = ""

for i in range(len(s)):
    char = s[i]
    word += char

    if char == " " or i == len(s) - 1:
        if word.lower() < first_word.lower():
            first_word = word
        word = ""

print(first_word)
