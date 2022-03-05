from bs4 import BeautifulSoup
import requests
import time
import csv

hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'en-US,en;q=0.9',
        }

url1 = "https://www.metacritic.com/browse/tv/score/metascore/all/filtered?sort=desc"
url2 = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
csvfile1 = open('rt.csv', 'w', newline='', encoding='utf-8')
c = csv.writer(csvfile1)
c.writerow(['Title', 'Link', 'IMDB or M', 'Site Score', 'User Score'])

def get_metacritic_scores(tv_url):
    page = requests.get(tv_url, headers=hdr)
    soup = BeautifulSoup(page.text, 'html5lib')

    titles = soup.find_all('a', class_="title")
    scores = soup.find_all('a', class_="metascore_anchor")


    
    

    sid = 0
    tid = 0
    titless = []
    hrefs = []
    uscores = []
    mscores = []

    for title in titles:
        titless.append(title.text)
        hrefs.append(title.attrs['href'])
    
    for x in range(100):
        mscore = scores[sid].find('div')
        uscore = scores[sid+2].find('div')
        mscores.append(mscore)
        uscores.append(uscore)
        sid += 3

    for title in titless:
        c.writerow([title, hrefs[tid], 'RT', mscores[tid].text, uscores[tid].text])
        tid += 1

    
    return None

def get_imdb_scores(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    outer_titles = soup.find_all('td', class_='titleColumn')
    titles = []
    
    for t in outer_titles:
        titles.append(t.find('a'))

    outer_score = soup.find_all('td', class_='ratingColumn imdbRating')
    scores = []
    
    for s in outer_score:
       scores.append(s.find('strong'))
    
    
    for x in range(100):
        c.writerow([titles[x].text, titles[x].attrs['href'], 'IMDB', scores[x].text, 'None.'])
        
    
    return None
    
    

    
get_metacritic_scores(url1)
get_imdb_scores(url2)

csvfile1.close()