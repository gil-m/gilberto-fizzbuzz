# -*- coding: utf-8 -*-
def fizzbuzz_calculator(number):
    word = ''
    if not number % 3:
        word += 'Fizz'
    if not number % 5:
        word += 'Buzz'
    print(word or number)
    return word or str(number)
