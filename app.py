from flask import Flask, render_template
import feedparser

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    
    # parse YouTube feed from MyKampus TV
    rss = feedparser.parse(
        'https://www.youtube.com/feeds/videos.xml?channel_id=UChVS7qvjXYiPuqYNtiAPOWw')
    urls = []

    # print video links
    for item in rss.entries:
        for element in item.links:
            txt = element['href'].replace('watch?v=', 'embed/')
            urls.append(txt)  # add URLs to list
    
    return render_template("index.html", urls=urls)


@app.route("/mktv")
def mktv():

    # Same as Index page, parse YouTube feed from MyKampus TV
    rss = feedparser.parse(
        'https://www.youtube.com/feeds/videos.xml?channel_id=UC0wQr4JFllCGu5lehj4gHGw')
    urls = []

    # print video links
    for item in rss.entries:
        for element in item.links:
            txt = element['href'].replace('watch?v=', 'embed/')
            urls.append(txt)  # add URLs to list
    
    return render_template("mktv.html", urls=urls)


@app.route("/player")
def player():
    # page for dedicated MKR webplayer
    return render_template("player.html")


@app.route("/about")
def about():
    # about page
    return render_template("about.html")
