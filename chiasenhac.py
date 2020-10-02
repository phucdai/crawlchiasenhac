import requests
from bs4 import BeautifulSoup
url =  'https://chiasenhac.vn/nhac-hot.html'

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.findAll('h5', class_='media-title mt-0 mb-0')
links = [link.find('a').attrs["href"] for link in titles]

for link in links:
    url = requests.get("https://chiasenhac.vn" + link)
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find("h1", class_="title").text
    urls = soup.find("a", class_="download_item").attrs["href"]
    downloaded_obj = requests.get(urls)
    with open(title + '.mp3', "wb") as file:
        file.write(downloaded_obj.content)
    print("Tiêu đề: " + title)
    print("url: " + urls)
    print("Download complete! ")
    print("_________________________________________________________________________")