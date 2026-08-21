import webbrowser

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