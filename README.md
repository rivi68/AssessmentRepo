# Book Price Comparison Tool

This is a Python script that automates the process of comparing book prices from Amazon's website with prices extracted from screenshots using Optical Character Recognition (OCR). The script generates a report highlighting matching prices and discrepancies.

## Features

- Web scraping with Selenium to fetch book details from Amazon.
- Mobile interaction with Appium to capture screenshots of product listings.
- Text extraction from images using the pytesseract library.
- Data comparison and report generation.

## Installation

1. Clone the repository.

2. Install dependencies.

3. Ensure you have Chrome WebDriver installed and its path is added to your system's PATH environment variable. You can download Chrome WebDriver.

4. Set up Appium for mobile interaction. Follow the installation instructions (http://appium.io/docs/en/about-appium/getting-started/).

## USAGE

1. Modify the `scrape_books()` function in `main.py` to customize the search criteria for books.

2. Run the script:

3. Check the generated report in `report.txt` for matching prices and discrepancies.

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
