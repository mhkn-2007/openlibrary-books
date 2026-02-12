import requests
import csv

# Constant for the API URL
API_URL = "https://openlibrary.org/search.json?q=python&limit=50"


def fetch_books():
    """
    Fetch books data from OpenLibrary API.
    Returns a list of books.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        return data.get("docs", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


def filter_books(books):
    """
    Filter books published after the year 2000 and format authors.
    Returns a list of dictionaries with keys: title, author, year.
    """
    filtered = []
    for book in books:
        year = book.get("first_publish_year")
        title = book.get("title")
        authors = book.get("author_name", [])

        if year and year > 2000:
            filtered.append(
                {
                    "title": title,
                    "authors": "; ".join(authors) if authors else "Unknown",
                    "year": year,
                }
            )

    return filtered


def save_to_csv(books):
    """
    Save filtered books to a CSV file.
    """
    with open("books.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "authors", "year"])
        writer.writeheader()
        writer.writerows(books)


def main():
    """
    Main execution flow of the script.
    """
    books = fetch_books()
    filtered_books = filter_books(books)
    save_to_csv(filtered_books)
    print(f"Saved {len(filtered_books)} books to books.csv successfully.")


if __name__ == "__main__":
    main()
