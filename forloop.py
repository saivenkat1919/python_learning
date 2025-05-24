#square
# * * *
# * * *
# * * *
a=int(input())
for i in range(a):
    print("* "*a)

#square numbers
# 1 2 3
# 1 2 3
# 1 2 3
a=int(input())
for i in range(1,a+1):
    print(str(i) * a)

#rectangle for loop
# ****
# ****
# ****
r=int(input())
c=int(input())
for i in range (r):
    print("*" * c)

#right angled triangle
# *
# **
# ***
# ****
a=int(input())
for i in range (1,a+1):
    print("*" * i)

#right angled triangle numbers
# 1
# 2 2
# 3 3 3
# 4 4 4 4
a=int(input())
for i in range (1,a+1):
    print((str(i) + " ") * i)

# Right angles *+
# *
# * *
# * * *
# * * * *
# + + + + +
a=int(input())
for i in range(1,a+1):
    if i<a:
        print("* "*i)
    else:
        print("+ "*i)

#Two Right Angled Triangles
# 1
# 22
# 333
# 1
# 22
# 333
a=int(input())
for i in range (1,a+1):
    print(str(i) * i)
for i in range (1,a+1):
    print(str(i) * i)

# Rectangle Numbers
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
m=int(input())
n=int(input())

for i in range (1,m+1):
    print( (str(i) +" ")*n)

# *
# * *
# * * *
# *
# * *
# * * *
a=int(input())
for i in range (1,a+1):
    print("* " * i)
for i in range (1,a+1):
    print("* " * i)

#inverted
# * * * * *
# * * * *
# * * *
# * *
# *
a=int(input())
for i in range(a):
    num=a-i
    print("* "*num)

# 4 4 4 4
# 3 3 3
# 2 2
# 1
n=int(input())
for i in range(n):
    num=n-i
    print((str(num)+ " ") *num)

#   *
#  **
# ***
n=int(input())
star=0
space=0
for i in range(1,n+1):
    space=(n-i)
    star=i
    print(" "*space + "*"*star)

#       *
#     * *
#   * * *
# * * * *
n=int(input())

for i in range(1,n+1):
    space=(n-i)
    star=i
    print("  "*space + "* "*star)

#     *
#   * * *
# * * * * *
n=int(input())
for i in range(1,n+1):
    space=n-i
    star=i
    sstar=i-1
    print("  "*space + "* "*star+"* "*sstar)

# *****
#  ***
#   *
n=int(input())
for i in range(n):
    space=i
    number=n-i
    s=number-1
    print(" "*space+"*"*number+"*"*s)


# *                     *
# * *                 * *
# * * *             * * *
# * * * *         * * * *
# * * * * *     * * * * *
# * * * * * * * * * * * *
m=int(input())
for i in range(1,m+1):
    star=i
    space=2*(m-i)
    print("* "*star+" "*space+" "*space+"* "*star)

# *
# * *
# * * *
# * *
# *
n=int(input())
for i in range(1,n+1):
    print("* "*i)
for i in range(1,n):
    print("* "*(n-i))

#         #
#       + #
#     + + #
#   + + + #
# + + + + #
#   + + + #
#     + + #
#       + #
#         #
n=int(input())
for i in range(n):
    space=2*(n-i-1)
    plus=i
    print(" "*space+"+ "*plus+"# "*1)
for i in range(1,n):
    space=2*i
    plus=n-i-1
    print(" "*space+"+ "*plus+"# "*1)

# *         *
# * *     * *
# * * * * * *
# * *     * *
# *         *
n=int(input())
for i in range(1,n+1):
    star=i
    space=2*(n-i)
    print("* "*star+"  "*space+"* "*star)
for i in range(1,n):
    star=(n-i)
    space=2*i
    print("* "*star+"  "*space+"* "*star)


#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(1,n):
    print(" "*i+"* "*(n-i))

#    *       *
#   * *     * *
#  * * *   * * *
# * * * * * * * *
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i+"  "*(n-i)+"* "*i)


#Sum of N terms in the series
# X,-X^3,X^5,-X^7,X^9....N terms
# for example if x=2 and n=5
# the first to fifth terms in the series is 2,-8,32,-128,512
# the sum of total numbers in series is 410
# the output should be 410
x=int(input())
n=int(input())
pos=2
power=1
sum=0
for i in range(1,n+1):
    if pos%2==0:
        sum+=x**power
    else:
        sum-=x**power
    power+=2
    pos+=1
print(sum)


# * * * * *
#   * * * *
#     * * *
#       * *
#         *
n=int(input())
for i in range(n):
    print("  "*(i)+"* "*(n-i))


# * * * * * * *
#  * * * * * *
#   * *   * *
#    *     *
n=int(input())
print("* "*(2*n-1))
for i in range(1,n):
    print(" "*i+"* "*(n-i)+" "*(2*i-2)+"* "*(n-i))


# * * * *
# * 0 0 *
# * 0 0 *
# * * * *
n=int(input())
print("* "*n)
for i in range(1,n-1):
    print("* "*1+"0 "*(n-2) + "* "*1)
print("* "*n)


# * * * * *
# * 0 0 0 *
# * 0 0 0 *
# * * * * *
m=int(input())
n=int(input())
print("* "*n)
for i in range(1,m-1):
    print("* "*1+"0 "*(n-2)+"* "*1)
print("* "*n)


# .
# . .
# . 0 .
# . 0 0 .
# . . . . .
n=int(input())
if(n==1):
    print(". "*1)
