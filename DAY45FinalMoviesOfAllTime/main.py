from bs4 import BeautifulSoup
import requests

URL="https://www.empireonline.com/movies/features/best-movies-2/"
reponse = requests.get(URL)
# print(reponse)
html = reponse.text
# print(html)
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

all_movies = soup.find_all(name="h3",class_="listicleItem_listicle-item__title__hW_Kn")
movie_title = [movie.getText() for movie in all_movies]
movies = movie_title[::-1]
# print(movies)
#
# for n in range(len(movie_title)-1, 0 , -1):
#     print(movie_title[n])

with open("movies.txt", "w") as file:
    for movie in movies:
     file.write(f"{movie}\n")


