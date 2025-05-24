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

