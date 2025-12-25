
 Review Intelligence & Trend Analyzer

 Project Overview

This project is a **Python-based review analysis engine** that transforms raw SaaS product reviews into **actionable insights**.
It simulates data extraction from leading review platforms—**G2**, **Capterra**, and **TrustRadius**—and performs **date-based filtering, topic classification, and trend analysis**.

The core objective is to demonstrate how unstructured user feedback can be converted into **structured intelligence** that helps teams understand customer sentiment at scale.

 Why This Project Matters

* Companies receive thousands of reviews but struggle to extract **patterns**
* Manual analysis is slow and biased
* This script showcases a **scalable and automated approach** to identifying user pain points and strengths

This project focuses on **logic, data modeling, and insight generation**, not just scraping.

 Key Features

✔ Interactive user-driven inputs
✔ Multi-platform review support
✔ Robust date-range filtering
✔ Topic classification using keyword heuristics
✔ Trend analysis via frequency aggregation
✔ Clean, structured JSON output
✔ Graceful error handling and validations



 How It Works (High-Level Flow)

1. User provides company name, review source, and date range
2. Review data is loaded (sample dataset for reliability)
3. Reviews are filtered based on time period
4. Each review is analyzed and assigned a **feedback topic**
5. A **topic-frequency trend table** is generated
6. Final insights are displayed in the terminal and saved as JSON



 Input Parameters

The script prompts the user for:

* **Company Name**
* **Review Platform** (`g2`, `capterra`, `trustradius`)
* **Start Date** (`YYYY-MM-DD`)
* **End Date** (`YYYY-MM-DD`)


Output Structure

All results are saved in:


output/sample_reviews.json


 Output Includes:

* Metadata (company, platform, date range)
* Topic-wise trend summary
* Filtered review list containing:

  * Review title
  * Review text
  * Review date
  * Rating
  * Reviewer name
  * Auto-assigned topic

 Topic Trend Insights

The trend table highlights **what users talk about most**, such as:

* Pricing Issues
* Customer Support
* Performance
* Ease of Use
* General Feedback

This enables quick identification of **product strengths and improvement areas**.

## 🛡 Error Handling & Validation

The script safely handles:

* Invalid platform inputs
* Incorrect date formats
* Date ranges with no matching reviews
* Unsupported sources

User-friendly messages ensure **smooth execution without crashes**.


 Note on Data Ethics

Since platforms like G2 and Capterra limit automated scraping, **mock review datasets** are used.
This ensures:

* Ethical compliance
* Stable execution
* Focus on **core data processing logic**

The architecture is extensible and can support real APIs if access is granted.


 How to Run

1️⃣ Install Dependencies

bash
pip install -r requirements.txt

2️⃣ Execute Script

```bash
python scraper.py
```

 3️⃣ Sample Input

```text
Company Name: Slack  
Source: g2  
Start Date: 2024-06-01  
End Date: 2024-07-31
```

---
Tech Stack

* **Python**
* **JSON**
* `datetime`, `collections`, `os`


