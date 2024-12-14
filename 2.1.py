# coding=utf-8
# example/guess_number.py
import random

Rnd = random.randint(0, 9)  # Генерируем случайное число от 0 до 9
num = int(input("A random number has been generated! Guess it! "))
Attempts = 0

while Rnd != num:
    Attempts += 1
    if num > Rnd:
        print("Wrong! The hidden number is less")
    elif num < Rnd:
        print("Wrong! The hidden number is bigger")
    num = int(input("Try again: "))

print(f"You guessed the number in { Attempts} attempts!")