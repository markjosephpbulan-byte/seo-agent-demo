import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch {url} (status {response.status_code})")
            return None
        soup = BeautifulSoup(response.text, "lxml")
        return soup
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_page_data(url):
    soup = fetch_page(url)
    if not soup:
        return None

    title = soup.find("title").text if soup.find("title") else "No title"
    meta = soup.find("meta", attrs={"name":"description"})
    meta_content = meta["content"] if meta else "No meta description"
    h1 = soup.find("h1").text if soup.find("h1") else "No H1"

    return {
        "url": url,
        "title": title,
        "meta_description": meta_content,
        "h1": h1
    }

# Test it
if __name__ == "__main__":
    url = "https://example.com"  # Replace with any small demo site
    data = extract_page_data(url)
    print(data)