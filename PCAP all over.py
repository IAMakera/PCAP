# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:52:49 2020

@author: Abdulrahman Isah
"""

# 2.1.4.10 LAB: Operators and expressions

# =============================================================================
# x = int(input('Enter the value of x: ')) # hardcode your test data here
# x = float(x)
#  write your code here
# 
# y = 3*x**3 - 2*x**2 + 3*x -1
# print("y =", y)
# =============================================================================


# =============================================================================
# hour = int(input("Starting time (hours ): "))
# mins = int(input("Starting time(minutes):  "))
# dura = int(input("Event duration (minutes): "))
# 
# hour = (hour + ((dura + mins) // 60)) % 241
# mins = ((mins + dura) % 60)
# print("Expected Output: ", hour, ':', mins)
# =============================================================================

# =============================================================================
# n = int(input('Enter a number: '))
# print(n >= 100)
# =============================================================================

# =============================================================================
# #read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2

# # print the result
# print("The larger number ", larger_number)
# =============================================================================
 
# =============================================================================
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
# 
# # =============================================================================
# # largest_number = number1
# # if number2 > largest_number:
# #     largest_number = number2
# # if number3 > largest_number:
# #     largest_number = number3
# # 
# # print("The largest number is:", largest_number)
# # =============================================================================
# 
# print(max(number1, number2, number3))
# =============================================================================

# =============================================================================
# spat_lover = input("Guess the name of the plant i love: ")
# 
# if spat_lover == 'SPATHIPHYLLUM':
#     print(" Yes ", spat_lover, 'is the best plant ever! ')
# elif spat_lover == 'Spathiphyllum':
#     print('No, I want a big Spathiphyllum!')
# else:
#     print('Spathiphyllum! Not [input]!')
# =============================================================================

# =============================================================================
# income = float(input("Enter the annual income: "))
# 
# if income <= 85528:
#     tax = 0.18 * income - 556.02
# elif income > 85528:
#     tax = 14839.02 + (0.32*(income-85528))
# if tax <= 0:
#     tax = 0
# tax = round(tax, 0)
# 
#     
# print("The tax is: ", tax, "Thalers")
# =============================================================================

# =============================================================================
# year = int(input("Enter a year: "))
# 
# if year >= 1582:
#     if (year % 4) != 0:
#         print('Common Year')
#     elif (year % 100) != 0:
#         print('Leap year')
#     elif (year % 400) != 0:
#         print('Common Year')
#     else:
#         print('It\'s a leap Year')
# if year < 1582:
#     print('Not within the Gregorian Calendar Period')
# =============================================================================

# =============================================================================
# largest_number = -999999999
# 
# number = int(input("Enter a number or type -1 to stop: "))
# while number != -1:
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to stop: "))
#     
# print("The largest number is:", largest_number)
# =============================================================================

# =============================================================================
# odd_numbers = 0
# even_numbers= 0
# 
# number = int(input('Enter a number or type 0 to stop: '))
# 
# while number != 0:
#     if (number % 2) == 1:
#         odd_numbers += 1
#     else:
#         even_numbers += 1
#     number = int(input('Enter a number or type 0 to stop: '))
# print('We have ', odd_numbers, 'odd numbers', even_numbers, 'even number')
# =============================================================================

# =============================================================================
# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)
# =============================================================================

# =============================================================================
# secret_number = 777
# print(
# """
#  +================================+
#  | Welcome to my game, muggle!    |
#  | Enter an integer number        |
#  | and guess what number I've     |
#  | picked for you.                |
#  | So, what is the secret number? |
#  +================================+
#  """)
#  
# number = int(input("So tell me the secret number: "))
# while number != 777:
#     print("Ha ha! You're  stuck in my loop!")
#     number = int(input("So tell me the secret number: "))
# print("Well done, muggle! You are free now.")
# =============================================================================

# =============================================================================
# for i in range(2, 8, -8):
#     print("The value of i is currently ", i)
# =============================================================================

# =============================================================================
# 

# =============================================================================
# import time
# for i in range (5):
#     i += 1
#     print(i, "Mississippi")
#     time.sleep(1)
# =============================================================================
     

