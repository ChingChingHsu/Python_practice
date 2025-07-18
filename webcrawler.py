"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def main():
    driver = webdriver.Chrome()
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        driver.get(url)
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 't-stripe'))
            WebDriverWait(driver, 10).until(element_present)
        except TimeoutException:
            print(f"Timed out waiting for page {year} to load.")
            continue

        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
        main_table = soup.find('table', class_='t-stripe')
        tbody = main_table.find('tbody')
        rows = tbody.find_all('tr')

        male_total = 0
        female_total = 0
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 5:
                male_num = int(cols[2].text.replace(',', ''))
                female_num = int(cols[4].text.replace(',', ''))
                male_total += male_num
                female_total += female_num

        print(f"Male Number: {male_total}")
        print(f"Female Number: {female_total}")

    driver.quit()

if __name__ == '__main__':
    main()
