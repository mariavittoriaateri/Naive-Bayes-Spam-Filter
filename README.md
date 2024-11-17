# Naive Bayes Spam Filter

A Naive Bayes spam filter implemented in Python. This project was developed as the final assignment for the basic programming course in Computational Linguistics.

---

## Overview

The project consists of three main modules:  
1. **`corpus.py`**  
2. **`nb.py`**  
3. **`main.py`**

---

## Module Descriptions

### 1. `corpus.py`

This module handles data preprocessing and provides the following functions:

- **`tokenize(text)`**  
  Accepts a string (`text`) as input and returns a list of tokens.

- **`read_file(path)`**  
  - Accepts a string (`path`) as input.  
  - Opens the file at the specified path and returns the file's contents as a list of tokens.  
  - Discards the first line of the file (the email subject).

- **`read_dataset(path)`**  
  - Accepts a string (`path`) pointing to a dataset containing two directories: `ham` and `spam`.  
  - Reads all email files in these directories using `read_file`.  
  - Combines the email content into a tuple with its respective label (`"ham"` or `"spam"`).  
    Example: `(["buy", "cheap", "medications"], "spam")`.  
  - Returns a list of such training instances.

---

### 2. `nb.py`

This module contains the **`SpamFilter`** class, which manages spam filtering using token sequences processed by `corpus.py`.

**Methods:**

- **`train(self, emails)`**  
  Trains the spam filter by analyzing email statistics.  
  - **`emails`**: A list of training instances returned by `read_dataset`.

- **`classify(self, email)`**  
  Classifies an email (represented as a list of tokens) into `"spam"` or `"ham"`.  
  - **Returns**:  
    1. The spam score.  
    2. The classification result (`"spam"` or `"ham"`).

---

### 3. `main.py`

This module handles user interaction and serves as the entry point for the program.  
By running `main.py`, all functionality is exposed to the user.

---

## Program Features

1. Train a spam filter using a dataset of emails.  
2. Classify a single email as `"spam"` or `"ham"`.  
3. Batch classify an entire dataset of emails.

---

## Notes

- The original dataset used for this project (no longer available) contains two directories: `ham` and `spam`.  
  Each email file is named using the format `numericID.ham` or `numericID.spam`.
  Only a small subset of data from the ham directory are still available and can be found in `Subset_dataset_ham`.
