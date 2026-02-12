# 📚 OpenLibrary Books Fetcher

A Python script that fetches 50 books about "Python" from the OpenLibrary API, filters books published after 2000, and exports the results to a CSV file.

---

## 🎯 Purpose

This project was built to demonstrate:

- Fast learning and API integration skills
- Clean and modular Python code structure
- Proper Git workflow and documentation practices
- Basic data processing and export handling

---

## 🔎 What This Script Does

1. Sends a request to the OpenLibrary Search API  
2. Retrieves 50 books related to a search query  
3. Filters books published after the year 2000  
4. Extracts key metadata:
   - Title
   - First listed Author
   - First Publish Year  
5. Saves the filtered results into a structured CSV file  

---

## 🌐 API Reference

Endpoint used:

https://openlibrary.org/search.json

Relevant parameters:
- `q` → Search query  
- `limit` → Number of results  
- `fields` → Requested fields (title, author_name, first_publish_year)

Official documentation:  
https://openlibrary.org/dev/docs/api/search

---

## 🧩 Technologies Used

- Python 3.10+
- requests (HTTP communication)
- Built-in csv module

---

## 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd openlibrary-books
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Script

```bash
python main.py
```

---

## 📂 Output

The script generates:

```
books.csv
```


### Output Example

| title  | authors | year |
|--------|--------|------|
| Python Cookbook | Alex Martelli; David Ascher; David M. Beazley; Brian K. Jones | 2002 |
| Python Basics | David Amos; Dan Bader; Joanna Jablonski; Fletcher Heisler | 2021 |
| Python | Byron Francis | 2016 |


---

## 🛡 Error Handling

- Handles HTTP request failures
- Uses safe dictionary access to avoid KeyErrors
- Prevents crashes if optional fields are missing

---

## 🧠 Code Architecture

```
main.py
│
├── fetch_books()      → Handles API request & JSON parsing
├── filter_books()     → Applies year-based filtering logic
├── save_to_csv()      → Writes structured data to CSV
└── main()             → Controls execution flow
```

The project follows a function-based modular structure to ensure readability and maintainability.

---

## 📌 Project Structure

```
openlibrary-books/
│
├── main.py
├── books.csv
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Possible Improvements

- CLI argument support for dynamic search queries
- Logging instead of print statements
- Pagination handling for larger datasets
- Unit testing

---

## ✒️ Author
Mohammad Hasan Kamali Nikou
[GitHub Profile](https://github.com/mhkn-2007)

---

## 📄 License

Developed for mentorship selection evaluation.
