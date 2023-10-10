from scraper import scrapeAllCategories
from scraper import TOIclassNames
import csv

def scrape_and_save_headlines_to_csv(csv_filename):
    try:
        headlines = scrapeAllCategories()

        if headlines:
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:  # Use 'a' for append mode, but using w as of now
                fieldnames = ['headline', 'link','image','category']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                # Check if the file is empty, and if so, write the header row
                if csvfile.tell() == 0:
                    writer.writeheader()
                
                for headline in headlines:
                    writer.writerow(headline)
            print(f'New headlines appended to {csv_filename}')
        else:
            print('Failed to retrieve headlines from the web page.')

    except Exception as e:
        print('Error:', str(e))

if __name__ == '__main__':
    csv_filename = '../dataset/toi_headlines.csv'
    scrape_and_save_headlines_to_csv(csv_filename)
