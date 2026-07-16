# multi-threaded-file-search-tool

## Overview

This project is a Python-based multi-threaded file search tool that searches multiple text files concurrently for a user-specified keyword. It uses regular expressions and ThreadPoolExecutor for efficient parallel processing.

## Features
- Multi-threaded file searching
- Concurrent execution using ThreadPoolExecutor
- Regular expression (Regex) search
- Case-insensitive keyword matching
- Displays matching line numbers
- Exception handling for missing files
- Unit testing using unittest

## Technologies Used
- Python 3
- Regular Expressions (re)
- concurrent.futures.ThreadPoolExecutor
- unittest

## Project Structure
```
file_search.py
test_file_search.py
poem.txt
eassy.txt
story.txt
chapter.txt
letter.txt
README.md
```

## How to Run
Run the main program:

```bash
python file_search.py
```

Run the unit tests:

```bash
python test_file_search.py
```

## Sample Input

```
Enter the word to search: Python
```

## Sample Output

```
File: poem.txt
Line 2: Python is easy to learn.
Line 5: Python supports threading.

File: story.txt
Line 2: He wanted to learn Python.
```

## Concepts Used
- Regular Expressions (Regex)
- Concurrent Programming
- Multi-threading
- ThreadPoolExecutor
- Exception Handling
- Unit Testing

## Author
Ritesh Wagh
