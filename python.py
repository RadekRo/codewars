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

# favourite solution:
# return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')

# Challenge 9 - 6 kyu
# You live in the city of Cartesia where all roads are laid out in a perfect grid. 
# You arrived ten minutes too early to an appointment, so you decided to take the 
# opportunity to go for a short walk. The city provides its citizens with a Walk 
# Generating App on their phones -- everytime you press the button it sends you an 
# array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
# You always walk only a single block for each letter (direction) and you know it takes 
# you one minute to traverse one city block, so create a function that will return true 
# if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) 
# and will, of course, return you to your starting point. Return false otherwise.

def is_valid_walk(walk):
    x_axis = 0
    y_axis = 0
    for coord in walk:
        match coord:
            case "n": 
                y_axis += 1
            case "s":
                y_axis -= 1
            case "e":
                x_axis += 1
            case "w":
                x_axis -= 1
            case _: 
                print("Wrong coordinates entered!")
                break
    return x_axis == 0 and y_axis == 0 and len(walk) == 10

#TESTS
# print(is_valid_walk(["n", "e", "n", "e", "s", "w", "s", "w", "e", "w"]))
# print(is_valid_walk(["n", "e", "n", "e", "s", "w", "s", "w", "e", "w", "e", "w"]))
# print(is_valid_walk(["n", "e"]))
# favourite solution:
# return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

# Challenge 10 - 6 kyu

# Given an array of integers, find the one that appears an odd number of times.

def find_it(seq):
    for num in seq:
        if seq.count(num)%2 != 0:
            return num

# favourite solution:
# return [x for x in seq if seq.count(x) % 2][0]

# Challenge 11 - 8 kyu
# Create a function with two arguments that will return an array of the first n multiples of x.

def count_by(x, n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(x * i)
    return numbers

# favourite solution:
# return [i * x for i in range(1, n + 1)]

# Challenge 12 - 8 kyu

# In this simple assignment you are given a number and have to make it negative. 
# But maybe the number is already negative?

def make_negative( number ):
    return number if number <= 0 else number - number * 2

# favourite solution
# return -abs(number)

# Challenge 13 - 8 kyu

# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. 
# If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

def lovefunc(flower1, flower2):
    return (flower1 + flower2)%2 != 0

# favourite solution:
# return (flower1 + flower2)%2

# Challenge 14 - 6 kyu

# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time 
# required for all the customers to check out!
# input
# customers: an array of positive integers representing the queue. Each integer represents a customer, 
# and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.

def queue_time(customers, n):
    if n == 1 or len(customers) == 0:
        return sum(customers)
    elif n >= len(customers):
        return max(customers)
    else:
        tills = [0] * n
        for i in range(len(tills)):
            tills[i] = customers[0]
            del customers[0]
        time = 0
        while len(customers) > 0:
            for i in range(len(tills)):
                tills[i] -= 1
                if tills[i] == 0 and len(customers) > 0:
                    tills[i] = customers[0]
                    del customers[0]
            time += 1
        return max(tills) + time

# favourite solution:
# def queue_time(customers, n):
#    l=[0]*n
#    for i in customers:
#        l[l.index(min(l))]+=i
#    return max(l)

# Challenge 15 - 8 kyu

# our function takes two arguments:
# current father's age (years)
# current age of his son (years)
# ??alculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). 
# The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.

def twice_as_old(dad_years_old, son_years_old):
    years_ago_or_future = 0
    if son_years_old == 0:
        years_ago_or_future += 1
        son_years_old += 1
        dad_years_old += 1
    if dad_years_old / son_years_old > 2:
        while dad_years_old / son_years_old != 2:
            dad_years_old += 1
            son_years_old += 1
            years_ago_or_future += 1
    else:
        while dad_years_old / son_years_old != 2:
            dad_years_old -= 1
            son_years_old -= 1
            years_ago_or_future += 1
    return years_ago_or_future

# favourite solution:
# return abs(dad_years_old - 2*son_years_old)