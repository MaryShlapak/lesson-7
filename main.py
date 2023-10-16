# Завдання 2.

# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)

def draw_stars(user_input):
    if user_input > 0:
        print("*", end=" ")
        draw_stars(user_input - 1)

try:
    user_input = int(input("Enter stars number: "))
    if user_input <= 0:
        print("Enter positive number")
    else:
        draw_stars(user_input)
except ValueError:
    print("Enter numbers only")