# =============================================================================
# print("The break instruction: ")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")
# 
# 
# 
# 
# # continue
# 
# print("\n The continue instructio: ")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop. ", i)
# print("Outside the loop", i)
# =============================================================================

# =============================================================================
# largest_number = -99999999
# counter = 0
# 
# number = int(input("Enter a number or type -1 to end program: "))
# while True:
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end program: "))
# print('Largest Number is : ', largest_number, counter)
# =============================================================================
# =============================================================================
# if counter != 0:
#     print('Largest number is: ', largest_number)
# else:      
#     print('You havent entered any number')
# check = input('You want to know total number your entered')
# if check == 'Yes':
#     print(counter)
# else:
#     'Never Mind'
# =============================================================================


# =============================================================================
# wordWithoutVowels = ""
# userWord = input("Please Enter a word: ")
# userWord = userWord.upper()
# for letter in userWord:
#     if letter == 'A':
#         continue
#     elif letter == 'E':
#         continue
#     elif letter == 'I':
#         continue
#     elif letter == 'O':
#         continue
#     elif letter == 'U':
#         continue
#     
#     else:
#         wordWithoutVowels += letter
# print(wordWithoutVowels)
# =============================================================================

# =============================================================================
# 
# userWord = input("Please Enter a word: ")
# userWord = userWord.upper()
# for letter in userWord:
#     if letter == 'A':
#         continue
#     elif letter == 'E':
#         continue
#     elif letter == 'I':
#         continue
#     elif letter == 'O':
#         continue
#     elif letter == 'U':
#         continue
#     print(letter, end='')
# =============================================================================
# =============================================================================
# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else: ", i)
# =============================================================================

# =============================================================================
# blocks = int(input("Enter the number of blocks: "))
# 
# height = 0
# 
# rows = 1
# 
# while rows <= blocks:
#     
#     height += 1
#     blocks -= rows
#     if blocks <= rows:
#         break
#     rows += 1
# print("The height of the pyramid: ", height)
# =============================================================================

# =============================================================================
# counter = 5
# while counter > 2:
#     counter -= 1
#     print(counter)    
# =============================================================================
# =============================================================================
# 
# word = "python" 
# for letter in word:
#     print(letter, end='*')
# =============================================================================

# =============================================================================
# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i)
# =============================================================================
# =============================================================================
# 
# text = "OpenEDG Python Institute"
# for letter in text:
#     if letter == "P":
#         break
#     print(letter, end='')
# =============================================================================
# =============================================================================
# 
# for i in range(0, 3):
#     print(i)
# else:
#     print(i, 'else')
# =============================================================================
# =============================================================================
# 
# var = 32
# 
# varRight = var >> 1
# varLeft = var << 1
# print(var, varLeft, varRight)
# =============================================================================


# =============================================================================
# x = 4
# y = 1
# 
# a = x & y 
# b = x | y
# c = ~x
# d = x ^ 5
# e = x >> 2
# f = x << 2 
# 
# print(a, b, c, d, e, f)
# =============================================================================

# =============================================================================
# myList = [10, 1, 8, 3, 5]
# total = 0
# 
# for i in myList:
#     total += 1
# 
# print(total)
# =============================================================================

# =============================================================================
# numbers = [1, 2, 3, 5, 6, 7, 6, 8, 9]
# 
# del(numbers[0:2])
# print(len(numbers))
# =============================================================================

# =============================================================================
# hatList = [1, 2, 3, 4, 5]
# print(len(hatList))
# middleNumber = int(input("Please Enter the middle number: "))
# hatList[2] = middleNumber
# del(hatList[4])
# print(hatList)
# =============================================================================

# =============================================================================
# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)
# 
# numbers.append(4)
# 
# print(len(numbers))
# print(numbers)
# 
# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)
# =============================================================================

# =============================================================================
# myList = []
# 
# for i in range(5):
#     myList.insert(0, i + 1)
# print(myList)
# =============================================================================

