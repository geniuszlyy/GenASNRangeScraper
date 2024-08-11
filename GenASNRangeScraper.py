import sys
import requests
import re
import argparse
import os
import json
from typing import List
from colorama import Fore, init

# Инициализация colorama
init(autoreset=True)

# Регулярное выражение для поиска CIDR
CIDR_REGEX = r'>([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2})<'
# URL-адрес для получения информации по ASN
INFO_URL = "https://ipinfo.io/%s"
# Пользовательский агент для HTTP-запроса
HTTP_USER_AGENT = "Mozilla/4.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
# Файл для кэширования данных
CACHE_FILE = "cidr_cache.json"

# Переопределяет метод error для кастомного вывода сообщений
class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX} GenASNRangeScraper {Fore.LIGHTYELLOW_EX}]{Fore.LIGHTBLUE_EX} » {Fore.LIGHTYELLOW_EX}Ошибка. Вы не ввели ASN диапазон.\n")
        sys.exit(2)

# Извлекает список CIDR из ASN
def extract_cidr_list(asn: str) -> List[str]: # asn (str) - ASN для парсинга. | List[str] - Список строк, содержащих CIDR
    response = requests.get(url=INFO_URL % asn, headers={"User-Agent": HTTP_USER_AGENT})
    if response.status_code != 200:
        raise ValueError(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenASNRangeScraper {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Ошибка при запросе к серверу: {Fore.LIGHTRED_EX}{response.status_code}")
    cidr_set = set(re.findall(pattern=CIDR_REGEX, string=response.text))
    return list(cidr_set)

# Загружает кэш из файла
def load_cache() -> dict:
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as file:
            return json.load(file)
    return {}

# Сохраняет кэш в файл
def save_cache(cache: dict):
    with open(CACHE_FILE, "w") as file:
        json.dump(cache, file)

# Отображает логотип и информацию
def display_logo_and_usage():
    logo = f"""{Fore.LIGHTRED_EX}

   _____                      _____ _   _ _____                         _____                                
  / ____|              /\    / ____| \ | |  __ \                       / ____|                               
 | |  __  ___ _ __    /  \  | (___ |  \| | |__) |__ _ _ __   __ _  ___| (___   ___ _ __ __ _ _ __   ___ _ __ 
 | | |_ |/ _ \ '_ \  / /\ \  \___ \| . ` |  _  // _` | '_ \ / _` |/ _ \\\\___ \ / __| '__/ _` | '_ \ / _ \ '__|
 | |__| |  __/ | | |/ ____ \ ____) | |\  | | \ \ (_| | | | | (_| |  __/____) | (__| | | (_| | |_) |  __/ |   
  \_____|\___|_| |_/_/    \_\_____/|_| \_|_|  \_\__,_|_| |_|\__, |\___|_____/ \___|_|  \__,_| .__/ \___|_|   
                                                             __/ |                          | |              
                                                            |___/                           |_|              
    """
    print(logo)
    print(f"""
{Fore.LIGHTYELLOW_EX}╭────────────────────────━━━━━━━━━━━━━━━━━━━━━──────────────────────╮
{Fore.LIGHTGREEN_EX}|         GenASNRangeScraper - Получение списков CIDR из ASN        {Fore.LIGHTYELLOW_EX}|
|───────────────────────────────────────────────────────────────────|
{Fore.LIGHTGREEN_EX}| Использование: python {os.path.basename(__file__)} [ASN]                 {Fore.LIGHTYELLOW_EX}|
{Fore.LIGHTGREEN_EX}| Пример: python {os.path.basename(__file__)} AS12345                      {Fore.LIGHTYELLOW_EX}|
{Fore.LIGHTGREEN_EX}| Описание: Эта программа извлекает список CIDR из заданного ASN.   {Fore.LIGHTYELLOW_EX}|
{Fore.LIGHTYELLOW_EX}╰────────────────────────━━━━━━━━━━━━━━━━━━━━━──────────────────────╯
""")

def main():
    display_logo_and_usage()
    # Парсинг аргументов командной строки
    parser = CustomArgumentParser(description="Сбор списка CIDR по одному ASN.")
    parser.add_argument("asn", help="ASN для парсинга")
    args = parser.parse_args()

    cache = load_cache()

    if args.asn in cache:
        cidr_list = cache[args.asn]
    else:
        try:
            cidr_list = extract_cidr_list(args.asn)
            cache[args.asn] = cidr_list
            save_cache(cache)
        except Exception as e:
            print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenASNRangeScraper {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Произошла ошибка:  {Fore.LIGHTRED_EX}{e}", file=sys.stderr)
            sys.exit(1)

    # Определяем имя файла для сохранения результатов
    output_file = f"{args.asn}.txt"
    with open(output_file, "w") as f:
        f.write('\n'.join(cidr_list))
    print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenASNRangeScraper {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Результаты сохранены в файл: {Fore.LIGHTGREEN_EX}{output_file}")

if __name__ == "__main__":
    main()
