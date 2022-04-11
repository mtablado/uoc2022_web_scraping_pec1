from socket import timeout
import urllib
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def download(url):
    print('Downloading:', url)
    try:

        # Replace python default user agent.
        headers = {'User-Agent': 'Mozilla/5.0'}
        request = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(request, timeout=60).read()

    except urllib.error as e:
        print('Download error:', e.reason)
        html = None

    except timeout as e:
        print('Timeout error:', e.reason)
        html = None
    return html

def selenium_download(url):
    '''
    Downloads the page source of a web using selenium webdriver which allows to load 
    advanced javascript webpages.
    '''
    url = 'https://earthquake.usgs.gov/earthquakes/map/?extent=-89.58992,-357.1875&extent=89.58992,717.1875&range=search&listOnlyShown=true&baseLayer=terrain&timeZone=utc&search=%7B%22name%22:%22Search%20Results%22,%22params%22:%7B%22starttime%22:%221900-01-01%2000:00:00%22,%22minmagnitude%22:7,%22orderby%22:%22time%22%7D%7D'
    browser = webdriver.Firefox()
    browser.get(url)

    # There is an overlay shown with text "Earthquakes loaded" which only appears after data been loaded. Useful.
    class_name = "cdk-global-overlay-wrapper"

    try:
        print("Waiting for data grid container to be loaded")
        elem = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name)) #This is a dummy element
        )
    finally:
        print("Data grid container found. Closing driver.")
        html = browser.page_source
        browser.close()
    return html