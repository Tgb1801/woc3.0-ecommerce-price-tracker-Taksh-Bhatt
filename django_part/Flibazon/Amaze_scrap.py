# Amazon Website

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(PATH, options=options)


def get_product_name_from_amaze(url):
    driver.get(url)

    name_of_product = driver.find_element_by_id("titleSection").find_element_by_id("productTitle").text

    return name_of_product


def get_product_price_from_amaze(url):
    driver.get(url)

    try:
        # Regular Price
        price_of_product = driver.find_element_by_id("priceblock_ourprice").text
    except Exception:
        try:
            # Deal Price
            price_of_product = driver.find_element_by_id("priceblock_dealprice").text
        except Exception:
            try:
                price_of_product = driver.find_element_by_id("tmmSwatches").find_element_by_class_name("a-color-base").find_elements_by_tag_name("span")[0].text
            except Exception:
                try:
                    price_of_product = driver.find_element_by_id("priceblock_saleprice").text
                except Exception:
                    # No Price
                    price_of_product = -1   # -1 means the price is not available

    return price_of_product