# =============================================================================
# myList = [10, 1, 8, 3, 5]
# total = 0
# 
# for i in range(len(myList)):
#     total += myList[i]
# print(total)
# =============================================================================

# =============================================================================
# myList = [10, 1, 8, 3, 5]
# total = 0
# 
# for i in myList:
#     total += i
# print(total)
# =============================================================================

# =============================================================================
# myList = [2, 4, 1, 8, 10, 9]
# length = len(myList)
# 
# for i in range(length // 2):
#     myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]
# print(myList)
# =============================================================================

# =============================================================================
# beatles = []
# print("Step 1:", beatles)
# 
# beatles.append('John Lennon')
# beatles.append('Paul McCartney')
# beatles.append('George Harrison')
# print("Step 2:", beatles)
# 
# print("Step 3:", beatles)
# for i in range(2):
#     newMembers = input("Enter the new Members name")
#     beatles.append(newMembers)
# print("Step 4:", beatles)
# del beatles 
# print("Step 4:", beatles)
# 
# print("The Fab", len(beatles))
# =============================================================================

# =============================================================================
# myList = [8, 10, 6, 2, 4] #list to sort
# for i in range(len(myList) - 1): # we need (5 - 1) comparisons
#     if myList[i] > myList[i + 1]: #compare adjacent elements
#         myList[i], myList[i + 1] = myList[i + 1], myList[i]     
# print(myList)        
# =============================================================================

# =============================================================================
# myList = [8, 10, 6, 2, 4]
# swapped = True #it's a little fake - we need to enter the while loop
# 
# while swapped:
#     swapped = False # no swaps so far
#     for i in range(len(myList) - 1): 
#         if myList[i] > myList[i + 1]:
#             swapped = True # swap occured
#             myList[i], myList[i + 1] = myList[i +1], myList[i]
# print(myList)
# =============================================================================

# =============================================================================
# myList = [8, 10, 6, 2, 4]
# swapped = True
# swapCounter = 0
# while swapped:
#     swapped = False
#     for i in range(len(myList) - 1): 
#         if myList[i] > myList[i + 1]:
#             swapCounter += 1
#             swapped = True # swap occured
#             myList[i], myList[i + 1] = myList[i +1], myList[i]
#             print(myList, swapCounter)
# print(myList)
# =============================================================================

# =============================================================================
# myList = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))
# 
# for i in range(num):
#     val = float(input("Enter a list element: "))
#     myList.append(val)
# 
# while swapped:    
#     swapped = False
#     for i in range(len(myList) - 1):
#         if myList[i] > myList[i + 1]:
#             swapped = True
#             myList[i], myList[i + 1] = myList[i + 1], myList[i]
# print("\nSorted: ")
# print(myList)
# =============================================================================

# =============================================================================
# myList = [10, 8, 6, 4, 2]
# newList = myList[1:5]
# print(newList)
# =============================================================================

# =============================================================================
# myList = [10 , 8, 6, 5, 3]
# toFind = 5
# for i in myList:
#     if toFind in i:
#         break
# print(i)
# =============================================================================
    
#The in and not in operators

# =============================================================================
# myList = [0, 3, 12, 8, 2]
# 
# print(5 in myList)
# print(5 not in myList)
# print(12 in myList)
# 
# =============================================================================

# =============================================================================
# myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = myList[0]
# 
# for i in myList:
#     if i > largest:
#         largest = i
# print(largest)
# 
# for i in range(len(myList)):
#     if myList[i] > largest:
#         largest = myList[i]
# print(largest)
# 
# for i in myList[1:]:
#     if i > largest:
#         largest = i
# print(largest)
# =============================================================================

# =============================================================================
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# toFind = 5
# found = False
# 
# for i in range(len(myList)):
#     found = myList[i] == toFind
#     if found:
#         break
# if found:
#     print("Element found at index", i)
# else:
#     print("absent")
# =============================================================================
    
# =============================================================================
# myList = [5, 2, 3, 4, 1, 6, 7, 8, 9, 10]
# toFind = 5
# found = False
# 
# for i in myList:
#     found = i == toFind
#     if found:
#         break
# if found:
#     print("Element found at index", i)
# else:
#     print("absent")
#     
# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0
# =============================================================================

