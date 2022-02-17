from bs4 import BeautifulSoup
from variable import *
import requests
# import re

ingredient = ["brown rice"]

url = "https://livefitfood.ca"

def formulate_request(url, product_name):
    safe = []
    full_request = requests.get(f"{url}{product_name}")
    full_soup = BeautifulSoup(full_request.content, "html.parser")
    find_nutrition = full_soup.findAll("div", attrs={"class": "accordian-info"})
    for i in find_nutrition:
        validation = i.get_text().strip().replace(" ", "").lower()
    for b in ingredient:
        ing = b.replace(" ", "").lower()
        if ing not in validation:
            safe.append("True")
        else:
            safe.append("False")
    return safe

def check_for_ingredient(boolean, product_name):
    if "False" not in boolean:
        print(product_name.split("/")[4])
    else:
        return ""



def main(url):
    request = requests.get(f"{url}/collections/meals")
    soup = BeautifulSoup(request.content, "html.parser")
    findProduct = soup.findAll("div", class_="info")
    for i in findProduct:
        undersoup = BeautifulSoup(str(i), "html.parser")
        underfinder = undersoup.find("a")
        product_name = underfinder["href"]
        final_request = formulate_request(url, product_name)
        check_for_ingredient(final_request, product_name)

if __name__ == "__main__":
    main(url) 
