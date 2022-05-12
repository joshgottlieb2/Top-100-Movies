from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

movies = soup.find_all(name="h3", class_="title")


movie_titles = [movie.getText() for movie in movies]
# print(movie_titles)
movies_rev = movie_titles[::-1]
print(movies_rev)

with open("movies.txt", mode="w") as file:
    for movie in movies_rev:
        file.write(f"{movie}\n")


