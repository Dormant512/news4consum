from bs4 import BeautifulSoup
import requests
from datetime import date, timedelta
import csv
import sys


def daterange(start_date, end_date):
    """Yields a range of dates to iterate (inluding end)."""
    for n in range(int((end_date - start_date).days + 1)):
        yield start_date + timedelta(n)


date_args = [int(i) for i in sys.argv[1:]] #YYYY, MM, DD, YYYY, MM, DD

start_date = date(*date_args[0:3])
end_date = date(*date_args[3:])


def get_news_from_date_mk(cur_date):
    """Returns all news titles from SPB.MK.RU from a given date."""
    date_url = cur_date.strftime("%Y/%m/%d")

    url = f"https://spb.mk.ru/news/{date_url}/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    sections = soup.find_all('li', class_="news-listing__item")

    cur_titles = []
    for item in sections:
        title = item.find('h3', class_="news-listing__item-title").text.strip()
        cur_titles.append(title)

    return cur_titles


write_name = f"./SCRAPED-DATA/spb-mk{'-'.join([str(i) for i in date_args])}.csv"
with open(write_name, 'w', newline='') as csvfile:
    news_writer = csv.writer(csvfile, delimiter='\t', quotechar='"', \
            quoting=csv.QUOTE_ALL, skipinitialspace=True)
    news_writer.writerow(["date", "title"])

    for single_date in daterange(start_date, end_date):
        cur_news = get_news_from_date_mk(single_date)
        print(f"SPb MK:\tNews for {single_date} scraped.")
            
        for title in cur_news:
            news_writer.writerow([single_date] + [title])
    
