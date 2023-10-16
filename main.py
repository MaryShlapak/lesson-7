# Завдання 3.

# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.

def range_sum(a, b):
    if a > b:
        return 0
    return a + range_sum(a + 1, b)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter last number: "))

    if a > b:
        print("The first number must be less than the last number")
    else:
        result = range_sum(a, b)
        print(f"Sum of numbers in range from {a} to {b} = ", result)
except ValueError:
    print("Enter numbers only!")