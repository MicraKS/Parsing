from bs4 import BeautifulSoup
import csv
import requests


def get_data(url):
    # Парсим данные
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    requestss = requests.get(url, headers)
    print(requestss.text)
    with open("test.html", "wb") as file:
        file.write(requestss.content)


    #  Сохраняем в файл
    with open("test.html") as file:
        scr = file.read()

    # Создаем табличку с заголовками
    with open(f"venv/Дома.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "Title",
                "Link",
                "Square",
                "Price",
                "Vendor_code"
            )
        )

    soup = BeautifulSoup(scr, "lxml")
    src = soup.find_all("a", class_="element")

    # Проходим куску кода для поиска нужной информации
    for item in src:
        link = "https://www.shop-project.ru" + item.get("href")

        title = item.get("title")

        square = item.find("td", class_="element-square").text

        price = item.find("span", class_="default-color-2").text

        vendor_code = item.find("span", class_="default-color").text

        # Записываем информацию в табличку с заголовками
        with open(f"venv/Дома.csv", "a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title[(str(title).find(".")) + 2:].strip(),
                    link.strip(),
                    square.strip(),
                    price.strip(),
                    vendor_code.strip(),
                )
            )

get_data("https://www.shop-project.ru/")
