from web_download import selenium_download
from scrap import scrap

def main():
    #html = download.selenium_download('https://www.ngdc.noaa.gov/hazel/view/hazards/earthquake/event-data')

    html = selenium_download()
    #html = download('https://www.ngdc.noaa.gov/hazel/view/hazards/earthquake/event-data')
    #print(html)

    scrap(html)

if __name__ == "__main__":
    main()