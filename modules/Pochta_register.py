import trio
import httpx

# Импортируем модули сайтов
from holehe.modules.social_media.snapchat import snapchat
from holehe.modules.social_media.twitter import twitter
from holehe.modules.social_media.instagram import instagram


async def scan():
    email = input("Введите Email для проверки: ").strip()
    if not email or "@" not in email:
        print("Ошибка: неверный формат почты!")
        return

    print(f"\n[+] Запуск проверки через библиотеку Holehe для: {email}...\n")

    out = []
    
    async with httpx.AsyncClient() as client:
        # Список функций-модулей, которые мы хотим запустить
        modules_to_run = [snapchat, twitter, instagram]
        
        for module in modules_to_run:
            try:
                # Безопасно запускаем каждый модуль по очереди
                await module(email, client, out)
            except Exception:
                # Если сайт выдал ошибку (как Snapchat), мы её тихо игнорируем
                print(f"  [!] Ошибка проверки модуля: {module.__name__} (сайт изменил верстку)")
                continue

    print("\n" + "=" * 50)
    print(" РЕЗУЛЬТАТЫ ПРОВЕРКИ:")
    print("=" * 50)

    if not out:
        print("  [-] Аккаунты на выбранных сайтах не найдены.")
    else:
        for result in out:
            if result.get("exists"):
                print(f"  [+] Найден аккаунт: {result.get('name')}")

    print("=" * 50)


def start_holehe():
    trio.run(scan)


if __name__ == "__main__":
    start_holehe()
