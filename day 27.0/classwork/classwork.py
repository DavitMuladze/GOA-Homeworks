
# 1) ფუნქცია - ორი რიცხვის ნამრავლი

def multiply(a, b):
    return a * b

print(multiply(5, 3))  # Output: 15


# 2) ფუნქცია - მისალმება სახელით

def greet(name):
    print("Hello, " + name + "!")

greet("Nika")  # Output: Hello, Nika!


# 3) ფუნქცია - სამი რიცხვის ჯამი

def sum_three_numbers(a, b, c):
    return a + b + c

print(sum_three_numbers(2, 4, 6))  # Output: 12


# 4) ფუნქცია - ორი სტრინგის კონკატენაცია (შეერთება)

def concatenate(str1, str2):
    return str1 + str2

print(concatenate("Hello ", "world"))  # Output: Hello world


# 5) replace() მეთოდი replace() ცვლის სტრინგში გარკვეულ ტექსტს სხვა ტექსტით

text = "I love apples"
new_text = text.replace("apples", "oranges")
print(new_text)  # Output: I love oranges

message = "Python is cool"
updated = message.replace("cool", "awesome")
print(updated)  # Output: Python is awesome


# 6) .upper() და .lower() მეთოდები, upper() — ყველა ასოს აქცევს დიდად, lower() — ყველა ასოს აქცევს პატარა ასოდ

word = "hello"
print(word.upper())  # Output: HELLO

name = "luka"
print(name.upper())  # Output: LUKA

greeting = "HELLO"
print(greeting.lower())  # Output: hello

phrase = "PyThOn"
print(phrase.lower())  # Output: python


# 7) find() მეთოდი, find() აბრუნებს იმ სიმბოლოს ინდექსს სტრინგში, თუ იპოვა. თუ ვერ იპოვა - აბრუნებს -1

text = "Welcome to Python"
position = text.find("Python")
print(position)  # Output: 11

another = "Hello world"
print(another.find("o"))  # Output: 4

# 8) capitalize() მეთოდი, capitalize() — პირველი ასო დიდად, დანარჩენი პატარა ასოდ

name = "giorgi"
print(name.capitalize())  # Output: Giorgi

text = "hello world"
print(text.capitalize())  # Output: Hello world


# 9) swapcase() მეთოდი, swapcase() — დიდი ასოებს აქცევს პატარა ასოდ და პირიქით

word = "HeLLo"
print(word.swapcase())  # Output: hEllO

sentence = "PyThOn IS FuN"
print(sentence.swapcase())  # Output: pYtHoN is fUn