# Flipkart Website

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#webdriver_manager automatically downloads the required version of the webdriver.

# PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver = webdriver.Chrome(PATH, options=options)


def get_product_name_from_flip(url):

    driver.get(url)

    name_of_product = driver.find_element_by_class_name("B_NuCI").text

    return name_of_product


def get_product_price_from_flip(url):

    driver.get(url)

    price_of_product = driver.find_element_by_class_name("_25b18c").find_elements_by_tag_name("div")[0].text

    return price_of_product

