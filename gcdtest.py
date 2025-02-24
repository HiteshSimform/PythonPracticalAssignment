# # Python program to find GCD of two numbers


# # Recursive function to return gcd of a and b
# def gcd(a, b):

#     # Everything divides 0
#     if (a == 0):
#         return b
#     if (b == 0):
#         return a

#     # Base case
#     if (a == b):
#         return a

#     # a is greater
#     if (a > b):
#         return gcd(a-b, b)
#     return gcd(a, b-a)


# # Driver code
# if __name__ == '__main__':
#     a = 25
#     b = 14
#     if(gcd(a, b)):
#         print('GCD of', a, 'and', b, 'is', gcd(a, b))
#     else:
#         print('not found')

# # This code is contributed by Danish Raza


# # 


a=11
b=20
x=0
flag=False
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        x=i
        flag=True
if flag==True:
    print(x)
else:
    print(1)