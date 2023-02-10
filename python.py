# These are the solutions of the codewars.com challenges in Python language

# Challenge 1 - 7 kyu
# check if the provided number is a perfect square

def is_square(n):  
    if n < 0:
        return False
    else:
        calc_base = n ** 0.5
        return calc_base - int(calc_base) == 0

print(is_square(-1))
print(is_square(0))
print(is_square(4))
print(is_square(7))