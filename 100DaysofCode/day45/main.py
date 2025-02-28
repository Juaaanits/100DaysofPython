'''
Instructions for Scraping the Top Movies List
1. Understand the Goal
The goal is to scrape a list of movies from a website and save them to a text file.
2. Choose the Website to Scrape
The website used in the code is an archived version of Empire Online’s "Best Movies" list.
The URL being used:
https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/
3. Fetch the Web Page
Use the requests library to send an HTTP GET request to the URL.
Store the response content (HTML) in a variable.
4. Parse the HTML Content
Use BeautifulSoup to parse the website’s HTML.
Identify the tags and classes containing the movie titles by inspecting the webpage structure using Chrome DevTools (right-click → Inspect Element).
5. Extract the Movie Titles
Use .find_all() to get all movie titles from the HTML.
Extract only the text of each title.
6. Reverse the Order
The movies might be listed in descending order (from best to worst), so reverse the list if needed.
7. Save the Data to a File
Open a file (movies.txt) in write mode.
Write each movie title into the file, each on a new line.
'''

import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]    
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
