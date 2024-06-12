from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract


def scrape_books():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Hindi Books")
    search_box.send_keys(Keys.RETURN)

    # Scraping book details
    books = []
    book_elements = driver.find_elements(By.XPATH, '//div[@class="puisg-col puisg-col-4-of-12 puisg-col-8-of-16 puisg-col-12-of-20 puisg-col-12-of-24 puis-list-col-right"]')
    for book_element in book_elements:
        name = book_element.find_element(By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]').text
        price = book_element.find_element(By.XPATH, './/span[@class="a-price-whole"]').text
        rating = book_element.find_element(By.XPATH, '//span[@class="a-size-base s-underline-text"]').text
        books.append({"name": name, "price": price, "rating": rating})
    driver.quit()
    return books

# Mobile Interaction using Appium


def capture_screenshot():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "app": "C://Users//RIVAN//AppData//Local//Android//Sdk//platform-tools//amazon-shopping.apk"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    # Capture screenshot of product list
    screenshot = driver.get_screenshot_as_png()
    with open("screenshot.png", "wb") as f:
        f.write(screenshot)

    driver.quit()
    return screenshot

# Text Extraction with OCR


def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except FileNotFoundError:
        print("Error: Image file not found.")
        return ""

# Data Comparison and Report Generation


def compare_data(web_data, ocr_data):
    matching_prices = []
    mismatching_prices = []
    for web_book in web_data:
        for ocr_book in ocr_data:
            if web_book["name"] == ocr_book["name"]:
                if web_book["price"] == ocr_book["price"]:
                    matching_prices.append({"name": web_book["name"], "price": web_book["price"]})
                else:
                    mismatching_prices.append({"name": web_book["name"], "web_price": web_book["price"],
                                               "ocr_price": ocr_book["price"]})

    return matching_prices, mismatching_prices


if __name__ == "__main__":

    # Step 1: Web Automation
    web_data = scrape_books()

    # Step 2: Mobile Interaction
    capture_screenshot()

    # Step 3: Text Extraction with OCR
    ocr_data = extract_text_from_image("screenshot.png")
    print(ocr_data)  # Check OCR output

    # Step 4: Data Comparison and Report Generation
    matching_prices, mismatching_prices = compare_data(web_data, ocr_data)

    # Generate report
    with open("report.txt", "w") as f:
        f.write("Products with matching prices:\n")
        for product in matching_prices:
            f.write(f"{product['name']}: {product['price']}\n")

        f.write("\nProducts with discrepancies in prices:\n")
        for product in mismatching_prices:
            f.write(f"{product['name']}: Web Price - {product['web_price']}, OCR Price - {product['ocr_price']}\n")

    print("Report generated successfully.")
