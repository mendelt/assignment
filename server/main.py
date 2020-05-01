import tornado.ioloop
import tornado.web
import json

PORT = 8888


class EmailsHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(store.all())

    def post(self):
        new_id = store.store(Email.parse(json.loads(self.request.body)))
        self.write({'id': new_id})


class EmailHandler(tornado.web.RequestHandler):
    def get(self, id):
        self.write(store.retrieve(id).serialize())


class Email:
    def __init__(self, subject, body, to):
        self.subject = subject
        self.body = body
        self.to = to

    @staticmethod
    def parse(json_email):
        return Email(json_email["subject"], json_email["body"], json_email["to"])

    def serialize(self):
        return {"subject": self.subject, "body": self.body, "to": self.to}


class EmailStore:
    """
    Store emails in memory for now. Because of the auto_number field this should not be used concurrently
    """

    def __init__(self):
        self._auto_id = 0
        self._store = {}

    def store(self, email):
        self._auto_id += 1
        self._store[self._auto_id] = email
        return self._auto_id

    def retrieve(self, id):
        return self._store[int(id)]

    def all(self):
        return self._store


# Do this here for now. Refactor this out of global state later (use dependency injection for example)
store = EmailStore()


def start_app():
    """
    Set up the application, start listening and run the event loop. Does not return until event-loop gets stopped
    """

    application = tornado.web.Application([
        (r"/", EmailsHandler),
        (r"/email/([^/]+)?", EmailHandler),
    ])
    application.listen(PORT)
    print("Start listening on http://localhost:{}".format(PORT))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    start_app()
