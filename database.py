from deta import Deta
import os
from dotenv import load_dotenv
load_dotenv()
DETA_KEY = os.getenv('DETA_KEY')
deta = Deta(DETA_KEY)
db = deta.Base('users')

def insert_user(username, password, email, dateofbirth, qualification, learnertype):
    return db.put({"username":username, "password": password, "email": email, "dateofbirth": dateofbirth, "qualification": qualification, "learnertype": learnertype})

def checkUserExist(username):
    return db.fetch({"username?contains": username})