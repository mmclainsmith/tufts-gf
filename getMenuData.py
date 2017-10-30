import sys
from BeautifulSoup import BeautifulSoup
import urllib
from datetime import datetime

def menus(meal):
    halls = {"Carmichael":"09", "Dewick":"11"}

    menus = {}
    for hall in halls:
        info = (halls[hall], datetime.now().month, datetime.now().day, datetime.now().year, meal)
        url = "http://menus.tufts.edu/fpmobile/shortmenu.asp?sName=Tufts+Dining&locationNum={0}&locationName=&naFlag=1&WeeksMenus=This+Week%{2}s+Menus&dtdate={1}%2F{2}%2F{3}&mealName=&savedallergens=%FD%FD%FD%FD%FD%FDON%FD%FDON%FD%FDNOCONTAINS&savedwebcodes=%FDlngcurselmeal%3D3&lngcurselmeal={4}".format(*info)

        print url
        site = urllib.urlopen(url).read()
        soup = BeautifulSoup(site)
        menu_items = soup.findAll(True, {"class":["shortmenurecipes", "shortmenucats"]})

        categories = []
        new_cat = {}
        for item in menu_items:
            if "shortmenucats" in item["class"]:
                if new_cat:
                    categories.append(new_cat)
                    new_cat = {}
                new_cat["name"] = item.getText().replace("-","").title()
                new_cat["items"] = []
            else:
                new_cat["items"].append(item.getText())
        menus[hall] = categories
    return menus
