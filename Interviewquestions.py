


# h = "hello how  hi how do doing"
# h1 = [ ]
# for item in h.split():
#     if item[0] == 'h':
#         h1.append(item)
#     else:
#         print(item)


# for index,item in enumerate(h):
#     if item=='n':
#         print(item,index)
    
# def positive(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args,**kwargs)
#         return result * -1
#     return wrapper
# @positive
# def sub(a,b):
#     return a - b

# print(sub(10,20))


# from itertools import islice

# with open(r"K:/Python Notes/Pdf's/sample.log") as file:
#     n = 3
#     lastline = 0
#     for line in file:
#         lastline += 1
#     file.tell()
#     file.seek(0)
#     result = islice(file,lastline-n,n)
#     print(list(result))

# print(1,2,3,4,end='\n')

# lst = ["hello",12,12.5]
# lst2 = [ ]
# res = ""
# for item in lst:
#     if isinstance(item,(int,float)):
#         item = str(item)
#     lst2.append(item)
#     res = item +","+ res
# print(res.split())




# lst = [1,2,1,2,3,5,3]
# lst2 = []
# for item in lst:
#     if lst.count(item)>1:
#         if item  not in lst2:
#             lst2.append(item)
# print(lst2)

# lst = range(1,7)
# dd = {}
# for index,item in enumerate(lst):
#     if item not in dd:
#         dd[index] = index * 2 
# print(dd)

# string = "sony India"
# lstcomp = [string[2:],string[6:]]
# print(lstcomp)

# for i in range(1,101):
#     if i%3==0:
#         print(i)

# lst1 = [1,2,3]
# lst2 = [4,5,6]

# def add(lst1,lst2):
#     return  lst1 + lst2

# res = map(add,lst1,lst2)
# print(list(res))

# class Calculator:

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b

#     def sub(self):
#         return self.a - self.b

# # c = Calculator(5,3)
# # d = c.add()
# # e = c.sub()
# # print(c.__dict__)
# # print(d)
# # print(e)

# # integer = 121
# # d=str(integer)
# # res =""
# # while integer>0:
# #     res +=str(integer%10)
# #     integer = integer//10
# # if res==d:
# #     print(res,"it is palindrome number")
# # else:
# #     print(res,"it is not palindrome number")


# integers = "121"
# res=""
# for integer in integers:
#     res = integer + res
# print(int(res))
# if(res == integers):
#     print(res,"it is a palindrome number")
# else:
#     print(res,"it is not a palindrome number")

# n=int(input("enter the number"))
# tem=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if tem==rev:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

# def even(n):
#     for i in range(n):
#         if i % 2 ==0:
#             yield i
    
# fa = even(10)
# while(True):
#     print(next(fa))

# lst = [1,2,3,4,5]
# a = int(input("enter a value"))
# b = int(input("enter b value"))
# def add(a,b):
#     return a+b
# f = add(a,b)
# for i in lst:
#     if f==i:
#         print("present")


# expected_status = "Response [200]"
# url = f"https://reqres.in/api/users?page=2"
# response = request("GET", url)
# response_text = response.text
# d = loads(response_text)
# actual_status = response
# assert actual_status.status_code==200
# fname = d['data']
# count = 0
# for item in fname:
#     if isinstance(item,dict):
#         for key,value in item.items():
#             if key == 'id':
#                 count += 1
# print(count)


# import random 
# n = random. randint(10,30)
# print(n)          


# (i,*l,p) =[12, 34, 56, 78]
# print([p,*l,i])


# ip = [1, 2, 3, 4, 5, 6, 7, 9, 10]
# for i in range(1,11):
#     if i not in ip:
#         print(i)
