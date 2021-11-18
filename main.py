import requests
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
video = "https://youtu.be/OyLCbb2dSNo"
with YoutubeDL() as ydl:
      info_dict = ydl.extract_info(video, download=False) # set to True to download as mp4 too
      video_id = info_dict.get("id", None)
      video_title = info_dict.get('title', None)
str = requests.get(f'https://www.yt-download.org/api/button/mp3/{video_id}').content
soup = BeautifulSoup(str, features="html.parser")
links = []
for link in soup.findAll("a"):
    links.append(link.get("href"))
if f"download/{video_id}/mp3" in links[len(links) - 1]:
	print("downloading...")
	open(video_title+".mp3", "wb").write(requests.get(links[len(links) - 1], allow_redirects=True).content)
	print("done!")