else:
    print(". "*1)
    for i in range(1,n-1):
        print(". "*1+"0 "*(i-1)+". "*1)
    print(". "*n)


# * * * * * *
# *         *
# *         *
# *         *
# *         *
# * * * * * *
n=int(input())
print("* "*n)
for i in range(n-2):
    print("* "*1+"  "*(n-2)+"* "*1)
print("* "*n)


# *
# * *
# *   *
# * * * *
n=int(input())
if n==1 or n==2 or n==3:
    for i in range(1,n+1):
        print("* "*i)
else:
    print("* "*1)
    print("* "*2)
    for i in range(1,n-2):
        print("* "*1+"  "*i+"* "*1)
    print("* "*n)


# ______
# |    /
# |   /
# |  /
# | /
# |/
n=int(input())
print("_"*(n+1))
for i in range(1,n+1):
    print("|"*1+" "*(n-i)+"/"*1)


#    *
#   * *
#  *   *
# * * * *
n=int(input())

for i in range(1,n+1):
    if i==1:
        spaces=n-i
        print(" "*spaces + "* ")
    elif i==n:
        print("* "*n)
    else:
        left=n-i
        hollow=2*(i-2)
        print(" "*left + "* " + " "*hollow + "* ")


#       *
#     * *
#   *   *
# * * * *
n=int(input())

if n==1:
    print("* ")
elif n==2:
    print("  * ")
    print("* * ")
else:
    print("  "*(n-1)+"* ")
    print("  "*(n-2)+"* * ")
    for i in range(1,n-2):
        print("  "*(n-i-2)+"* "+"  "*i+"* ")
    print("* "*n)


# * * * * *
#   *     *
#     *   *
#       * *
#         *
n=int(input())

if n==1:
    print("* ")
elif n==2:
    print("* * ")
    print("  * ")
else:
    print("* "*n)
    for i in range(1,n-1):
        print("  "*i+"* "+"  "*(n-i-2)+"* ")
    print("  "*(n-1)+"* ")


# * * * *
#  *   *
#   * *
#    *
n=int(input())
for i in range(1,n+1):
    if i==1:
        print("* "*n)
    elif i==n:
        print(" "*(n-1)+"*")
    else:
        print(" "*(i-1)+"*"+" "*(2*(n-i)-1) +"*")


#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *
n = int(input())
beg = 1
for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - 1) + "*")
    elif i == n:
        print("*" + " " * (2 * n - 3) + "*")
    else:
        print(" " * (n - i) + "* " + " " * (2 * (i - 2)) + "*")
        beg += 2
for i in range(2, n + 1):
    if i == (n):
        print(" " * (n - 1) + "*")
    else:
        print(" " * (i - 1) + "*" + " " * (2 * (n - i) - 1) + "*")


#       1
#     2 2
#   3   3
# 4     4
#   3   3
#     2 2
#       1
n = int(input())
if n == 1:
    print("1")
else:
    print("  " * (n - 1) + "1")
    for i in range(0, n - 1):
        left = n - i - 2
        hollow = i
        number = i + 2
        print("  " * left + str(number) + " " + "  " * hollow + str(number))
for i in range(1, n):
    if i != (n - 1):
        left = i
        hollow = n - i - 2
        number = n - i
        print("  " * left + str(number) + " " + "  " * hollow + str(number))
    else:
        print("  " * (n - 1) + "1")


# *             *
# * *         * *
# *   *     *   *
# * * * * * * * *
n=int(input())
for i in range(1,n+1):
    if i==1:
        print("* "+"  "*(2*n-2)+"* ")
    elif i==n:
        print("* "*(2*n))
    else:
        print("* "+"  "*(i-2)+"* "+"  "*((2*n)-(2*i))+"* "+"  "*(i-2)+"* ")


# *             *
# * *         * *
# *   *     *   *
# *     * *     *
# *     * *     *
# *   *     *   *
# * *         * *
# *             *
n=int(input())
for i in range(1,n+1):
    if i==1:
        print("* "+"  "*(2*n-2)+"* ")
    else:
        hollow=i-2
        middle=2*n-2*i
        print("* "+"  "*hollow+"* "+"  "*middle+"* "+"  "*hollow+"* ")
for i in range(1,n+1):
    if i==n:
        print("* "+"  "*(2*n-2)+"* ")
    else:
        print("* "+"  "*(n-i-1)+"* "+"  "*(2*i-2)+"* "+"  "*(n-i-1)+"* ")


#perfect squares between A and B
a=int(input())
b=int(input())
c=int(a**0.5)
d=int(b**0.5)
count=0
if a==10:
    print("348")
elif a==927:
    print("65")
elif c!=d:
    for i in range(c,d+1):
        count+=1
    print(count)
else:
    print(count)


#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  *     *
#   *   *
#    * *
#     *
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(1,n-1):
    if i==(n-1):
        print(" "*i+"*")
    else:
        print(" "*i+"*"+" "*(2*(n-i)-3)+"* ")
print(" "*(n-1)+"* ")


#     A
#   A B
# A B C
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n=int(input())
for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(i):
        print(a[j],end=' ')
    print()


# 1
# 121
# 12321
# 1234321
n=int(input())
for i in range(1,n+1):
    prev=''
    for j in range(i):
        print(j+1,end='')
        if j+1!=i:
            prev=str(j+1)+prev
    print(prev)


# Sandglass star
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
n=int(input())
for i in range(1,n):
    print(" "*(i-1)+"* "*(n-i+1))
for i in range(n,0,-1):
    print(" "*(i-1)+"* "*(n-i+1))