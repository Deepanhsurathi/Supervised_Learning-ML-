#!/usr/bin/env python
# coding: utf-8

# In[1]:


#[1]Write a function to generate the first n Fibonacci numbers using a loop. For example, if n = 6, the output should be 
# [0, 1, 1, 2, 3, 5].

def fibonacci(n):
    fibonacci_numbers = []
    if n <= 0:
        return fibonacci_numbers
    
    a, b = 0, 1
    
    for i in range(n):
        fibonacci_numbers.append(a)
        a, b = b, a + b
    return fibonacci_numbers

n = int(input("Enter the number of Digits : "))
print(fibonacci(n))


# In[2]:


# Write a function to compute the factorial of a given number using a loop. For example, factorial(5) should return 120.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Find the factorial : "))
print(factorial(n))  


# In[3]:


# Write a function that takes an integer and returns the sum of its digits. For example, for the number 1234, 
#the output should be 10 (1 + 2 + 3 + 4).

def sum_of_digits(number):
    number = abs(number)
    sum = 0
    while number > 0:
        sum = sum + number % 10
        number = number // 10
    return sum

number =int(input("Enter the number : "))
print(sum_of_digits(number))


# In[4]:


# Write a function to check if a given number is prime using a loop. For example, is_prime(29) should return True,
# and is_prime(10) should return False.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

print(is_prime(29)) 
print(is_prime(10))


# In[5]:


# Write a function to reverse a given string using a loop. For example, for the input "hello", the output should be "olleh".

def reverse_string(s):
    reversed_str = ""
    
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    
    return reversed_str

print(reverse_string("hello")) 


# In[6]:


#Write a function to check if a given string is a palindrome using a loop. For example, "madam" is a palindrome.

def is_palindrome(s):
    s = s.lower()
 
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        
        start += 1
        end -= 1
        
    return True

print(is_palindrome("madam")) 
print(is_palindrome("hello"))


# In[9]:


# Write a function that prints the multiplication table for a given number n up to 10.

def print_multiplication_table(n):
    for i in range(1, 11):
        product = n * i
        print(f"{n} x {i} = {product}")

print_multiplication_table(5)


# In[11]:


# Write a function that finds the largest number in a list using a loop. For example, given [4, 7, 1, 8, 3], 
# the output should be 8.

def largest_number(numbers):
    largest = numbers[0]
    
    for number in numbers:
        if number > largest:
            largest = number
    return largest

numbers = [4, 7, 1, 8, 3]
print(largest_number(numbers))  


# In[12]:


'''
# Write a function that prints a pattern of stars based on the number of rows provided. For example, if rows = 5, 
  the output should be:
*
**
***
****
*****
'''

n = int(input("Enter the number of rows : "))
print()
for i in range(1, n+1):
    for j in range(1,i+1):
        print("*", end="")
    print()


# In[16]:


# Write a function that takes a list of integers and returns two lists: one containing all the even numbers 
# and the other containing all the odd numbe
def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    return even_numbers, odd_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens, odds = separate_even_odd(numbers)
print("Even numbers:", evens)  
print("Odd numbers:", odds)  


# In[14]:


# Write a function that takes a string and returns the count of vowels and consonants. For example,
# for the input "hello world", the output should be {'vowels': 3, 'consonants': 7}.

def count(s):
    s = s.lower()
    vowels = 0
    consonants = 0
    for i in s:
        if i in 'aeiou':
            vowels += 1
        elif i.isalpha():
            consonants += 1
    return {'vowels': vowels, 'consonants': consonants}

s = input("Enter the string : ")
result = count(s)
print(result)


# In[15]:


'''
# Write a function that prints a number pattern based on a given integer n. For example, for n = 4, the output should be:
1
22
333
4444
'''

n = int(input("Enter the number of rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end="")
    print()


# In[17]:


# Write a function that prints all multiples of a given number up to a specified limit. 
# For example, for num = 3 and limit = 20, the output should be 3, 6, 9, 12, 15, 18.

def print_multiples(num, limit):
    for multiple in range(num, limit + 1, num):
        print(multiple, end=' ')
    print()  
    
print_multiples(3, 20)  


# In[18]:


# Write a function that takes a list of integers and returns a tuple with the sum of even numbers and the sum of odd numbers. 
# For example, for the list [1, 2, 3, 4, 5, 6], the output should be (12, 9).

def sum(numbers):
    even = 0
    odd = 0
    for num in numbers:
        if num % 2 == 0:
            even += num
        else:
            odd += num
    return (even, odd)

num = [1, 2, 3, 4, 5, 6]
result = sum(num)
print(result)


# In[ ]:




