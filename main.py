import jinja2
import os
import webapp2
from getMenuData import menus

template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))

class MenuPage(webapp2.RequestHandler):
    def get(self, meal_time):
        meal_times = ["1","2","3"]
        if meal_time in meal_times:
            menu = menus(meal_time)
        else:
            self.redirect("/1", abort=True)

        context = {
            "active": meal_time,
            "menu": menu
        }
        template = template_env.get_template('index.html')
        self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([(r'/(.*)', MenuPage)], debug=True)
