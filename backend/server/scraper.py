import requests
from bs4 import BeautifulSoup

TOIclassNames={
    'india':['div',['col_l_6','col_1_5','iN5CR']],
    '':['div',['col_l_6']],
    'sports/cricket':['div',['col_l_6','col_1_3']],
    'auto':['li',['clearfix']],

}

def scrape_toi_headlines(element,category=''):
    url = 'https://timesofindia.indiatimes.com/'+category
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all the div elements with the class "col_l_6"
            divs = soup.find_all(element, class_=TOIclassNames[category])
            figures = soup.find_all('figure')
            headlines = []
            for fig in figures:
                try:
                    headline_text = fig.find('figcaption').text
                    headline_link = fig.find('a')['href']
                    headline_image = fig.find('img')['data-src']

                    headlines.append({
                        'headline': headline_text,
                        'link': headline_link,
                        'image': headline_image,
                        'category':category
                    })
                except:
                    pass
            # Loop through the div elements and extract the data you need
            for div in divs:
                try:
                    # Extract the headline text from the figcaption
                    headline_text = div.find('img')['alt'].strip()

                    # Extract the link to the news article from the anchor inside the div
                    headline_link = div.find('a')['href']
                    
                    headline_image = div.find('img')['data-src']

                    headlines.append({
                        'headline': headline_text,
                        'link': headline_link,
                        'image': headline_image,
                        'category':category
                    })
                # except Exception as e:
                #     print('Error:', str(e))
                except:
                    pass

            return headlines
        else:
            return None
    except Exception as e:
        print('Error:', str(e))
        return None
    
def scrapeAllCategories():
    headlines = []
    for category in TOIclassNames:
        headlines.extend(scrape_toi_headlines(TOIclassNames[category][0],category))
    return headlines

if __name__ == '__main__':
    headlines = scrapeAllCategories()
    if headlines:
        for headline in headlines:
            print(f"Headline: {headline['headline']}")
            print(f"Link: {headline['link']}")
            print(f"Image: {headline['image']}")
            print()
    else:
        print('Failed to retrieve the web page.')
        

