'''
Fizzbuzz:

Write a program that prints the numbers from 1 to 100. But

-- for multiples of three print "Fizz" instead of the number
-- for the multiples of five print "Buzz".
-- for numbers which are multiples of both three and five print "FizzBuzz".
'''


def divisible3(num):
    if num % 3 == 0:
        return True
    return False


def divisible5(num):
    if num % 5 == 0:
        return True
    return False


def divisible35(num):
    if divisible3(num) and divisible5(num):
        return True
    return False


def fizzbuzz(inp):
    output = []

    for n in inp:
        if divisible35(n):
            output.append('FizzBuzz')
        elif divisible3(n):
            output.append('Fizz')
        elif divisible5(n):
            output.append('Buzz')
        else:
            output.append(n)
    return output


numbers = range(1, 100)

print('Result:\n', fizzbuzz(numbers))
