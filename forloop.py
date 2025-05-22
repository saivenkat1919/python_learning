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


