import requests
from bs4 import BeautifulSoup


def Ip_Probix():
    ip = input("Введите IP для пробива (или Enter для своего IP): ").strip()
    
    # Формируем ссылку по вашему формату
    url = f"https://infobyip.com/ip-{ip}.html" if ip else "https://infobyip.com"
    
    print(f"\n[+] Сбор АБСОЛЮТНО ВСЕЙ информации с InfoByIp для: {ip if ip else 'Ваш IP'}...")
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"[-] Ошибка: Не удалось загрузить страницу (Код: {response.status_code})")
            return
            
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Находим абсолютно все таблицы на странице
        tables = soup.find_all("table")
        
        if not tables:
            print("[-] Данные не найдены.")
            return

        for table in tables:
            # Ищем заголовок таблицы (в th)
            th = table.find("th")
            if th:
                header_text = " ".join(th.text.split()).upper()
                print(f"\n{"=" * 15} {header_text} {"=" * 15}")
            else:
                # Если у таблицы нет th, но это таблица с данными, разделяем их визуально
                print(f"\n{"-" * 45}")
            
            # Перебираем строки таблицы
            for row in table.find_all("tr"):
                # Пропускаем строку, если она сама является заголовком th
                if row.find("th"):
                    continue
                    
                cells = row.find_all("td")
                if len(cells) == 2:
                    key = " ".join(cells[0].text.split())
                    value = " ".join(cells[1].text.split())
                    
                    # Игнорируем пустые или рекламные строки
                    if not key and not value:
                        continue
                        
                    print(f"  • {key}: {value}")
                    
        print(f"\n{"=" * 50}\n[+] Парсинг успешно завершен!")

    except requests.exceptions.RequestException as e:
        print(f"[-] Ошибка сети: {e}")
    except Exception as e:
        print(f"[-] Произошла ошибка при разборе страницы: {e}")
