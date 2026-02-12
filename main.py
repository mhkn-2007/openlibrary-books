import requests

def fetch_books():
    """
    Fetch books data from OpenLibrary API.
    Returns a list of books.
    """
    url = "https://openlibrary.org/search.json?q=python&limit=50"

    try:
        response = requests.get(url)
        response.raise_for_status()  # check for HTTP errors
        data = response.json()
        return data.get("docs", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


def filter_books(books):
    """
    Filter books published after the year 2000.
    """
    filtered = []
    for book in books:
        year = book.get("first_publish_year")
        title = book.get("title")
        authors = book.get("author_name", [])

        if year and year > 2000:
            filtered.append({
                "title": title,
                "author": authors[0] if authors else "Unknown",
                "year": year
            })

    return filtered


def save_to_csv(books):
    """
    Save filtered books to a CSV file.
    """
    pass


def main():
    books = fetch_books()
    filtered_books = filter_books(books)

    print(f"Filtered books count: {len(filtered_books)}")


if __name__ == "__main__":
    main()
