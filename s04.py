# a = int(input())
# b = int(input())
# if a>b:
#     a,b=b,a
# n=a
# while n<=b:
#     i=2
#     p=True
#     while i<n:
#         if n%i==0:
#             p=False
#         i+=1
#     if p and n!=1:
#         print(n)
#     n+=1




# def say_hello (name):
#     print("hello my name is:", name)



# say_hello("jangali")




# def add(a,b):
#     return a**b
# a=int(input())
# b=int(input())
# z=add(a,b)
# print(z)


# def add (a,b):
#     return a**b
# z=add(2,4)
# print(z)


# a = int(input())
# b = int(input())
# if a>b:
#     a,b=b,a
# n=a
# while n<=b:
#     i=2
#     p=True
#     while i<n:
#         if n%i==0:
#             p=False
#         i+=1
#     if p and n!=1:
#         print(n)
#     n+=1

# def addaval(a):
#     if a==1:
#         return False
#     if a==2:
#         return True
#     if a%2==0:
#         return False
#     i=3
#     p=True
#     while i<a:
#         if a%i==0:
#             return False
#         i+=1
#     return True
# z=addaval(12)
# print(z)



# n=int(input())
# i=0
# while i<n:
#     j=0
#     while j<n:
#         if i==0 or i==n-1:
#             print("*",end="")
#         else:
#             if j==0 or j==n-1:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         j+=1
#     print()
#     i+=1






# a=input()
# b=input()
# if int(a[::-1]) > int(b[::-1]):
#     print(f"{a}> {b}")
# else :
#     print(f"{a}< {b}")



# m= "shanbe,1shanbe 2shanbe,3shanbe "
# def split_str(s,char):
#     start,end=0,0
#     while end<len(s):
#         if m[end]==char or end==len(s)-1:
#             print(s[start:end])
#             start=end+1
#         end+=1

# split_str(m,",")

