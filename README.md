# Tufts GF Menus

https://spartan-thunder-180219.appspot.com

Displays the day's GF options in the Tufts dining halls.

Problem:
Too many steps to get GF menus, bad UI

Steps to get GF Menu through Tufts app
* Select dining
* Select location
* Select day (hard to click)
* Select allergens (Wheat, gluten, "hide" option)
* ( Repeat for other locations )

Goal:
Make a mobile friendly site that lets me view the menus so I can quickly see my options and decide between locations.

Implementation:
Site is hosted on Google App Engine and uses the webapp2 framework with python. Info is scraped with Beautiful Soup and displayed using jinja2 templates.

To do:
* Switch to flask?
