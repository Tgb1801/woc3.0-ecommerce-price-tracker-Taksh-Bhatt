# ebay Website

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#webdriver_manager automatically downloads the required version of the webdriver.

# PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver = webdriver.Chrome(PATH, options=options)


def get_product_name_from_eba(url):
    driver.get(url)

    try:
        name_of_product = driver.find_element_by_id("itemTitle").text
    except Exception:
        name_of_product = driver.find_element_by_id("mainContent").find_element_by_class_name("product-title").text

    return name_of_product


def get_product_price_from_eba(url):

    driver.get(url)

    try:
        try:
            price_of_product = driver.find_element_by_id("convbinPrice").text
        except Exception:
            price_of_product = driver.find_element_by_id("prcIsum").text
    except Exception:
        try:
            price_of_product = driver.find_element_by_class_name("item-desc").find_element_by_class_name("display-price").text
        except Exception:
            price_of_product = driver.find_element_by_id("prcIsum_bidPrice").text

    return price_of_product


