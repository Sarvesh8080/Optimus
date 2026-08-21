import webbrowser
from urllib.parse import quote_plus

def search_google(query):
    url = "https://www.google.com/search?q=" + quote_plus(query)
    webbrowser.open(url)

def search_youtube(query):
    url = "https://www.youtube.com/results?search_query=" + quote_plus(query)
    webbrowser.open(url)

def search_stackoverflow(query):
    url = "https://stackoverflow.com/search?q=" + quote_plus(query)
    webbrowser.open(url)

def search_reddit(query):
    url = "https://www.reddit.com/search/?q=" + quote_plus(query)
    webbrowser.open(url)

def search_twitter(query):
    url = "https://twitter.com/search?q=" + quote_plus(query)
    webbrowser.open(url)

def search_facebook(query):
    url = "https://www.facebook.com/search/top/?q=" + quote_plus(query)
    webbrowser.open(url)

def search_linkedin(query):
    url = "https://www.linkedin.com/search/results/all/?keywords=" + quote_plus(query)
    webbrowser.open(url)
    

def search_instagram(query):
    url = "https://www.instagram.com/explore/tags/" + quote_plus(query)
    webbrowser.open(url)   

def search_instagram(query):
    url = "https://www.instagram.com/explore/tags/" + quote_plus(query)
    webbrowser.open(url)

                    

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "stackoverflow": "https://stackoverflow.com",
    "reddit": "https://www.reddit.com",
    "twitter": "https://twitter.com", 
    "facebook": "https://www.facebook.com",   
     "linkedin": "https://www.linkedin.com",
    "instagram": "https://www.instagram.com", }  

def open_website(website_name):
    url = WEBSITES.get(website_name)

    if url is None:
        return False

    webbrowser.open(url)
    return True