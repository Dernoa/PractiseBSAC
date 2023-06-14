def find_24_expression(digits):
    if len(digits) != 4 or not digits.isdigit():
        return "Некорректный ввод. Введите строку из 4 цифр."

    numbers = [int(digit) for digit in digits]

    permutations = get_permutations(numbers)

    for permutation in permutations:
        operators = ["+", "-", "*", "/"]
        combinations = get_operator_combinations(operators, 3)

        for combination in combinations:
            expression = generate_expression(permutation, combination)
            result = evaluate_expression(expression)
            if result == 24:
                return expression

    return "Нет решения."

def get_permutations(numbers):
    from itertools import permutations
    return permutations(numbers)

def get_operator_combinations(operators, length):
    from itertools import product
    return product(operators, repeat=length)

def generate_expression(numbers, operators):
    expression = ""
    for i in range(3):
        expression += str(numbers[i]) + operators[i]
    expression += str(numbers[3])
    return expression

def evaluate_expression(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return None

digits = input("Введите 4 цифры (от 1 до 9): ")
expression = find_24_expression(digits)
print(expression)
