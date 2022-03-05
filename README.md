#ReadMe.md

My goal for this project was to scrape the top 100 movies from Metacritic and Rotten Tomatoes. Unfortunately,
I could not scrape Rotten Tomatoes without Selenium and I couldn't get Selenium working on my computer in time.
Instead, I scraped the top 100 movies on IMDB and Metacritic. I had some trouble scraping Metacritic at first,
but once I figured out how to scrape with a header it was just like any other website.

First, I have a function (get_metacritic_scores) that cycles through every review link on the top 100 page for
Metacritic and puts the title, href, and scores into a csv. Next, another function (get_imdb_scores) does the same
thing with the first 100 headlines on the IMDB top 250 TV show list. Finally, I close the csv file.