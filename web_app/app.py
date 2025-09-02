from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import pymongo
import json
from bson import json_util
app = Flask(__name__)


# database connection 



# start database configure
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.test
# client.admin.command('ping')  # Quick and safe connection test
# print(" MongoDB Atlas connection successful.")
collection = db['flask-tutorial']
# end database configure


@app.route("/")
def hello_world():
    return render_template("index.html")
    # return render_template("success_page.html")

@app.route("/sign_up", methods=["POST"])
def signup_submit():
    try:
        data = {"username": request.form.get("username"),
                "email": request.form.get("email"),
                "password": request.form.get("password")
                }

        if data.get('email'):
            record = collection.find_one({'email': data['email']})
            print("redord=> ", record)

            
            if record is None:
                result = collection.insert_one(data)
                return render_template("success_page.html")
            else:
                return render_template("index.html", message="warning" ,warning_msg = f"{data.get('email')} is already found)")
        
    except Exception:
        return render_template("index.html",message="error", error_msg= "An Error occured while submiting.Please retry after some time.")        
            

@app.route("/sign_in", methods=["POST"])
def signin_submit():
    data = {"email": request.form.get("email"),
            "password": request.form.get("password")
            }
    if data.get("email") and data.get("password"):
        record = collection.find_one({'email': data['email'], 'password':data['password']})
        # print("login record-> ", record)
        if record:
            data = list(collection.find({}))
            
            # print("data=> ", data)
            return json.loads(json_util.dumps(data))
        
    return render_template("index.html",message="error", error_msg= "Invalid email or password.")



if __name__ == '__main__':
    app.run(debug=True, port=8080)