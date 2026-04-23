import argparse
import time
import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--pages_count", type=int, default=5)
args = parser.parse_args()
max_pages = args.pages_count

conn = psycopg2.connect(
    dbname="products_db",
    user="postgres",
    password="zdxsdT8.",
    host="localhost",
    port="5432"
)

conn.set_client_encoding('UTF8')
cursor = conn.cursor()

cursor.execute("TRUNCATE TABLE products RESTART IDENTITY;")
conn.commit()

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)


def wait_for_page_load(timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    except:
        pass


def go_to_next_page(current_page):
    methods = [
        lambda: click_pagination_button(),
        lambda: click_load_more_button(),
        lambda: use_direct_url_pagination(current_page),
        lambda: use_infinite_scroll()
    ]

    for method in methods:
        try:
            if method():
                return True
        except:
            continue
    return False


def click_pagination_button():
    selectors = [
        "//a[contains(text(), 'Далее')]",
        "//a[contains(text(), 'Следующая')]",
        "//a[contains(@class, 'next')]",
        "//a[contains(@class, 'pagination-next')]",
        "//link[@rel='next']",
        "//a[contains(@href, 'PAGEN_1=') and not(contains(@href, 'PAGEN_1=1'))]"
    ]

    for selector in selectors:
        try:
            buttons = driver.find_elements(By.XPATH, selector)
            for button in buttons:
                if button.is_displayed() and button.is_enabled():
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                    time.sleep(0.5)
                    try:
                        button.click()
                    except:
                        driver.execute_script("arguments[0].click();", button)
                    wait_for_page_load()
                    return True
        except:
            continue
    return False


def click_load_more_button():
    selectors = [
        "//button[contains(text(), 'Показать еще')]",
        "//button[contains(text(), 'Загрузить еще')]",
        "//a[contains(text(), 'Показать еще')]",
        "//div[contains(@class, 'load-more')]//button",
        "//button[contains(@class, 'show-more')]"
    ]

    for selector in selectors:
        try:
            button = driver.find_element(By.XPATH, selector)
            if button.is_displayed() and button.is_enabled():
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                time.sleep(0.5)
                try:
                    button.click()
                except:
                    driver.execute_script("arguments[0].click();", button)
                wait_for_page_load()
                return True
        except:
            continue
    return False


def use_direct_url_pagination(current_page):
    current_url = driver.current_url
    url_patterns = [
        lambda: current_url.replace(f'PAGEN_1={current_page}', f'PAGEN_1={current_page + 1}'),
        lambda: current_url + ('' if '?' in current_url else '?') + f'&PAGEN_1={current_page + 1}',
        lambda: current_url.rstrip('/') + f'/page{current_page + 1}/',
        lambda: f"{current_url.split('?')[0]}?PAGEN_1={current_page + 1}"
    ]

    for get_next_url in url_patterns:
        try:
            next_url = get_next_url()
            if next_url != current_url:
                driver.get(next_url)
                wait_for_page_load()
                return True
        except:
            continue
    return False


def use_infinite_scroll():
    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_attempts = 0
    while scroll_attempts < 5:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        scroll_attempts += 1
    return scroll_attempts > 0


try:
    driver.get("https://mirm.ru/")
    time.sleep(3)

    guitar_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Гитары")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", guitar_button)
    time.sleep(1)
    guitar_button.click()
    time.sleep(3)

    electroguitar_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "ЭЛЕКТРОГИТАРЫ")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", electroguitar_button)
    time.sleep(1)
    electroguitar_button.click()
    time.sleep(3)

    page = 1
    total_products = 0
    consecutive_failures = 0

    while page <= max_pages:
        print(f"Парсинг страницы {page}...")

        wait_for_page_load()
        time.sleep(2)

        products = driver.find_elements(By.CLASS_NAME, 'showcase-item-3')
        if not products:
            products = driver.find_elements(By.CLASS_NAME, 'showcase-item')

        for product in products:
            try:
                name = product.find_element(By.CLASS_NAME, 'showcase-name-first').text
                price = product.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
                article = product.find_element(By.CSS_SELECTOR, '.product-code .value').text
                availability = product.find_element(By.CLASS_NAME, 'product-status').text
                link = product.find_element(By.CSS_SELECTOR, 'a[itemprop="url"]').get_attribute('href')

                cursor.execute('''
                    INSERT INTO products (name, price, article, availability, link)
                    VALUES (%s, %s, %s, %s, %s)
                ''', (name, price, article, availability, link))
                conn.commit()

                total_products += 1
            except Exception as e:
                continue

        if page < max_pages:
            if go_to_next_page(page):
                page += 1
                consecutive_failures = 0
            else:
                consecutive_failures += 1
                if consecutive_failures >= 3:
                    break
                driver.refresh()
                time.sleep(3)
        else:
            break

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()
    cursor.close()
    conn.close()
    print(f"Парсинг завершен. Добавлено товаров: {total_products}")