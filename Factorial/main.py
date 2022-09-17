# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print('Введите число: ')
number = int(input())
n = number
def factorial(n):
	res = 1
	for i in range(1, n+1):
		res *= i
	return res

print(f'Результат равен: {factorial(n)}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
