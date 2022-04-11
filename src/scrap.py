from bs4 import BeautifulSoup

def scrap(html):
    data = []
    soup = BeautifulSoup(html)
    items = soup.find_all('usgs-event-item-detail')
    for item in items:
        try:
            item_data = parse_item(item)
            data.append(item_data)
        except:
            print("Error parsing item:" + item)
        
    return data

def parse_item(item):
    magnitude = item.find('span', {'class':'ng-star-inserted'}).text
    place = item.find('h6', {'class':'header'}).text
    time = item.find('span', {'class':'time'}).text
    depth = item.find('aside').find('span', {'class':'ng-star-inserted'}).text
    return [time, place, depth, magnitude]