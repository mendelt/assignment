import tornado.ioloop
import tornado.web
import json

from tornado import httputil

PORT = 8888


class EmailsHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello Kopano!")

    def post(self, _):
        new_id = store.store(Email.parse(json.loads(self.request.body)))
        self.write({'id': new_id})


class Email:
    def __init__(self, subject, body, to):
        self.subject = subject
        self.body = body
        self.to = to

    @staticmethod
    def parse(json_email):
        return Email(json_email["email"], json_email["body"], json_email["to"])


class EmailStore:
    """
    Store emails in memory for now. Because of the auto_number field this should not be used concurrently
    """

    def __init__(self):
        self.auto_id = 0
        self._store = {}

    def store(self, email):
        self.auto_id += 1
        self.store[self.auto_id] = email
        return self.auto_id

    def retrieve(self, id):
        return self.store[id]


# Do this here for now. Refactor this out of global state later (use dependency injection for example)
store = EmailStore()


def startApp():
    """
    Set up the application, start listening and run the event loop. Does not return until event-loop gets stopped
    """

    application = tornado.web.Application([
        (r"/", EmailsHandler),
    ])
    application.listen(PORT)
    print("Start listening on http://localhost:{}".format(PORT))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    startApp()
