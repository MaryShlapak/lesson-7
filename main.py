# Завдання 1.

# Написати рекурсивну функцію знаходження ступеня числа.

user_number = float(input("Enter your number: "))
user_pow_num = int(input("Enter the power of number: "))
def power(user_number, user_pow_num):
    if not isinstance(user_number, (int, float)):
        raise ValueError("Enter numbers only")
    if not isinstance(user_pow_num, int):
        raise ValueError("Enter integer only")
    if user_pow_num == 0:
        return 1
    if user_number < 0:
        return 1 / (user_number * power(user_number, -user_pow_num - 1))
    return user_number * power(user_number, user_pow_num - 1)
result = power(user_number, user_pow_num)
print(f"The power of {user_number} = ", result)