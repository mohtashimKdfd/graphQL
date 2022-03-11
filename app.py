import falcon
import json
from database import engine, session, init_session

class Home:
    def on_get(self, req, resp):
        resp.body = json.dumps("Hello Boiss")
        return resp

init_session()    
api = falcon.App()
api.add_route('/',Home())