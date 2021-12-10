#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <center><img src='../../BlueSoft_logo.png' width="500" height="208"/></center>
# 
# ___

# # Flow control exercises

# ### Exercise 1
# 
# Write code that:
# - prints `Hello` if `1` is stored in `spam` variable,
# - prints `Howdy` if `2` is stored in `spam`,
# - and prints `Greetings!` if anything else is stored in `spam`.

# In[ ]:


print("Input value of spam")
spam = int(input())

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')


# ### Exercise 2
# 
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number.
# 
# For example, if the user entered `10` the output should be `55` (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10).
# 
# Expected output:
# ```
# Enter your number.
# 10
# Sum is: 55
# ```

# In[ ]:


n = int(input("Enter number"))
sum = 0
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of numbers is: ", sum)


# ### Exercise 3
# 
# Write a program to print the following number pattern using a loop, where number of rows is given by the user.
# 
# Expected output:
# ```
# How many rows would you like to draw?
# 5
# 
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# ```

# In[ ]:


user_input = int(input("How many rows would you like to draw: "))

for row in range(user_input,0,-1):

   for col in range(1,row+1):

       print (col,end=" ")

   print()


# ### Exercise 4
# 
# Write a program to check the validity of password input by users.
# 
# - At least 1 letter between [a-z] and 1 letter between [A-Z].
# - At least 1 number between [0-9].
# - At least 1 character from [$#@].
# - Minimum length 6 characters.
# - Maximum length 16 characters.
# 
# Expected output:
# ```
# What is your password?
# MarekTracz1
# Invalid password format.
# ```
# or:
# ```
# What is your password?
# M@r3kTracz
# Registration successful.
# ```

# In[12]:


import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Registration successful.")
        x=False
        break

if x:
    print("Invalid password format.")


# ### Exercise 5
# 
# Write a program that reads two inputs representing a month and day and prints the season for that month and day.
# 
# Expected output:
# ```
# Input the month (e.g. January, February, etc.):
# December
# Input the day:
# 1
# At that day, the season is autumn.
# ```

# In[13]:


month = input("Input the month(e.g. January, February, etc.): ")
day = int(input("Input the day: "))

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'March') and (day > 19):
	season = 'spring'
elif (month == 'June') and (day > 20):
	season = 'summer'
elif (month == 'September') and (day > 21):
	season = 'autumn'
elif (month == 'December') and (day > 20):
	season = 'winter'

print("At that day, the season is",season)


# ### Exercise 6
# 
# Given a dictionary called `stocks` that contains both stock tickers and the corresponding stock prices, write code that prints out the formatted information in the table.
# 
# Expected output:
# ```
# -----------------------
# TICKER      PRICE (USD)
# -----------------------
# AAPL             165.30
# MSFT             330.59
# FB               324.46
# AMZN            3507.07
# TSLA            1144.76
# GOOGL           2837.95
# ```

# In[14]:


stocks = {
        'AAPL': 165.30,
        'MSFT': 330.59,
        'FB': 324.46,
        'AMZN': 3507.07,
        'TSLA': 1144.76,
        'GOOGL': 2837.95
        }

# Code here


# ### Exercise 7
# 
# The code below prints all perfect numbers from 1 to 100. Rewrite the `while` loop into `for` loop.
# 
# More information about perfect numbers here: [Wikipedia: Perfect number](https://en.wikipedia.org/wiki/Perfect_number).

# In[15]:


# solution using while and for loops

print('Shows Perfect number fom 1 to 100.')
n = 2
# outer while loop
while n <= 100:
    x_sum = 0
    # inner for loop
    for i in range(1, n):
        if n % i == 0:
            x_sum += i
    if x_sum == n:
        print('Perfect number:', n)
    n += 1


# In[ ]:


print('Shows Perfect number fom 1 to 100.')
n = 2
for i in range(1, 101): 
    x_sum = 0
    for i in range(1, n):
        if n % i == 0:
            x_sum += i
    if x_sum == n:
        print('Perfect number:', n)
    n += 1

