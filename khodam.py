# my_list =["a","b","c","c","c","a","a","a","b"]
# my_list2=[]
# for i in set (my_list):
#     my_list2.append([i,my_list.count(i)])
# print(my_list2)

# a=(int(input("enter a")))
# b=int(input("enter b"))
# if a==1 and b==1:
#     pass
# elif a==1 and b==2:
#     print(2)
# elif a==2 and b==2:
#     print(2)
# else:
#     if a==1 or a==2 :
#         print(2)
#     if a % 2 == 0:
#         start_point=a+1
#     else:
#         if a==1:
#             start_point=2
#         else:
#             start_point=a
#     if b % 2 == 0:
#         end_point=b-1
#     else:
#         end_point=b
#     for i in range(start_point,end_point+1,2):
#         is_prime=True
#         for j in range(2,int(i**0.5)+1,2):
#             if i%j==0:
#                 is_prime=False
#                 break
#         if is_prime:
#             print(i)




# a=input()
# b=(a[::-1])
# if a==b:
#     print("yes")
# else:
#     print("no")




a=input()
b=input()
if int(a[::-1]) > int(b[::-1]):
    print(f"{a}> {b}")
else :
    print(f"{a}< {b}")
