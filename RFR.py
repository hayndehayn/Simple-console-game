import random
import time
import tabulate

money = 500
regiments = []

# TODO: Переробити механіку та додати аби рекрутів можна було наймати в селах, які випадковим чином будуть траплятися
def recruitMen():
    men_power = 1000
    recruited = 0
    while True:
        try:
            recruit_men = int(input("How many men do you want to recruit? "))
            break
        except:
            print("Invalid input. Please enter a valid integer.")
    if recruit_men > men_power:
        print("You don't have enough menpower.")
        return 0
    
    # * Menpower change
    men_power -= recruit_men
    recruited = recruit_men

    # * Print the results
    print("You recruited " + str(recruited) + " men.")
    print("You have " + str(men_power) + " menpower remaining.")

# TODO: Переробити систему, аби вона залежала від значення змінної menpower
def formRegiments():
    global regiments
    regiment_name = input("\n Name your regiment: ")
    regiment = {"name": regiment_name, "soldiers": []}
    regiments.append(regiment)
    print(tabulate.tabulate(regiments))
    print("Regiment " + regiment_name + " has been created.")

def manageRegiments():
    print(tabulate.tabulate(regiments))
    # TODO: Проробити функціонал покращення полків
    # TODO: Забезпечення нових рекрутів
    # TODO: Покращення спорядження
    # TODO: Механіка тренувань

def menu():
    print("\nWelcome.")
    # * Statistics
    print("Your money is " + str(money))
    print("You have next regiments: ")
    print(tabulate.tabulate(regiments))
    # TODO: Доробити відображення інших аргументів
    
    # * Menu
    print("1. Recruit men")
    print("2. Form a regiment")
    print("3. Manage regiments")
    print("4. Exit")
    choice = input("Answer: ")
    menu_choice = choice

    if menu_choice == "1":
        recruitMen()
    elif menu_choice == "2":
        formRegiments()
    elif menu_choice == "3":
        manageRegiments()
    elif menu_choice == "4":
        pass

while True:
    menu()