# =============================================================================
# for number in bets:
#     if number in drawn:
#         hits += 1
# print(hits)
# =============================================================================

# =============================================================================
# myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# count = 0
# rept = []
# for i in myList:
#     i in myList
#     del myList[i]
#     print(myList)
#     count += 1
#     
#     rept.append(myList[i])
# print(myList, count, '\n', rept)
# 
# =============================================================================

# =============================================================================
# board = []
# EMPTY = "**"
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)
# 
# print(board)
# =============================================================================

# =============================================================================
# empty = "*"
# board = [[empty for i in range(8)] for j in range(8)]
# print(board)
# =============================================================================

# =============================================================================
# EMPTY = "-"
# ROOK = "ROOK"
# board = []
# KNIGHT = 'ME'
# 
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)
#     
# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK
# 
# board[4][2] = KNIGHT
# board[3][4] = "PAWN"
# 
# print(board)
# =============================================================================

# =============================================================================
# row = []
# 
# for i in range(8):
#     row.append("me")
# 
# print(row)
# =============================================================================

# =============================================================================
# row = [i + 1 for i in range(8)]
# print(row)
# =============================================================================

# =============================================================================
# a = [i for i in range(20)]
# b = a[::-1]
# 
# print(b)
# print(a)
# =============================================================================

# =============================================================================
# b = []
# a = []
# 
# for i in range(10):
#     num = input("Enter anything you like: ")
#     b.append(num)
#     a = b[::-1]
# print(b)
# print(a)     
# =============================================================================

# =============================================================================
# a = [[i for i in range(10)] for j in range(20, 40, 2)]
# a[9][9] = 30
# print(a[9])
# total = 0
# 
# for day in a:
#     total += day[9]
#     print(day[9])
# print(total)
# =============================================================================

# =============================================================================
# temps = [[0.0 for h in range(24)] for d in range(31)]
# 
# 
# 
# # =============================================================================
# # #To determine the monthly average noon temperature. 
# # total = 0.0
# # 
# # for day in temps:
# #     total += day[11]
# #     
# # average = total / 31
# # print("Average temperature at noon: ", average)
# # =============================================================================
# 
# # =============================================================================
# # # To find the highest temperature of the whole month
# # 
# # highest = -100
# # 
# # for day in temps:
# #     for temp in day:
# #         if temp > highest:
# #             highest = temp
# # print("The highest temperature was: ", highest)
# # =============================================================================
# 
# #To count the days when the temperature at noon was at least 20oC
# 
# hotDays = 0
# 
# for day in temps:
#     if day[11] > 20.0:
#         hotDays += 1
#         
# print(hotDays, "days were hot")
# =============================================================================

# =============================================================================
# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# rooms[1][9][13] = True # booking room for newlywed couple in the second building thenth floor room 14
# 
# 
# vacancy = 0
# for roomNumber in range(20):
#     if not rooms[2][14][roomNumber]:
#         vacancy += 1
#         
#         
# =============================================================================

# =============================================================================
# def message():
#     print("Enter a value: ")
#     name = int(input("tell me"))
# print("we start here")
# message()
# print("we end here", message)
# =============================================================================

# =============================================================================
# def message(number):
#     print("Enter a number: ", number)
# 
# message(1)
# =============================================================================

# =============================================================================
# def introduction(firstName, middleName, lastName):
#     print("Your First Name is: ", firstName, '\n Midldle Name is: ', middleName, ' \n Last Name is: ', lastName )
#     
# introduction('Abdulrahman', 'Adewale', 'Isah')
# introduction('Asmau', 'Ajoke', 'Isah')
# =============================================================================

# =============================================================================
# def boringFunction():
#     print("You dummy")
#     return 123
# 
# boringFunction()
# print(boringFunction())
# =============================================================================

# =============================================================================
# def myName(wishes = True):
#     print('i hate you')
#     print('like')
#     print('me')
#     
#     if not wishes:
#         return
#     
#     print('you and me')
# 
# myName()
# =============================================================================

