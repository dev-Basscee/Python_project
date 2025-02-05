
import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.parse import quote_plus

def web_search():
    search_term = input("Enter what you want to search for: ")
    
    # Format the search term for URL
    formatted_search = quote_plus(search_term)
    
    # Multiple search engines and their search URLs
    search_engines = {
        'google': f'https://www.google.com/search?q={formatted_search}',
        'duckduckgo': f'https://duckduckgo.com/?q={formatted_search}',
        'bing': f'https://www.bing.com/search?q={formatted_search}'
    }
    
    try:
        # Using Google as default search engine
        url = search_engines['google']
        
        # Headers to mimic browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Get the webpage
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find search results
        search_results = soup.find_all('div', class_='g')
        
        print("\nSearch Results:\n")
        
        # Extract and display results
        for result in search_results[:5]:  # Display top 5 results
            title = result.find('h3')
            link = result.find('a')
            snippet = result.find('div', class_='VwiC3b')
            
            if title and link and snippet:
                print(f"Title: {title.text}")
                print(f"URL: {link['href']}")
                print(f"Description: {snippet.text}\n")
                
        # Ask if user wants to open results in browser
        open_browser = input("Would you like to open the search in browser? (yes/no): ")
        if open_browser.lower() == 'yes':
            webbrowser.open(url)
            
    except requests.RequestException as e:
        print(f"An error occurred: {e}")    search_term = input("Enter what you want to search for: ")
    
    # Format the search term for URL
    formatted_search = quote_plus(search_term)
    
    # Multiple search engines and their search URLs
    search_engines = {
        'google': f'https://www.google.com/search?q={formatted_search}',
        'duckduckgo': f'https://duckduckgo.com/?q={formatted_search}',
        'bing': f'https://www.bing.com/search?q={formatted_search}'
    }
    
    try:
        # Using Google as default search engine
        url = search_engines['google']
        
        # Headers to mimic browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Get the webpage
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find search results
        search_results = soup.find_all('div', class_='g')
        
        print("\nSearch Results:\n")
        
        # Extract and display results
        for result in search_results[:5]:  # Display top 5 results
            title = result.find('h3')
            link = result.find('a')
            snippet = result.find('div', class_='VwiC3b')
            
            if title and link and snippet:
                print(f"Title: {title.text}")
                print(f"URL: {link['href']}")
                print(f"Description: {snippet.text}\n")
                
        # Ask if user wants to open results in browser
        open_browser = input("Would you like to open the search in browser? (yes/no): ")
        if open_browser.lower() == 'yes':
            webbrowser.open(url)
            
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    web_search()
