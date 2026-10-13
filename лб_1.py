#Завдання 1

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print("1. Початковий список:", numbers)

print("Елемент з індексом 2:", numbers[2])
print("Елемент з індексом -1:", numbers[-1])

print("Зріз від 1 до 4:", numbers[1:4])
print("Зріз від початку до 5:", numbers[:5])
print("Кожен другий елемент:", numbers[::2])
print("Зріз у зворотному порядку:", numbers[::-1])

numbers.append(90)
print("Після додавання 90:", numbers)

numbers.insert(2, 25)
print("Після вставлення 25:", numbers)

numbers.remove(50)
print("Після видалення 50:", numbers)

print("Кількість елементів:", len(numbers))
print("Фінальний список:", numbers)


#Завдання 2

products = [
    (1, "Миша", 3, 450.0),
    (2, "Клавіатура", 2, 850.0),
    (3, "Навушники", 4, 600.0)
]

def show_product(product):
    product_id, name, quantity, price = product
    print(
        f"ID: {product_id}, назва: {name}, "
        f"кількість: {quantity}, ціна: {price:.2f} грн"
    )

def calculate_total(items):
    return sum(quantity * price
               for _, _, quantity, price in items)

print("2. Перелік товарів:")
for product in products:
    show_product(product)

total = calculate_total(products)
print(f"Загальна вартість: {total:.2f} грн")

try:
    products[0][1] = "Ігрова миша"
except TypeError as error:
    print("Помилка зміни кортежу:", error)

student = ("Іваненко", [85, 90, 95])
print("Початковий запис студента:", student)

student[1].append(100)
print("Після додавання оцінки:", student)


#Завдання 3

text = """Python зручний для програмування. Python допомагає вивчати програмування!"""

normalized_text = text.lower()

for symbol in ".,!?;:":
    normalized_text = normalized_text.replace(symbol, " ")

words = normalized_text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("3. Частоти слів за алфавітом:")
for word in sorted(frequency):
    print(f"{word}: {frequency[word]}")

print("Частота слова 'алгоритм':",
      frequency.get("алгоритм", 0))

sorted_frequency = sorted(
    frequency.items(),
    key=lambda item: (-item[1], item[0])
)

print("\nСлова за спаданням частоти:")
for word, count in sorted_frequency:
    print(f"{word}: {count}")

threshold = 2
common_words = {
    word: count
    for word, count in frequency.items()
    if count >= threshold
}

print("\nСлова з частотою не менше 2:", common_words)


#Завдання 4

data_a = [101, 102, 103, 103, 104, 105]
data_b = [103, 104, 104, 105, 106, 107]
data_c = [101, 102]

set_a = set(data_a)
set_b = set(data_b)
set_c = set(data_c)

print("4. Початкова колекція A:", data_a)
print("Унікальні значення A:", sorted(set_a))

print("Початкова колекція B:", data_b)
print("Унікальні значення B:", sorted(set_b))

print("Перетин A і B:", sorted(set_a & set_b))
print("Об'єднання A і B:", sorted(set_a | set_b))
print("Симетрична різниця A і B:",
      sorted(set_a ^ set_b))

print("Чи є C підмножиною A?", set_c <= set_a)
print("Чи є B підмножиною A?", set_b <= set_a)

group_names = {
    frozenset({101, 102}): "Перша група",
    frozenset({103, 104}): "Друга група"
}

print("Назва групи:", group_names[frozenset({101, 102})])


#Завдання 5

import timeit

sizes = [100, 1000, 5000]
repeats = 3

print("5. Результати вимірювання часу")
print("Усі значення часу наведено в мілісекундах.")
print()

header = (
    f"{'n':>6} | {'Пошук у списку':>16} | "
    f"{'Пошук у set':>12} | {'Пошук у dict':>13} | "
    f"{'Унікальні: list':>16} | {'Унікальні: set':>15}"
)
print(header)
print("-" * len(header))


def average_time(function):
    measurements = timeit.repeat(
        function,
        number=1,
        repeat=repeats
    )
    return sum(measurements) / repeats


for n in sizes:
    data = list(range(n))
    data_set = set(data)
    data_dict = {value: True for value in data}

    target = n - 1

    list_search = average_time(
        lambda: target in data
    )
    set_search = average_time(
        lambda: target in data_set
    )
    dict_search = average_time(
        lambda: target in data_dict
    )

    def unique_list():
        result = []
        for value in data:
            if value not in result:
                result.append(value)
        return result

    def unique_set():
        result = set()
        for value in data:
            result.add(value)
        return result

    list_build = average_time(unique_list)
    set_build = average_time(unique_set)

    values = [
        list_search * 1000,
        set_search * 1000,
        dict_search * 1000,
        list_build * 1000,
        set_build * 1000
    ]

    print(
        f"{n:6} | "
        + " | ".join(f"{value:16.4f}" for value in values)
    )
