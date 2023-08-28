#!/usr/bin/python3
# 9-print_last_digit.py

def print_last_digit(number):
    """Print last digit of a number and return it"""
    absolute = abs(number)
    print(absolute % 10, end="")
    return (absolute % 10)
