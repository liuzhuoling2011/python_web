import os
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', welcome!')

class JojoHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('aini', 'Hello')
        self.render('index.html', lzl="lallala")
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        self.write(username)
        self.set_cookie('123','234')

url_handler = [(r"/", IndexHandler), (r"/jojo", JojoHandler)]

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics")
)

application = tornado.web.Application(handlers=url_handler, **settings)
