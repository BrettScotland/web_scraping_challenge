from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Mars_scrape

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    Mars_data = mongo.db.data.find_one()

    # Return template and data
    return render_template("index.html", vacation=Mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    Mars_dict = Mars_scrape.scrape_info()

    # Update the Mongo database using update and upsert=True
    collection = mongo.db.data
    collection.update({}, Mars_dict, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
