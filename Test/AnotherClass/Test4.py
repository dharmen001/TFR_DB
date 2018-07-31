# def double(x):
#
#     if x == 0:
#         return 0
#
#     return double(x-1) * 3
#
#
# print(double(2))

# 4-> 2
# 3-> 2
# 2-> 2
# 1-> 2
# 0-> 0


# def tri(n):
#     if n == 0:
#         return 0
#     return tri(n-1) + n
#
#
# for N in range(10):
#     print(tri(N))

# 343 -> 10
# 111222 -> 9

# def sum_digits(n):
#     if n == 0:
#         return 0
#     return sum_digits(n/10) + n % 10
#
#
# print(sum_digits(111222))
# print(sum_digits(989))
# print(sum_digits(343))


# YYXXXYYX = 4
# XXYYXYYY = 3


# def count_x(str_x):
#
#     if str_x == '':
#         return 0
#
#     last_num = str_x[-1]
#
#     if last_num == 'X':
#         return count_x(str_x[:-1]) + 1
#     return count_x(str_x[:-1]) + 0
#
#
# print(count_x('YYXXXYYX'))
#
# print(count_x('XXYYXYYY'))


# 0! = 1
# 1! = 2
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4

# def factorial(x):
#     if x in (0, 1):
#         return 1
#     return factorial(x-1) * x
#
#
# for x in range(10):
#     print(factorial(x))

# 0,1,1,2,4,8,16,32,64

def fib(n):

    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


N = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(N):
    print(fib(i)),


















