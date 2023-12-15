def sum_of_numbers(*args):
    total_sum = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total_sum += arg
    return total_sum


print(sum_of_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_of_numbers())


def recursive_sum(data_list):
    if not data_list:
        return 0, 0, 0

    current_number = data_list[0]
    total, even_sum, odd_sum = recursive_sum(data_list[1:])

    if isinstance(current_number, int):
        total += current_number
        if current_number % 2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number

    return total, even_sum, odd_sum

numbers_list = [1, 2, 3, 4, 5]
total_sum, even_sum, odd_sum = recursive_sum(numbers_list)
print("Total sum:", total_sum)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)


def read_and_return_number():
    user_input = input("Introduceți un număr întreg: ")
    try:
        return int(user_input)
    except ValueError:
        return 0


# Exemplu de utilizare:
result = read_and_return_number()
print("Valoarea introdusă sau 0 dacă nu este un număr întreg:", result)
