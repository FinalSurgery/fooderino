from bs4 import BeautifulSoup
from variable import *
import requests
# import re

ingredient = ["mustard"]

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
    # page_request = requests.get(f"{url}/collections/meals?&page={n}")
    # page_soup = BeautifulSoup(page_request.content, "html.parser")
    # page_validation = page_soup.find("p", class_="quote")
    # print(page_validation)
    n = 1
    run = True
    while run == True: 
        request = requests.get(f"{url}/collections/meals?&page={n}")
        soup = BeautifulSoup(request.content, "html.parser")
        findProduct = soup.findAll("div", class_="info")
        page_validation = soup.find("p", class_="quote")
        if page_validation == None:
            for i in findProduct:
                undersoup = BeautifulSoup(str(i), "html.parser")
                underfinder = undersoup.find("a")
                product_name = underfinder["href"]
                final_request = formulate_request(url, product_name)
                check_for_ingredient(final_request, product_name)
        else:
            run == False
            break
        n += 1
        continue

if __name__ == "__main__":
    main(url) 
