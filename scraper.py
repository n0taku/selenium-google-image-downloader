from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime

import requests
import os


class Scraper:
    def __init__(self, path):
        self.driver = webdriver.Chrome(path)

    def quit(self):
        self.driver.quit()

    def search(self, query):
        self.driver.get(
            f"https://www.google.com/search?q={query}&source=lnms&tbm=isch&tbs=isz:m")

    def getImageList(self, query, size=10, download=False):
        self.search(query)
        img_list = []
        idx = 0
        e = self.driver.find_elements(By.CSS_SELECTOR, "#islrg .Q4LuWd")[idx]
        while len(img_list) < size:
            e = self.driver.find_elements(
                By.CSS_SELECTOR, "#islrg .Q4LuWd")[idx]
            idx += 1
            try:
                e.click()

                alt = e.get_attribute('alt')
                src = e.get_attribute('src')

                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, f".n3VNCb[alt='{alt}'][src^='http']:not([src='{src}']")))

                img = self.driver.find_element(
                    By.CSS_SELECTOR, f".n3VNCb[alt='{alt}'][src^='http']").get_attribute('src')
                img_list.append(img)

                if download == True:
                    os.makedirs(query, exist_ok=True)
                    date = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
                    with open(f"./{query}/{date}.jpg", "wb") as f:
                        r = requests.get(img)
                        f.write(r.content)
            except Exception as ex:
                print(ex)
                continue
        return img_list
