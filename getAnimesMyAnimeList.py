import random
import requests
from bs4 import BeautifulSoup

url = 'https://myanimelist.net/topanime.php'
def getAnime(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    animeNameTags = soup.select('h3.anime_ranking_h3')
    animeHref = soup.select('h3.anime_ranking_h3 a')
    length = len(animeNameTags)
    randNum = random.randrange(0, length)
    animeEpisodes = soup.select('div.information')
    animeEpisodeFilter = animeEpisodes[randNum].text
    animeEpisode = animeEpisodeFilter.split('\n')[1]
    newUrl = animeHref[randNum]['href']
    getAnimeInfo(newUrl, animeEpisode)


def getAnimeInfo(newUrl, animeEpisode):
    response = requests.get(newUrl)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    animeNameTag = soup.select('title')
    animeName = animeNameTag[0].text.split(' - ')[0]
    getGenre = soup.find_all(text='Genres:')[0]
    animeGenreAux = getGenre.parent # .parent
    animeGenre = animeGenreAux.find_all('a')
    animeGenreList = []
    for genre in animeGenre:
        animeGenreList.append(genre.text)
    animeGenreString = 'Genres: (' + ', '.join(animeGenreList) + ')'
    getSynopsis = soup.find('p', itemprop='description').text.split('[Written by MAL Rewrite]')[0]
    print(f'-------------------------------------\nKATIAAAAAAU GERANDO ANIME KATIAAAAAAU\n{animeName} \n{animeEpisode}\n{animeGenreString}\n---Synopsis---\n{getSynopsis}')
    


def main():
    getAnime(url)
    while(True):
        answer = input('________________________\nAnother one? (y/n) ')
        if answer != 'y':
            break
        else:
            getAnime(url)

if __name__ == '__main__':
    main()