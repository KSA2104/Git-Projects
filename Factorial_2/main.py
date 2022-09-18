# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print('Введите число: ')
number = int(input())
n = number
def factorial(n):
      if(n <= 1):
        return 1
      else:
        return(n * factorial(n - 1))
print(f'Факториал числа равен:{factorial(n)}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
