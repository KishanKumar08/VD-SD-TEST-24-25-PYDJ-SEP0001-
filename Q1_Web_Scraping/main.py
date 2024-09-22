import requests
from bs4 import BeautifulSoup

class NewsScraper:
    """
    A class to scrape the latest articles from a news website.

    Attributes:
    -----------
    url : str
        The URL of the news website to scrape.
    headers : dict
        The HTTP headers for mimicking a browser request.

    Methods:
    --------
    fetch_page():
        Sends a GET request to the specified URL and returns the page content.
    extract_articles(soup):
        Parses the HTML and extracts the first 10 article titles and URLs.
    scrape():
        Main method to perform the scraping and print the article details.
    """
    
    def __init__(self, url):
        """
        Initializes the NewsScraper with the provided URL and a default User-Agent header.

        Parameters:
        -----------
        url : str
            The URL of the news website to scrape.
        """
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def fetch_page(self):
        """
        Sends a GET request to the specified URL and returns the response content.

        Returns:
        --------
        BeautifulSoup:
            Parsed HTML content of the page if the request is successful, otherwise None.
        """
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()  # Check if request was successful
            print(f"Successfully fetched the page: {self.url}")
            return BeautifulSoup(response.content, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve the page. Error: {e}")
            return None

    def extract_articles(self, soup):
        """
        Parses the HTML content and extracts the first 10 article titles and URLs.

        Parameters:
        -----------
        soup : BeautifulSoup
            The parsed HTML content of the page.

        Returns:
        --------
        List[Tuple[str, str]]:
            A list of tuples containing article titles and URLs.
        """
        articles = []
        anchor_tags = soup.find_all('a', href=True)  # Finding all anchor tags

        for anchor in anchor_tags:
            title = anchor.get_text(strip=True)
            link = anchor['href']

            # Ensure the title and link are valid and filter out unwanted URLs
            if title and link and 'cnn.com' in link:
                full_link = link if link.startswith('http') else f"https://edition.cnn.com{link}"
                articles.append((title, full_link))

            # Limit to first 10 articles
            if len(articles) >= 10:
                break
        
        return articles

    def scrape(self):
        """
        Main method that orchestrates the scraping process by fetching the page,
        extracting the articles, and printing them.

        Prints:
        -------
        Prints the first 10 article titles and URLs found on the page.
        """
        soup = self.fetch_page()
        if soup:
            articles = self.extract_articles(soup)
            if articles:
                print("\nTop 10 Articles:\n")
                for i, (title, url) in enumerate(articles, 1):
                    print(f"{i}. Title: {title}\n   URL: {url}\n")
            else:
                print("No articles found.")
        else:
            print("Failed to scrape the website.")

# Example Usage
if __name__ == '__main__':
    # Specify the URL of the news website (e.g., CNN)
    news_scraper = NewsScraper('https://edition.cnn.com/')
    news_scraper.scrape()
