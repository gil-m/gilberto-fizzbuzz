# -*- coding: utf-8 -*-
import requests


ANSWERS = []
EVEN_COUNT = 0
ODD_COUNT = 0
FIZZ_COUNT = 0
BUZZ_COUNT = 0
FIZZBUZZ_COUNT = 0


def fizzbuzz_calculator(number):
    word = ''
    if not number % 3:
        word += 'Fizz'
    if not number % 5:
        word += 'Buzz'
    print(word or number)
    return word or str(number)


def fizzbuzz_call(number):
    request = requests.get('http://127.0.0.1:8000/' + str(number))
    answer = request.json().get('answer')
    print(answer)
    return answer


for number in range(100):
    answer = fizzbuzz_call(number + 1)
    ANSWERS.append(answer)

    if answer == 'Fizz':
        FIZZ_COUNT += 1
    elif answer == 'Buzz':
        BUZZ_COUNT += 1
    elif answer == 'FizzBuzz':
        FIZZBUZZ_COUNT += 1
    else:
        try:
            parsed = int(answer)
            if parsed % 2 == 0:
                EVEN_COUNT += 1
            else:
                ODD_COUNT += 1
        except:
            print('Bad answer')

print('Números pares:', EVEN_COUNT)
print('Números ímpares:', ODD_COUNT)
print('Fizz:', FIZZ_COUNT)
print('Buzz:', BUZZ_COUNT)
print('FizzBuzz:', FIZZBUZZ_COUNT)
print(' '.join(ANSWERS))
