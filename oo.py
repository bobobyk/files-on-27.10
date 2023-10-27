dict = {}

while True:
    name = input("Введите имя человека: ")
    age = int(input("Введите возраст человека: "))

    dict[name] = age

    oldest = max(dict, key=dict.get)
    print("Человек с самым большим возрастом: ", oldest)