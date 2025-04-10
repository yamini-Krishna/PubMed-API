# PubMed API Research Paper Fetcher

A command-line application to fetch and filter research papers from PubMed, specifically identifying papers with non-academic authors.

## Project Structure
The code is neatly organized with separate files and classes, following object-oriented principles for improved maintainability and readability.
- **`pubmed_api_client.py`** - Handles API requests to fetch PubMed IDs and paper details.
- **`paper_parser.py`** - Parses XML data to extract relevant paper information.
- **`csv_exporter.py`** - Exports the extracted data to a CSV file.
- **`logger_config.py`** - Configures application logging.
- **`cli.py`** - Provides a command-line interface for interacting with the application.

## Features
- Efficiently fetches PubMed research papers based on search queries.
- Identifies papers with non-academic authors.
- Exports results to a CSV file.
- Offers debug mode for detailed logs.

## Installation
Ensure you have Python (>= 3.7) and Poetry installed. Then follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yamini-Krishna/PubMed-API.git
    cd PubMed-API
    ```
    
2. Install "requests":
    ```bash
    pip install requests
    ```

3. Locate to pubmed-api(which contains cli.py):
    ```bash
    cd pubmed-api
    ```
4. Run the script:
    ```bash
    python cli.py
    ```
    
## Usage
To run the CLI:
```bash
python cli.py "<search-query>" -f <output-file.csv> --debug
```
- `<search-query>` - Your search term for PubMed.
- `-f, --file` (optional) - Name of the output CSV file.
- `--debug` (optional) - Enable debug mode for detailed logging.

Example:
```bash
python cli.py "cancer research" -f results.csv --debug
```

## LLM and Tools Used
- **Chatgpt** - Used for learning about Pubmed API, Test pypi, and poetry
 
This project was built using the following tools and libraries:
- **Python** - https://www.python.org/
- **Poetry** (Dependency Management) - https://python-poetry.org/