# =============================================================================
# def sumOfList(lst):
#     sum = 0
#     for elem in lst:
#         sum += elem
#         
#     return sum
# print(sumOfList([2, 4, 5, 6]))
# =============================================================================

# =============================================================================
# def strangeListFunction(n):
#     straneList = []
#     
#     for i in range(0, n):
#         straneList.insert(0, i)
#         
#     return straneList
# 
# print(strangeListFunction(5))
#                                             
# =============================================================================

# =============================================================================
# def isYearLeap(year):
#     if year % 2000 == 0 or year % 2016 == 0:
#         return True
#     elif year % 1900 == 0 or year % 1987 == 0:
#         return False
#     
# print(isYearLeap(2000))
#     
#     
# testData = [1900, 2000, 2016, 1987]
# testResults = [False, True, True, False]
# for i in range(len(testData)):
#     yr = testData[i]
#     print(yr, "->", end="")
#     result = isYearLeap(yr)
#     if result == testResults[i]:
#         print("Ok")
#     else:
#         print("Failed")
# =============================================================================

# =============================================================================
# def isYearLeap(year):
#     if year % 2000 == 0 or year % 2016 == 0:
#         return True
#     elif year % 1900 == 0 or year % 1987 == 0:
#         return False
# 
# def daysInMonth(year, month):
#     if year % 1900 == 0 and month == 2:
#         return 28
#     elif year % 2000 == 0 and month == 2:
#         return 29
#     elif year % 2016 == 0 and month == 1:
#         return 31
#     elif year % 1987 == 0 and month == 11:
#         return 30
# print(daysInMonth(1900, 2))
#     
# testYears = [1900, 2000, 2016, 1987]
# testMonths = [2, 2, 1, 11]
# testResults = [28, 29, 31, 30]
# for i in range(len(testYears)):
#     yr = testYears[i]
#     mo = testMonths[i]
#     print(yr, mo, "->", end="")
#     result = daysInMonth(yr, mo)
#     if result == testResults[i]:
#         print("Ok")
#     else:
#         print("Failed")
# =============================================================================

# =============================================================================
# a = 1
# b = 2
# c = 3
# 
# if a == 1 and b == 2 and c == 3:
#     print('make sense')
# else:
#     print('days')
# =============================================================================

# =============================================================================
# def isPrime(num):
#     if num =
# 
#     
# for i in range(1, 20):
#     if isPrime(i + 1):
#         print(i + 1, end=" ")
# print()
# =============================================================================

# =============================================================================
# def myFunction(myList1):
#     print(myList1)
#     del myList1[0]
# 
# myList2 = [2, 3]
# myList3 = [1, 2]
# myFunction(myList2)
# print(myList2)
# myFunction(myList3)
# print(myList3)
# =============================================================================

# =============================================================================
# def myName():
# # =============================================================================
# #     global name
# # =============================================================================
#     name = 'Abdulrahman'
#     print(name)
# 
# name = 'Abdul'
# myName()
# print(name)
# 
# # =============================================================================
# # name ='Asmau'
# # print(myName())
# # print(name)
# # =============================================================================
# 
# =============================================================================

# =============================================================================
# def bm1(weight, height):
#     return weight / height ** 2
# 
# print(bm1(52.5, 1.65))
# =============================================================================


# =============================================================================
# def bm1(weight, height):
#     if height < 1.0 or height > 2.5 or \
#     weight < 20 or weight > 200:
#         return None
#     return weight / height ** 2
# 
# print(bm1(150, 1.65))
# 
# =============================================================================


# =============================================================================
# def ftintom(ft, inch):
#     return ft *0.3048 + inch * 0.0254
# 
# print(ftintom(2, 0))
# =============================================================================


