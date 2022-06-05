# MyKampus Radio Mini Web Player

![MyKampus Radio Logo](/static/MKR-Logo-Full.png)

## [Video Demo](https://youtu.be/4ZqF1GhT4hA)

## [Website Demo](https://mkr-website-flask.et.r.appspot.com/)

### Description

Simple and basic website to view latest YouTube videos from MyKampus Radio and MyKampus TV as well with online radio player embedded in.

In this website, user can navigate and see latest content from MyKampus Radio, from Podcast (Clips from Live Show) to Entertainment videos as well Radio Web Player which they can access easily.

### Files Structure

| static

​ | about.css

​ | MKR-Logo.png

​ | MKR-Logo-Full.png

​ | style.css

| templates

​ | about.html

​ | index.html

​ | layout.html

​ | mktv.html

​ | player.html

| app.py

| README.md

| requirements.txt

## Files Details

### app.py

Route /index and /mktv uses exact match code except URL (for ID). The code use feedparser library to XML content from respective channel. With that, we can go through each content with for loop, replacing the 'watch?v=' to 'embed/' and append it to the empty list we created.

It should look like this:

```text
# Before
https://www.youtube.com/watch?v=/<Video ID>

# After
https://www.youtube.com/embed/<Video ID>
```

For other route /player and /about, we just render it with template from layout.html

### layout.html

Setting up the head with common tags (script, css, bootstrap, etc.).

By using Jinja, we set up the navigation bar dynamically to indicate which current page are active.

After creating the nav tag and div inside of it. We use Jinja to generate the nav item using navigation_bar.

### player.html

Since we only use iFrame, we can just put iFrame tag in it.

### index.html and mktv.html

Both page use same tag, we simply use Jinja to generate each iFrame individually using for loop.

### about.html

This contain just contain bunch of text and hyperlink. Icons are from fontawesome.

#### Written in Python 3 with Flask library in Visual Studio Code

### Thanks to

[nick3499](https://gist.github.com/nick3499/5931a7beff3c85593e9018cca11ee91a) for Python2 code on getting URLs with Feedparser

### Requirements

flask
feedparser

### Fonts

[Poppins](https://fonts.google.com/specimen/Poppins) from Google

#### Bootstrap version 4.5.3

### Note on RSS Feed

At first, I use YouTube Data API v3 in order to get video feeds from YouTube. But YouTube have quota for free account and I have to scrap that idea and find other alternative which is YouTube-DL.

After doing some reading on YouTube-DL and checking things out. The YouTube-DL does not really suit my case since I just need a simple catalog to test things out.

From there, I came across with getting the feed with RSS and stumble upon nick3499 solution on getting things done with Feedparser.

Although, there are limitation with RSS which is whenever embedding a restricted video, YouTube would not allow the video to be embed and need to watch on their site.

### Note on iFrame Web Player

Due to limitation on radio player of MyKampus Radio, We can't customize the player as we want to. With that, we proceed iFrame embed directly to the HTML page.

### Why This Project Feels Empty?

Simply because I'm not ambitious enough to make it into a big project. My intentions is to make a simple web page for user to navigate and check for latest content from MyKampus Radio in a single website.

### DISCLAIMER

This project is purely for academic purpose, it was made for CS50 Final Year Project submission.
