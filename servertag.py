import flask
import os
from pymongo import MongoClient

# Get de uri for Atlas MongoDB database in the cloud
connectString = os.getenv("DBCONNECT")

# connect to Mongo on the cloud
client = MongoClient(connectString)

# that´s the database we want -> "TaggalinesGallore" (a typo, I know)
db = client.TagallinesGallore

# instatiate Flask server
app = flask.Flask("gettagline")

# set parameter to debug
app.config["DEBUG"] = True

# set the basic route for the API , a simple GET


@app.route('/', methods=['GET'])
def home():
    # Get one random document from the tagline collection.
    wresponse = (list(db.taglines.aggregate(
        [{"$sample": {"size": 1}}]))[0]['0'])
    # return to http request with Status 200 (ok)
    return (wresponse, 200)


# this is the main program
app.run()
