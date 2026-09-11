def find1sas1():


    import requests
    import time
    import sys
    from bs4 import BeautifulSoup
    from colorama import init, Fore, Style


    import os

    init(autoreset=True)

    # --- ТВОИ ОРИГИНАЛЬНЫЕ ФУНКЦИИ (БЕЗ ИЗМЕНЕНИЙ) ---





    def loading_animation(duration=1.0, text="Обработка"):
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for _ in range(int(duration * 10)):
            for char in chars:
                sys.stdout.write(f'\r{Fore.MAGENTA} {text} {char} ')
                sys.stdout.flush()
                time.sleep(0.01)
        sys.stdout.write('\r' + ' ' * 40 + '\r')


    def check_fshr():
        print(f"\n{Fore.WHITE}Введите ID ФШР:")
        fshr_id = input(f"{Fore.CYAN}>>> {Fore.YELLOW}").strip()
        
        url = f"https://ratings.ruchess.ru/people/{fshr_id}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

        loading_animation(text="Парсинг ФШР")

        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                player_name = soup.find('h1').get_text(strip=True) if soup.find('h1') else "Неизвестно"
                
                print(f"{Fore.GREEN}[FSHR SUCCESS]{Fore.WHITE} Игрок: {player_name}")
                print(f"{Fore.CYAN}{'━'*50}")

                items = soup.find_all('li', class_='list-group-item')
                for item in items:
                    text = item.get_text(" ", strip=True)
                    if "ФШР ID" in text:
                        print(f"{Fore.YELLOW}{'ФШР ID':<12} {Fore.WHITE}│ {Fore.CYAN}{text.split(':')[-1].strip()}")
                    elif "Пол" in text:
                        print(f"{Fore.YELLOW}{'Пол':<12} {Fore.WHITE}│ {Fore.WHITE}{text.split(':')[-1].strip()}")
                    elif "Регион" in text:
                        reg = text.split(':')[-1].replace('\n', ' ').strip()
                        print(f"{Fore.YELLOW}{'Регион':<12} {Fore.WHITE}│ {Fore.WHITE}{reg}")
                    elif "Год рождения" in text:
                        print(f"{Fore.YELLOW}{'Год рожд.':<12} {Fore.WHITE}│ {Fore.WHITE}{text.split(':')[-1].strip()}")
            else:
                print(f"{Fore.RED}[!] Ошибка: ID не найден.")
        except Exception as e:
            print(f"{Fore.RED}[!] Ошибка соединения: {e}")
    check_fshr()
