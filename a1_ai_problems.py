# Complete your individualized AI problems here

"""1. Hello, World!
Write a Python program that prints "Hello, World!" to the console.

2. Basic Arithmetic
Create a Python program that:

Prompts the user to enter two numbers.
Calculates the sum, difference, product, and quotient of the numbers.
Prints out the results.
3. Even or Odd
Write a function is_even_or_odd(number) that determines if a number is even or odd. The function should return "Even" or "Odd".

4. Fibonacci Sequence
Write a Python function fibonacci(n) that returns the first n numbers in the Fibonacci sequence. For example, fibonacci(5) should return [0, 1, 1, 2, 3].

5. List Manipulation
Given a list of integers, write a function reverse_list(lst) that returns the list in reverse order. For example, reverse_list([1, 2, 3, 4]) should return [4, 3, 2, 1].

6. Palindrome Check
Write a function is_palindrome(s) that checks if a given string s is a palindrome (reads the same forwards and backwards). For example, is_palindrome("racecar") should return True.

7. Count Vowels
Create a function count_vowels(s) that counts and returns the number of vowels in a given string s. For example, count_vowels("hello") should return 2.

8. Simple Calculator
Implement a simple calculator with functions for addition, subtraction, multiplication, and division. The user should be able to choose an operation and input two numbers to get the result.

9. List Comprehension
Write a Python program that uses list comprehension to generate a list of squares of numbers from 1 to 10.

10. Dictionary Operations
Create a dictionary student_grades with keys as student names and values as their grades. Write a function add_grade(name, grade) to add a new student or update an existing student’s grade. Also, write a function get_average() to calculate the average grade of all students.

11. Prime Number Check
Write a function is_prime(n) that checks if a number n is a prime number. The function should return True if n is prime and False otherwise.

12. Factorial Calculation
Write a function factorial(n) that computes the factorial of a non-negative integer n. For example, factorial(5) should return 120.

13. File Handling
Create a Python script that:

Writes some text to a file.
Reads the content from the file and prints it to the console.
Appends additional text to the file.
14. Simple Quiz Program
Create a simple quiz program that:

Asks the user a few questions.
Checks the answers and gives a score at the end.
15. Temperature Converter
Write a Python program that converts temperatures between Celsius and Fahrenheit. Implement two functions: one for converting from Celsius to Fahrenheit and another for converting from Fahrenheit to Celsius."""
def helloWorld():
    print("Hello world!")

def arithmetic():
    x=input("num 1: ")
    y=input("num 2: ")
    print(x+y+""+x-y+""+x*y+""+x/y)

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

def even_or_odd(n):
    return "even" if n%2==0 else "odd"

def fibonacci(n):
    lst=[0]
    for i in n:
        if len(lst)==1:
            lst.append(1)
        else:
            lst.append(lst[i]+lst[i+1])
    return lst

def reverse_list(lst):
    reversed=[]
    for i in len(lst):
        reversed.append(lst[-i])
    return reversed

def is_palindrome(s):
    for i in len(s):
        if s[i]!=s[-i]:
            return False
    return True

def count_vowels(s):
    v=0
    l="aeiou"
    for i in len(s):
        for j in len(l):
            if s[i]==l[j]:
                v+=1
    return v



assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

