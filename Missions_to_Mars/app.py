from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    mars_data = mongo.db.mars.find_one()
    if mars_data is None:
        mars_data = {
        'news_title':'',
        'news_paragraph':'',
        'featured_image_url':'',
        'facts_html':'',
        'hemi': [{'img_url': ''} for x in range(0,4)]}
    return render_template("index.html",data=mars_data)


@app.route("/scrape")
def scrape():
    new_info = scrape_mars.scrape()
    mongo.db.mars.update({}, new_info, upsert=True)
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)





