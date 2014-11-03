__author__ = 'Claudio'



""" Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""
def get_odd_numbers(data):
    return [k for k in data if (k & 1 == 1)]
