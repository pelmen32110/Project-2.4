'''
Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
Пункты задачи:
Создайте пустые списки primes и not_primes.
При помощи цикла for переберите список numbers.
Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
Выведите списки primes и not_primes на экран(в консоль).
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

def prime_numbers(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for number in numbers:
    if prime_numbers(number):
        primes.append(number)
    else:
        not_primes.append(number)

print('Простые числа: ', primes)
print('Не простые числа: ', not_primes)