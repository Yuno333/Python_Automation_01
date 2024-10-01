from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
AUTH = 'brd-customer-hl_4a38c7e4-zone-scraping_browser2:8kus97wcvi98'

SBR_WEBDRIVER = f'https://{AUTH}@zproxy.lum-superproxy.io:9515'


def main():
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')



    driver.get('https://www.booking.com/')
    print('Taking page screenshot to file page.png')
    driver.get_screenshot_as_file('./page.png')
    print('Navigated! Scraping page content...')
    html = driver.page_source
    print(html)


if __name__ == '_main_':
  main()