#3Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n
def divisible_by3_and4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


print(*divisible_by3_and4(30), sep=", ")

#5Implement a generator that returns all numbers from (n) down to 0.
n = int(input())

def nums(n):
    for i in range(n, 0, -1):
        yield i

print(*nums(n))

#2even numbers between 0 and n
n = int(input())

def even_numbers(n):
    even_nums = []
    for i in range(0, n + 1):
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums

nums = even_numbers(n)

print(*nums, sep=', ')

#4
l = int(input("Left bound: "))
r = int(input("Right bound: "))

def squares(l, r):
    for i in range(l, r + 1):
        yield i ** 2

print(*squares(l, r), sep=', ')

#1
n = int(input())

def generate_squares(n):
    squares = []
    for i in range(n + 1):
        squares.append(i**2)
    return squares
print(generate_squares(n))
