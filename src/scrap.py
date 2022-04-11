from bs4 import BeautifulSoup

def scrap(html):
    soup = BeautifulSoup(html)
    items = soup.find_all('usgs-event-item-detail')
    for item in items:
        print(item)
        parse_item(item)

def parse_item(item):
    magnitude = item.find('span', {'class':'ng-star-inserted'}).text
    place = item.find('h6', {'class':'header'}).text
    time = item.find('span', {'class':'time'}).text
    depth = item.find('aside').find('span', {'class':'ng-star-inserted'}).text
    print("Magnitude:" + magnitude)
    print("Place:" + place)
    print("Time:" + time)
    print("Depth:" + depth)