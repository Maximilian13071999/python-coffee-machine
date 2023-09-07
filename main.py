# COFFEE MACHINE PROJECT

coffee_machine = {
    "Water": 1000,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

coin_counts = {
    "рубль": 1,
    "2 рубля": 2,
    "5 рублей": 5,
    "десятка": 10
}

needed_to_coffee = {
    "латте": {
        "Water": 200,
        "Milk": 100,
        "Coffee": 25,
        "Money": 150
    },
    "эспрессо": {
        "Water": 50,
        "Milk": 0,
        "Coffee": 10,
        "Money": 90
    },
    "капучино": {
        "Water": 250,
        "Milk": 50,
        "Coffee": 25,
        "Money": 130
    }
}


def check_user_input():
    return input("Что вы хотите купить? (эспрессо/латте/капучино):”")


def print_report():
    print(f"Воды: {coffee_machine['Water']}ml")
    print(f"Молока: {coffee_machine['Milk']}ml")
    print(f"Кофе: {coffee_machine['Coffee']}g")
    print(f"Денег: {coffee_machine['Money']}р.")


def check_amounts(recept):
    for item in recept:
        if item == "Money":
            continue
        if coffee_machine[item] < recept[item]:
            print(f"Извините, недостаточно {item}.")
            return False
    return True


def check_drinks(drink_name):
    if drink_name in needed_to_coffee:
        if check_amounts(needed_to_coffee[drink_name]):
            return True
        else:
            return False
    else:
        print("Такого вида кофе нет.")
        return False


def safety_coin_input(coin_name):
    while True:
        coin_amount = input(f"Сколько монет номиналом {coin_name} вы хотите положить?")
        if coin_amount.isdigit():
            coin_amount = int(coin_amount)
            if coin_amount < 0:
                print("Не может быть отрицательное число!")
            else:
                return coin_amount
        else:
            print("Вы ввели не число!")

def update_coffee_machine(drink_name):
    drink_info = needed_to_coffee[drink_name]
    for item in drink_info:
        if item == "Money":
            coffee_machine[item] += drink_info[item]
        else:
            coffee_machine[item] -= drink_info[item]

while True:
    user_input = check_user_input()
    if user_input == "off":
        break
    print_report()
    if check_drinks(user_input):
        needed_money = needed_to_coffee[user_input]['Money']
        print(f"С вас {needed_money}р.")
        total_user_money = 0
        for coin in coin_counts:
            total_user_money += safety_coin_input(coin) * coin_counts[coin]
        if total_user_money < needed_money:
            print("У вас не хватает деньги. Заберите сдачу и попробуйте ещё раз.")
        else:
            print(f"Спасибо за покупку кофе в нашей кофе-машине. Заберите вашу сдачу {total_user_money - needed_money}")
            update_coffee_machine(user_input)


print("Coffee machine is disabled.")
