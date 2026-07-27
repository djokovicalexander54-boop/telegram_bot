from bs4 import BeautifulSoup
import time
import pandas as pd
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sel = sqlite3.connect(r"C:\Users\karino\Desktop\PROJECTS\file_1\data_base.db")
conn = sel.cursor()
conn.execute('''
        CREATE TABLE IF NOT EXISTS ta (
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        gold_name TEXT,
        name_product TEXT, 
        price TEXT,
        exist TEXT,
        time TEXT DEFAULT (datetime('now', 'localtime'))
        )
    ''')
sel.commit()
b=1
while b==1:
    try:
        Service = Service(ChromeDriverManager().install())
        site = webdriver.Chrome(service=Service)
        b=2
    except Exception as e:
        print("ops!! check your internet, I try agane...")
        time.sleep(2)
print('ok...')
k=1
m=1
while k==1:
    try:
        name_list = ["geram18","geram24","sekee","nim","rob"]
        site.get("https://www.tgju.org/")
        for item in name_list:
            WebDriverWait(site, 100).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='fs-row']"))
            )
            site_html = BeautifulSoup(site.page_source, 'html.parser')
            row = site_html.find('tr', attrs={'data-market-nameslug':f"{item}"}) 
            row_name = row.find('th', class_=False)
            row_price = row.find('td')
            conn.execute(
                    "INSERT INTO ta (gold_name, price) VALUES (?,?)",
                    (row_name.text.strip(), row_price.text.strip())
                )
            sel.commit()
        tab = site_html.find('div', class_="col-12 col-lg-12 col-xl-6 index-tabs-data-col-1")
        tab_new = tab.find('tbody')  
        row0 = tab_new.find_all('tr')
        for item0 in row0:
            name = item0.find('th')
            price = item0.find('td', class_="market-price")
            conn.execute(
                    "INSERT INTO ta (gold_name, price) VALUES (?,?)",
                    (name.text.strip(),price.text.strip())
                )
            sel.commit()
        tab = site_html.find('div', class_="col-12 col-lg-12 col-xl-6")
        tab_new = tab.find('tbody')  
        row0 = tab_new.find_all('tr')
        for item0 in row0:
            name = item0.find('th')
            price = item0.find('td', class_="market-price")
            conn.execute(
                    "INSERT INTO ta (gold_name, price) VALUES (?,?)",   
                    (name.text.strip(),price.text.strip())
                )
            sel.commit()
        tab = site_html.find('div', class_="index-tabs-data crypto-tabs-mobile2")
        tab_new = tab.find('tbody')  
        row0 = tab_new.find_all('tr')
        for item0 in row0:
            name = item0.find('th')
            price = item0.find('td', class_="market-price-irr") 
            conn.execute(
                    "INSERT INTO ta (gold_name, price) VALUES (?,?)",
                    (name.text.strip(),price.text.strip())
                )
            sel.commit()
        time.sleep(60)
    except Exception as e:
        print("ops!! check your internet, I try agane...")
        time.sleep(5)