# =============================================================================
# #BMI Calculator
# def ftintom(ft, inch =0.0):
#     return ft * 0.3048 + inch * 0.0254
# 
# def lbstokg(lb):
#     return lb * 0.45359237
# 
# def bm1(weight, height):
#     if height < 1.0 or height > 2.5 or \
#     weight < 20 or weight > 200:
#         return None
#     
#     return weight / height ** 2
# 
# print(bm1(weight = lbstokg(176), height = ftintom(5, 7)))def bm1(weight, height):
#     if height < 1.0 or height > 2.5 or \
#     weight < 20 or weight > 200:
#         return None
#     return weight / height ** 2
# 
# print(bm1(150, 1.65))
# =============================================================================

# =============================================================================
# def isItATriangle(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True
# 
# print(isItATriangle(1, 1, 1))
# print(isItATriangle(1, 1, 3))
# =============================================================================

# =============================================================================
# def isItATriangle(a, b, c):
#     if a + b <= c or b + c <= a or \
#     c + a <= b:
#         return False
#     return True
# print(isItATriangle(1, 1, 1))
# print(isItATriangle(1, 1, 3))
# =============================================================================

# =============================================================================
# def isItATriangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
# 
# print(isItATriangle(1, 1, 1))
# print(isItATriangle(1, 1, 3))
# =============================================================================

# =============================================================================
# def isItATriangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
# 
# a = float(input("Enter the first side's length: "))
# b = float(input("Enter the second side's length: "))
# c = float(input("Enter the third side's length: "))
# 
# if isItATriangle(a, b, c):
#     print("Congratulations - it can be a triangle.")
# else:
#     print("Sorry, it won't be a triangle")
# =============================================================================

# =============================================================================
# def isItATriangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
# 
# def isItRightTriangle(a, b, c):
#     if not isItATriangle(a, b, c):
#         return False
# # =============================================================================
# #     if c > a and c > b :
# #         return c ** 2 == a ** 2 + b ** 2
# # =============================================================================
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2
# print(isItATriangle(5, 3, 4))
# print(isItATriangle(2, 4, 3))
# =============================================================================


# =============================================================================
# def isItATriangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
# 
# def heron(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5
# 
# def fieldOfTriangle(a, b, c):
#     if not isItATriangle(a, b, c):
#         return None
#     return heron(a, b, c)
# 
# print(fieldOfTriangle(1., 1., 2.**.5))
# =============================================================================

# =============================================================================
# m = []
# def factorialFun(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     
#     product = 1
#     for i in range(2, n+1):
#         product *= i
#         m.append(product)
#     return product
# # =============================================================================
# # print(factorialFun(6))
# # print(m)
# # =============================================================================
# 
# for n in range(1, 6):
#     print(n, factorialFun(n))
# =============================================================================

# =============================================================================
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     
#     elem1 = elem2 = 1
#     sum = 0
#     
#     for i in range(3, n+1):
#         sum = elem1 + elem2
#         elem1, elem2 = elem2, sum
#     return sum
# 
# for n in range(1, 10):
#     print(n, "->", fib(n))
# =============================================================================

# =============================================================================
#Testing Fibonnaci
# elem1 = 1
# elem2 = 2
# sum = 0
# for i in range(2, 10):
#     sum = elem1 + elem2
#     elem1, elem2 = elem2, sum
#     print(sum)
# =============================================================================

# =============================================================================
# def fib(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * fib(n - 1)
# 
# for n in range(1, 10):
#     print(n, '->', fib(n))
# =============================================================================


# =============================================================================
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     return fib(n-1) + fib(n -2)
# 
# for n in range(1, 10):
#     print(n, '->', fib(n))
# =============================================================================


# =============================================================================
# class Employee:
#    'Common base class for all employees'
#    empCount = 0
# 
#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
#    
#    def displayCount(self):
#      print ("Total Employee %d" % Employee.empCount)
# 
#    def displayEmployee(self):
#       print ("Name : ", self.name,  ", Salary: ", self.salary)
# 
# emp1 = Employee("Zara", 2000)
# emp2 = Employee("Manni", 5000)
# print ("Employee.__doc__:", Employee.__doc__)
# print ("Employee.__name__:", Employee.__name__)
# print ("Employee.__module__:", Employee.__module__)
# print ("Employee.__bases__:", Employee.__bases__)
# print ("Employee.__dict__:", Employee.__dict__ )
# =============================================================================

