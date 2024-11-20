import warnings
warnings.filterwarnings("ignore")

import re

def validate_postal_code(postal_code):
    # Проверка формата почтового индекса (в данном случае, стандартный 5-значный формат)
    pattern = r'^\d{5}$'
    return re.fullmatch(pattern, postal_code) is not None

def find_postal_codes_in_text(text):
    # Паттерн для поиска почтовых индексов в тексте
    pattern = r'\b\d{5}\b'
    return re.findall(pattern, text)

def find_postal_codes_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if content.strip():  # Проверяем, что файл не пуст
                return find_postal_codes_in_text(content)
            else:
                print(f"Файл {file_path} пуст.")
                return []
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []

if __name__ == "__main__":
    while True:
        print("\nВыберите способ ввода данных:")
        print("1. Пользовательский ввод")
        print("2. Ввод адреса файла")
        print("3. Выход")

        try:
            k = int(input())
        except ValueError:
            print("Пожалуйста, введите число от 1 до 3.")
            continue

        if k == 1:
            postal_code_input = input("Введите почтовый индекс для проверки: ").strip()
            if validate_postal_code(postal_code_input):
                print("Почтовый индекс корректный.")
            else:
                print("Почтовый индекс некорректный.")

        elif k == 2:
            file_path = input("Введите путь к файлу для поиска почтовых индексов: ").strip()
            postal_codes_from_file = find_postal_codes_in_file(file_path)
            if postal_codes_from_file: #C:\Users\mehov\PycharmProjects\LAB3\test_file.txt
                print("Почтовые индексы, найденные в файле:", postal_codes_from_file)
            else:
                print("Почтовые индексы не найдены.")

        elif k == 3:
            break
        else:
            print("Пожалуйста, введите корректное число от 1 до 3.")
