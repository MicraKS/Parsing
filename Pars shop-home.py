import requests
from bs4 import BeautifulSoup
import json
import csv

def get_data(url):
    # headers = {
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    # }
    # requestss = requests.get(url, headers)
    # print(requestss.text)
    # with open("test.html", "w", encoding='utf-8') as file:
    #     file.write(requestss.text)

    with open("test.html", encoding='utf-8') as file:
        scr = file.read()

    home = []
    title = []
    link = []
    vendor_code = []
    square = []
    price = []

    soup = BeautifulSoup(scr, "lxml")
    src = soup.find_all("a", class_="element")

    for item in src:
        link.append("https://www.shop-project.ru" + item.get("href"))
        title.append(item.get("title"))

    vendor_code_pars = soup.find_all("span", class_="default-color")

    for item in vendor_code_pars:
        vendor_code.append(item.text)

    square_pars = soup.find_all("span", class_="color-white")
    # sup = soup.find("span", class_="color-white").find("sup").text
    # print(sup)

    for item in square_pars:
        square.append(item.text)

    # print(square)
    price_pars = soup.find_all("span", class_="default-color-2")
    for item in price_pars:
        price.append(item.text)

    for i in range(len(title)):
        home.append(
                    {
                        "Title": title[i],
                        "link": link[i],
                        "data": vendor_code[i],
                        "square": square[i],
                        "price": price[i],
                    }
                )
    print(home)



get_data("https://www.shop-project.ru/")
