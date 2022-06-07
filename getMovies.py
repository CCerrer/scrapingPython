import random
import requests
from bs4 import BeautifulSoup


link = 'http://www.imdb.com/chart/top'

def main():
    response = requests.get(link)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    movieTags = soup.select('td.titleColumn')
    innerMovieTags = soup.select('td.titleColumn a')
    movieRatings = soup.select('td.ratingColumn strong')

    # list comprehension to get the years
    def getYear(movieTag):
        movieSplit = movieTag.text.split()
        year = movieSplit[-1]
        return year
    yearsList = [getYear(tag) for tag in movieTags]
    actorsList = [tag['title'] for tag in innerMovieTags]
    titlesList = [tag.text for tag in innerMovieTags]
    ratingsList = [tag.text for tag in movieRatings]

    # choose random number within 1 to len(list)

    while(True):
        randNum = random.randrange(0, len(titlesList))
        print(f'{titlesList[randNum]} {yearsList[randNum]} - {ratingsList[randNum]} \n{actorsList[randNum]}')
        answer = input('________________________\nAnother one? (y/n) ')
        if answer == 'n':
            break
        else:
            print('\n')





if __name__ == '__main__':
    main()