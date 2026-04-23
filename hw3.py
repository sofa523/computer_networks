import argparse
import time
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--pages_count", type=int, default=5)
args = parser.parse_args()
max_pages = args.pages_count

csv_filename = "guitars.csv"
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Название', 'Цена (руб)', 'Артикул', 'Наличие', 'Ссылка'])

driver = webdriver.Chrome()
driver.get("https://mirm.ru/")
wait = WebDriverWait(driver, 10)

guitar_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Гитары")))
guitar_button.click()
time.sleep(2)

electroguitar_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "ЭЛЕКТРОГИТАРЫ")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", electroguitar_button)
time.sleep(1)
electroguitar_button.click()
time.sleep(3)

page = 1
while page <= max_pages:
    print(f"Парсинг страницы {page}...")
    products = driver.find_elements(By.CLASS_NAME, 'showcase-item-3')
    with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for product in products:
            try:
                name = product.find_element(By.CLASS_NAME, 'showcase-name-first').text
                price = product.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
                article = product.find_element(By.CSS_SELECTOR, '.product-code .value').text
                availability = product.find_element(By.CLASS_NAME, 'product-status').text
                link = product.find_element(By.CSS_SELECTOR, 'a[itemprop="url"]').get_attribute('href')

                price_clean = price.replace(' ', '') if price else '0'
                price_rub = f"{price_clean} руб"
                writer.writerow([name, price_rub, article, availability, link])
                print(f"Добавлен товар: {name}, {price}, {availability}")
            except Exception as e:
                print("Ошибка при парсинге товара:", e)

    try:
        next_page_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "PAGEN_1=")]'))
        )
        next_page_button.click()
        time.sleep(3)
        page += 1
    except Exception as e:
        print("Ошибка при переходе на следующую страницу или больше страниц нет:", e)
        break

driver.quit()
