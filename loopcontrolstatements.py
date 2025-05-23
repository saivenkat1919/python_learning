

# case conversion
# Input : PythonLearning
# Output : python_learning



#No of even's and odd's in range M,N
m=int(input())
n=int(input())
even=0
odd=0
for i in range(m,n+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print(odd)
print(even)



# program to print multiples of 3 among n numbers
n=int(input())
for i in range(n):
    number=int(input())
    if number%3==0:
        print(number)


# program to read n inputs and prints the given numbers unti a number is multiple of 5
n=int(input())
for i in range(n):
    number=int(input())
    if number%5==0:
        break
    else:
        print(number)



#program to print the Kth largest number of N
n=int(input())
k=int(input())
count=0
for i in range(n,0,-1):
    if n%i==0:
        count+=1
    if count==k:
        print(i)
        break
if count!=k:
    print(1)


# Program to print first prime number among n inputs
n=int(input())
for i in range(n):
    number=int(input())
    if number==1:
        continue
    if number==2 or number==3:
        print(number)
        break
    else:
        prime=1
        for i in range(2,number):
            if number%i==0:
                prime=0
                break
        if prime==1:
            print(number)
            break