# =============================================================================
# import matplotlib.pyplot as plt
# 
# class Circle(object):
#     
#     def _init_(self, radius = 3, color = 'red'):
#         self.radius = radius
#         self.color = color
#         
#         #Method
#         def add_radius(self, r):
#             self.radius += r
#             return(self.radius)
#         
#         #Method
#         def drawCircle(self):
#             plt.gca().add_patch(plt.Circle(0, 0), radius = self.radius, c=self.color)
#             plt.axis('scaled')
#             plt.show()
# =============================================================================
# =============================================================================
#             
# dd = {"1": "0", "0":"1"}
# for x in dd.vals():
#     print(x)
# =============================================================================
# =============================================================================
#     
# def fuc(a, b):
#     return b ** a
# print(func(b=2, 2))
# =============================================================================

# =============================================================================
# x = 1 // 5 + 1 / 5
# print(x)
# 
# dct = {'one': 'two', 'three':'one', 'two':'three'}
# v = dct['three']
# 
# for k in range(len(dct)):
#     v = dct[v]
# print(v)
# =============================================================================

# =============================================================================
# 
# lst = [[x for x in range(3)]for y in range(3)]
# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")
# =============================================================================

# =============================================================================
# tup = (1, 2, 4, 8)
# # =============================================================================
# # tup = tup[-2:-1]
# # =============================================================================
# tup = tup[-1]
# print(tup)
# =============================================================================

# =============================================================================
# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)
# print(fun (0, 3))
# =============================================================================

# =============================================================================
# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2
# 
# print(fun(fun(2)))
# =============================================================================

# =============================================================================
# nums = [1, 2, 3]
# vals = nums
# del vals[:]
# print(vals)
# print(nums)
# =============================================================================

# =============================================================================
# print("a", "b", "c", sep="sep")
# =============================================================================

# =============================================================================
# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else:
#     print("*")
#     
# =============================================================================


# =============================================================================
# tuple1 = (1, 2, 3, 4)
# 
# tuple1[1] = tuple[1] + tuple[3]
# print(tuple[1])
# =============================================================================

# =============================================================================
# lst = [x *x for x in range(5)]
# def fun(lst):
#     del lst[lst[2]]
#     return lst
# print(fun(lst))
# =============================================================================

# =============================================================================
# def fun(inp=2, out=3):
#     return inp * out
# print(fun(out=2))
# =============================================================================

# =============================================================================
# 
# def fun(a):
#     return None
# def fun2(a):
#     return fun(a) * fun2(a)
# print(fun2(2))
# =============================================================================
# =============================================================================
# z = 10
# y = 10
# x = y < z and z > y or y > z and z < y
# print(x)
# =============================================================================

# =============================================================================
# dict = {"cat":"chat", "dog":"chien", "horse": "cheval"}
# =============================================================================

# =============================================================================
# for key in sorted(dict.keys()):
#     print(key, "->", dict[key])
# =============================================================================

# =============================================================================
# for key, values in dict.items():
#     print(key, '->', values)
# =============================================================================

# =============================================================================
# dict['goat'] = 'meat'
# 
# dict.update({'duck':'canard'})
# print(dict)
# =============================================================================

# =============================================================================
# schoolClass = {}
# 
# while True:
#     name = input("Enter the student's name (or type exit to stop): ")
#     if name == 'exit':
#         break
#     
#     score = int(input("Enter the student's score (0-10): "))
#     
#     if name in schoolClass:
#         schoolClass[name] += (score)
#     else:
#         schoolClass[name] = (score)
#         
# for name in sorted(schoolClass.keys()):
#     sum = 0
#     counter = 0
#     for score in schoolClass[name]:
#         sum += score
#         counter += 1
#     print(name, ":", sum / counter)
#     
# =============================================================================

# =============================================================================
# from platform import platform
# 
# print(platform(1))
# =============================================================================
# =============================================================================
# 
# lst = [1]
# print(lst[-1])
# print(lst[0])
# =============================================================================


stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
print(stack)