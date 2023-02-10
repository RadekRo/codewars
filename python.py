# These are the solutions of the codewars.com challenges in Python language

# Challenge 1 - 7 kyu
# check if the provided number is a perfect square

def is_square(n):  
    if n < 0:
        return False
    else:
        calc_base = n ** 0.5
        return calc_base - int(calc_base) == 0

# TESTS
# print(is_square(-1))
# print(is_square(0))
# print(is_square(4))
# print(is_square(7))

# Challenge 2 - 7 kyu
# find a sum of provided TWO numbers and ALL between them. Numbers given unorderer.

def get_sum(a,b):
    if a == b:
        return a
    else:
        arr = [a, b]
        sum = 0
        arr.sort()
        for i in range(arr[0], arr[1]+1):
            sum += i
        return sum
    
#TESTS
#print(get_sum(2,2))
#print(get_sum(-1,0))
#print(get_sum(5,3))