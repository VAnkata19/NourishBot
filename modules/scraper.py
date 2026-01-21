from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = "https://www.ica.se/erbjudanden/ica-supermarket-aptiten-1003988/"

def grocery_offers():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    wait = WebDriverWait(driver, 4)

    agree_button_selector = "button#onetrust-accept-btn-handler"
    try:
        agree_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, agree_button_selector)))
        driver.execute_script("arguments[0].click();", agree_button)
    except:
        pass

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Parses page with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    title_selector = "article > div.offer-card__details-container > p.offer-card__title"
    desc_selector = "article > div.offer-card__details-container > p.offer-card__text"
    deal_selector = "article > div.offer-card__image-container > div > span.sr-only"

    title = [i.text for i in soup.select(title_selector)]
    desc = [i.text for i in soup.select(desc_selector)]
    deal = [i.text for i in soup.select(deal_selector)]

    grocery_ = list(zip(title, desc, deal))
    driver.quit()
    return grocery_