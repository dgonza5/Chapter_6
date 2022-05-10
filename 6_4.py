

# def power(r, n):
#     print("form power()")
#     r = r + 1
#     print("R: ", r)
#     # print("N: ", n)
#     if r <= 100:
#         power(r, n)

# power(2, 3)

# def power(r , n):
#     value = 1
#     for i in range(1, n + 1):
#         value = r * value 
#     return value 

# print("result", power(2, 3))

def power(r , n):
    if n == 1:
        return r
    else:
        return r * power(r, n - 1) 

print("result", power(2, 3))