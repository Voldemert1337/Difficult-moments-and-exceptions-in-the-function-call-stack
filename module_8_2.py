def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        if isinstance(numbers, (int, float)):
            print('В numbers записан некорректный тип данных')
            return None
        elif not numbers:
            return 0
        else:
            result, incorrect_data = personal_sum(numbers)
            return result / len(numbers)
    except Exception as e:
        print(f"Произошла ошибкач: {e}")
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')