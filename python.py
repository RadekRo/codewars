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
# return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

# Challenge 4 - 8 kyu

# Create a function that takes an integer as an argument 
# and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# TESTS
# print(even_or_odd(3))

# Challenge 5 - 7 kyu

# Write a function which takes a list of strings 
# and returns each line prepended by the correct number.

def number(lines):
    for i in range(0, len(lines)):
        lines[i] = f"{i + 1}: {lines[i]}"
    return lines

# TESTS
# print(number(["a", "b", "c"]))
# print(number([]))
# favourite solution:
# return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]

# Challenge 6 - 6 kyu (level up mode)

# Return the sum of all the multiples of 3 or 5 below the number passed in. 
# Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    set_of_numbers = set()
    for i in range(0, number):
        if i%3 == 0 or i%5 == 0:
            set_of_numbers.add(i)
    print (sum(set_of_numbers))

# TESTS
# solution(20)
# favourite solution:
# return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])

# Challenge 7 - 6 kyu

# The goal of this exercise is to convert a string to a new string where 
# each character in the new string is "(" if that character appears only 
# once in the original string, or ")" if that character appears more than once in the original string. 

def duplicate_encode(word):
    word = word.upper()
    coded_word = []
    for i in range(0, len(word)):
        if word.count(word[i]) > 1:
            coded_word.append(")")
        else:
            coded_word.append("(")
    return "".join(coded_word) 

# favourite solution:
# return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# Challenge 8 - 8 kyu

# Complete the function so that it finds the average of the three scores passed 
# to it and returns the letter value associated with that grade.

def get_grade(s1, s2, s3):
    score = (s1+s2+s3)/3
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'