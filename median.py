"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        median_position = ((len(numbers) + 1) / 2 ) - 1
        lower_value = numbers[math.floor(median_position)]
        upper_value = numbers[math.ceil(median_position)]
        median = (lower_value + upper_value) / 2
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
