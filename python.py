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
        arr_sum = 0
        arr.sort()
        for i in range(arr[0], arr[1]+1):
            arr_sum += i
        return arr_sum

# TESTS
# print(get_sum(2,2))
# print(get_sum(-1,0))
# print(get_sum(5,3))
#   favourite solution:
#   return sum(range(min(a, b), max(a, b) + 1))

# Challenge 3 - 6 kyu (level up mode)
# Write a function that takes in a string of one or more words, 
# and returns the same string, but with all five or more letter words reversed

def spin_words(sentence):
    sentence_words = sentence.split(" ")
    result = []
    for word in sentence_words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    print(" ".join(result))

# TESTS   
# spin_words("Welcome")
# spin_words("cup")
# spin_words("CodeWars")
# spin_words("Take me home to the place where I belong")
# favourite solution:
#  return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

# Challenge 4 - 8 kyu
# Create a function that takes an integer as an argument 
# and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# TESTS
# print(even_or_odd(3))