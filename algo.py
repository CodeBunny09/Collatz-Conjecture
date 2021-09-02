import matplotlib.pyplot as plt
import pandas as pd

def collatz_con(n):
    result = []
    node = n
    result.append(n)
    while node != 1:
        if node % 2 == 0:
            node = node/2
            result.append(node)
        else:
            node = (node * 3) + 1
            result.append(node)
    return result

number = 2**68
data = collatz_con(number)

while data[-5:] == [16.0, 8.0, 4.0, 2.0, 1.0]:
    print(data)
    number += 1
    data = collatz_con(number)

print(f'The nummber is {number}')

