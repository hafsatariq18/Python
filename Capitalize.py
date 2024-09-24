# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.

# alison heck = Alison Heck

# Given a full name, your task is to capitalize the name appropriately.


# Complete the solve function below.
def solve(s):
  final = []
  for word in s.split(' '):  
    final.append(word.capitalize())

  return ' '.join(final) 
if __name__ == '__main__':