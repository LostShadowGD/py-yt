import webbrowser
import time

url = input("Enter a Video URL: ")
joined_url = "https://lostshadowgd.github.io/py-yt/endpoint/?url=" + url
print("Download will start soon...")
time.sleep(1.5)
webbrowser.open(joined_url)
