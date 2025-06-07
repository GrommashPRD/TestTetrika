import requests
import csv
import time
from bs4 import BeautifulSoup


def scrape_wikipedia_animal_counts():

    current_url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

    base_url = "https://ru.wikipedia.org"

    letter_counts = {}

    russian_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    while True:
        print(f"Обрабатываю : {current_url}")

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(current_url, headers=headers, timeout=10)

            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print("Ошибка при запросе страницы")
            break

        soup = BeautifulSoup(response.text, 'lxml')
        content_block = soup.find('div', id='mw-pages')

        if not content_block:
            print("Нет блока div")
            break

        animal_items = content_block.find_all('li')

        for item in animal_items:
            title = item.get_text().strip()

            if title:
                first_letter = title[0].upper()

                if first_letter in russian_alphabet:
                    letter_counts[first_letter] = letter_counts.get(first_letter, 0) + 1

        next_page_link = soup.find('a', string='Следующая страница')

        if next_page_link:
            current_url = base_url + next_page_link['href']
            time.sleep(0.5)
        else:
            print("Последняя страница.")
            break

    print("\nСбор данных завершен.")

    sorted_counts = sorted(letter_counts.items())

    output_filename = 'beasts.csv'
    try:
        with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            writer.writerows(sorted_counts)

    except IOError as e:
        print("Ошибка при записи файла")

if __name__ == "__main__":
    scrape_wikipedia_animal_counts()