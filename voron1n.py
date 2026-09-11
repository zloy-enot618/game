import time
from colorama import Fore
import random 
from os import system as command
from modules.fsr import find1sas1
from modules.IP import Ip_Probix

def Logo():

    colors = [
        Fore.WHITE,
        Fore.MAGENTA,
        Fore.RED,
        Fore.GREEN,
        Fore.BLUE,
        Fore.YELLOW
    ]
    for char in " ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄     ▄▄▄▄      ▄▄        ▄ ":
        random_color = random.choice(colors)
        print(random_color + char, end='', flush=True)
        time.sleep(0.0001)  #0.00001 #o.
    print('')
    for char1 in " ▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌  ▄█░░░░▌    ▐░░▌      ▐░▌":
        random_color = random.choice(colors)
        print(random_color + char1, end='', flush=True)
        time.sleep(0.0001)

    print('')
    for char12 in "▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌ ▐░░▌▐░░▌    ▐░▌░▌     ▐░▌":
        random_color = random.choice(colors)
        print(random_color + char12, end='', flush=True)
        time.sleep(0.0001)
    print('')
    for char122 in "▐░▌         ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌  ▀▀ ▐░░▌    ▐░▌▐░▌    ▐░▌":
        random_color = random.choice(colors)
        print(random_color + char122, end='', flush=True)
        time.sleep(0.0001)
    print('')
    for char1223 in "▐░▌       ▐░▌   ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌     ▐░░▌    ▐░▌ ▐░▌   ▐░▌":
        random_color = random.choice(colors)
        print(random_color + char1223, end='', flush=True)
        time.sleep(0.0001)
    print('')
    for char333 in "▐░▌     ▐░▌    ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌     ▐░░▌    ▐░▌  ▐░▌  ▐░▌▌":
        random_color = random.choice(colors)
        print(random_color + char333, end='', flush=True)
        time.sleep(0.0001)
    print('')
    for char33 in "▐░▌   ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌     ▐░░▌    ▐░▌   ▐░▌ ▐░▌":
        random_color = random.choice(colors)
        print(random_color + char33, end='', flush=True)
        time.sleep(0.0001)
    print('')
    for char233 in "▐░▌ ▐░▌      ▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌     ▐░░▌    ▐░▌    ▐░▌▐░▌▌":
        random_color = random.choice(colors)
        print(random_color + char233, end='', flush=True)
        time.sleep(0.0001)
    print('')
        #▐░▌ ▐░▌      ▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌     ▐░░▌    ▐░▌    ▐░▌▐░▌
    for char3 in "▐░▐░▌       ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌ ▄▄▄▄█░░█▄▄▄ ▐░▌     ▐░▐░▌":
        random_color = random.choice(colors)
        print(random_color + char3, end='', flush=True)
        time.sleep(0.0001)
    print('')
    for char312 in "▐░▌        ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌":
        random_color = random.choice(colors)
        print(random_color + char312, end='', flush=True)
        time.sleep(0.0001)
    print('')
    for char31212 in "▀          ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀ ":
        random_color = random.choice(colors)
        print(random_color + char31212, end='', flush=True)
        time.sleep(0.0001)
    print('')
    for char31212asd in "                                                                                               ":
            random_color = random.choice(colors)
            print(random_color + char31212asd, end='', flush=True)
            time.sleep(0.0001)
    print('')    
    TheLogic()
def MainVore():
    Logo()




def TheLogic():
    print("┌───────────────────────────┬─────────────────────────┐")
    print("│  1. Пробив по номеру      │ 4. DDoS атака (мощная)  │")
    print("│  2. Пробив инфы по домену │ 5. Снос ТГ(тгк, акк,чат)│")
    print("│  3. Пробив по ФШР айди    │ 6. Пробив по Гос Номеру │")
    print("└───────────────────────────┴─────────────────────────┘")
    print("┌───────────────────────────┬─────────────────────────────────┐")
    print("│  7. Cmd Executor          │ 10. Брутфорс паролей к архивам  │")
    print("│  8. Power Shell Executor  │ 11. Чат с нейросетью            │")
    print("│  9. Сканнер портов        │ 12. СМС Бомбер                  │")
    print("└───────────────────────────┴─────────────────────────────────┘")
    print("┌───────────────────────────────────────────────────────┐")
    print("│  13. Узнать где зарегана почта                        │")
    print("│  14. Узнать где есть такой никнейм                    │")
    print("│  15. Показать все, где может быть зареган этот телефон│")
    print("└───────────────────────────────────────────────────────┘")
    print("┌───────────────────────────────────────────────────────┐")
    print("│                 16. Пробив по IP                      │")
    print("└───────────────────────────────────────────────────────┘")
    #choice = input("Enter choice: ")
    while True:
        try:
            choice_input = input("Выберите пункт меню (1-16): ").strip()
            if not choice_input:
                print("Ошибка: пустой ввод!")
                continue
            choice = int(choice_input)
            if 1 <= choice <= 16:
                Pereopr(choice)
                break
                
            else:
                print("Ошибка: число должно быть от 1 до 16!")
        except ValueError:
            print("Ошибка: введите целое число!")

    

def Pereopr(choice):
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        command("cls")
        find1sas1()
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        pass
    elif choice == 9:
        pass
    elif choice == 10:
        pass
    elif choice == 11:
        pass
    elif choice == 12:
        pass
    elif choice == 13:
        pass
    elif choice == 14:
        pass
    elif choice == 15:
        pass
    elif choice == 16:
        command("cls")
        Ip_Probix()






if __name__ == "__main__":
    MainVore()