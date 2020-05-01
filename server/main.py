import tornado.ioloop
import tornado.web


PORT = 8888


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Kopano!")


def startApp():
    """
    Set up the application, start listening and run the event loop. Does not return until event-loop gets stopped
    """

    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(PORT)
    print("Start listening on http://localhost:{}".format(PORT))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    startApp()
