# EN
**GenASNRangeScraper** is a Python tool designed to extract CIDR ranges from a given Autonomous System Number (ASN). This tool is essential for network administrators, cybersecurity professionals, and researchers who need to gather and analyze IP range information associated with specific ASNs.

## Features
- **Efficient CIDR Extraction**: Quickly retrieves CIDR ranges from ASN.
- **Customizable Output**: Results are saved in a text file named after the ASN for easy reference.
- **Cache System**: Caches previous results to improve efficiency on subsequent runs.
- **User-Friendly Interface**: Simple command-line interface with clear instructions and error handling.

## Installation
1. **Clone the repository**:
```bash
git clone https://github.com/geniuszlyy/GenASNRangeScraper.git
cd GenASNRangeScraper
```
2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Usage
To use GenASNRangeScraper, run the script with the ASN as an argument:
```bash
python GenASNRangeScraper.py [ASN]
```

![image](https://github.com/user-attachments/assets/134763c9-1815-42fe-b675-c1a4c5f7735b)



## Example
```bash
python GenASNRangeScraper.py AS12345
```
The output will be saved in a file named `AS12345.txt`.

![image](https://github.com/user-attachments/assets/6157e742-044c-41f3-9d5a-faebb2536060)


## Error Handling
If the ASN argument is not provided, the tool will display an error message along with usage instructions.

# RU
**GenASNRangeScraper** - это инструмент на Python, предназначенный для извлечения диапазонов CIDR из заданного автономного системного номера (ASN). Этот инструмент необходим для сетевых администраторов, специалистов по кибербезопасности и исследователей, которым необходимо собирать и анализировать информацию о диапазонах IP, связанных с конкретными ASN.

## Особенности
- **Эффективное извлечение CIDR**: Быстро извлекает диапазоны CIDR из ASN.
- **Настраиваемый вывод**: Результаты сохраняются в текстовом файле с именем ASN для удобства.
- **Система кэширования**: Кэширует предыдущие результаты для повышения эффективности при последующих запусках.
- **Удобный интерфейс**: Простой интерфейс командной строки с четкими инструкциями и обработкой ошибок.

## Установка
1. **Клонируйте репозиторий**:
```bash
git clone https://github.com/geniuszlyy/GenASNRangeScraper.git
cd GenASNRangeScraper
```
2. **Установите зависимости**:
```bash
pip install -r requirements.txt
```

## Использование
Для использования GenASNRangeScraper запустите скрипт с указанием ASN в качестве аргумента:
```bash
python GenASNRangeScraper.py [ASN]
```

![image](https://github.com/user-attachments/assets/0125fd25-ea7d-4469-89df-e693e4b95d45)


## Пример
```bash
python GenASNRangeScraper.py AS12345
```
Результаты будут сохранены в файле с именем `AS12345.txt`.

![image](https://github.com/user-attachments/assets/8b237bb3-10a0-4dd0-91c4-fe75eb69404a)


## Обработка ошибок
Если аргумент ASN не указан, инструмент отобразит сообщение об ошибке с инструкциями по использованию.
