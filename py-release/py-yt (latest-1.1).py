import webbrowser
import time

url = input("Enter a Video URL: ")
print("1: Video (max quality)")
print("2: Audio (max quality)")
option = int(input("Choose a format (1 or 2): "))

if option == 1:
  joined_url = "https://lostshadowgd.github.io/py-yt/endpoint/?url=" + url
elif option == 2:
  joined_url = "https://lostshadowgd.github.io/py-yt/endpoint/audio/?url=" + url
else:
  print("Invalid option. Download cancelled.")
  return
  
print("Download will start soon...")
time.sleep(1.5)
webbrowser.open(joined_url)
