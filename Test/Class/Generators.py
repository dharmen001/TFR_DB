# What Generators are : A generators is a way output a sequence of values without actually having to hold those values
# in memory like you would in an array however the catch to generator is that you can't iterate backwards on them or
# reset them in any in any way if you want to do that you have to create a new generator
# so we are already familiar with few of generator functions one of the most popular ones is the X range function
# so the X range number giving you the next number you're asking for, for example you can use it in for loop


# for n in range(10):
#     print(n)

gen = iter(range(10))
print(next(gen))
print(next(gen))
print(next(gen))


gen = reversed('abcde')
print(next(gen))
print(next(gen))
print(next(gen))

# 1, 1, 2, 3, 5, 8, 13, 21, .....
# generator = a generator can have an ending meaning it eventually runs out of elements or it continues on generating
# elements forever and that's what we're going to do for this donaire just for simplicity place, you saw the range
# generator eventually runs out of things to generate and if you just want to cancel out the generator can just give it
# a return but if we're using the return keyword to exit out of the generator we need another keyword that will
# actually return us generative elements and that's why we have the yield keyword


def fib_gen():

    a, b = 0, 1

    yield a
    yield b

    while True:
        yield a + b
        a, b = b, a + b


f = fib_gen()
print(next(f))
print(next(f))
print(next(f))
print(next(f))

squares = (x*x for x in range(10))
#print(squares.next())
print(next(squares))
print(squares)
for n in squares:
    print(n)


squares_new = [x*x for x in range(10)]
print(squares_new)


# a number that is divisible by itself or by 1


# Why they are handy




# Why you want to use them



