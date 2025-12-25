# Review Scraper and Trend Analysis

## About the Project
This project is a Python script that analyzes product reviews from popular SaaS review platforms such as **G2**, **Capterra**, and **TrustRadius**.  
The script takes user input, filters reviews based on a given date range, and generates insights in the form of a topic-wise trend table.

The main goal of this project is to show how review data can be structured, filtered, and analyzed to identify common user feedback themes.

---

## What the Script Does
- Takes company name, review source, and date range as input
- Supports multiple review platforms:
  - G2
  - Capterra
  - TrustRadius (bonus)
- Filters reviews based on the provided start and end dates
- Organizes reviews into a clean JSON format
- Assigns topics to reviews using simple keyword logic
- Creates a topic vs frequency trend table
- Prints the trend table in the terminal
- Saves the final output in a JSON file

---

## Input Details
The script asks for the following inputs:
- **Company Name** – Name of the product/company
- **Source** – `g2`, `capterra`, or `trustradius`
- **Start Date** – Beginning of the review period (YYYY-MM-DD)
- **End Date** – End of the review period (YYYY-MM-DD)

---

## Output
The output is saved in:

output/sample_reviews.json

### The JSON file contains:
- Company name
- Review source
- Selected date range
- Topic trend table (topic and frequency)
- List of filtered reviews with:
  - Title
  - Review text
  - Date
  - Rating
  - Reviewer name
  - Assigned topic

---

## Topic Trend Table
The topic trend table shows how many times each type of feedback appears within the selected date range.

Example topics:
- Pricing Issue
- Customer Support Issue
- Performance
- Ease of Use
- General Feedback

This makes it easy to understand which areas users talk about the most.

---

## Error Handling
The script handles common issues such as:
- Invalid source names
- Incorrect date format
- Out-of-range dates
- No matching reviews after filtering

Clear messages are shown instead of the program crashing.

---

## Note on Review Data
Platforms like G2 and Capterra restrict automated scraping.  
To avoid unreliable behavior and blocking issues, sample review data is used to demonstrate the full logic of the project.

All processing steps — input validation, filtering, topic classification, trend generation, and output formatting — are fully implemented and can be extended to real data if access is permitted.

---

## How to Run the Project

### Step 1: Install dependencies
pip install -r requirements.txt


### Step 2: Run the script
python scraper.py

### Step 3: Enter inputs when prompted
Example:
Enter company name: slack
Enter source (g2, capterra, or trustradius): g2
Enter start date: 2024-06-01
Enter end date: 2024-07-31


---

## Technologies Used
- Python
- JSON
- Built-in Python libraries (datetime, collections, os)

---

## Summary
This project demonstrates a complete review analysis workflow, starting from user input and ending with structured insights. It focuses on clean data handling, meaningful aggregation, and practical trend analysis while respecting real-world platform limitations.
