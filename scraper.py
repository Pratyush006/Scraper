import json
import os
from datetime import datetime
from collections import defaultdict
from utils import get_reviews, assign_topic

# ---------------- USER INPUTS ----------------
company = input("Enter company name (example: slack): ")
source = input("Enter source (g2, capterra, or trustradius): ").lower()
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# ---------------- DATE VALIDATION ----------------
try:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
except ValueError:
    print("❌ Invalid date format. Use YYYY-MM-DD")
    exit()

# ---------------- SOURCE URL ----------------
if source == "g2":
    url = f"https://www.g2.com/products/{company}/reviews"
elif source == "capterra":
    url = f"https://www.capterra.com/p/{company}/reviews"
elif source == "trustradius":
    url = f"https://www.trustradius.com/products/{company}/reviews"
else:
    print("❌ Invalid source")
    exit()

# ---------------- FETCH REVIEWS ----------------
reviews = get_reviews(url)

# ---------------- FILTER + TOPIC ANALYSIS ----------------
filtered_reviews = []
topic_counter = defaultdict(int)

for r in reviews:
    review_date = datetime.strptime(r["date"], "%Y-%m-%d")

    if start <= review_date <= end:
        topic = assign_topic(r["review"])
        r["topic"] = topic
        filtered_reviews.append(r)
        topic_counter[topic] += 1

# ---------------- CONVERT TO TABLE FORMAT ----------------
trend_table = []
for topic, count in topic_counter.items():
    trend_table.append({
        "Topic": topic,
        "Frequency": count
    })

# ---------------- SAVE OUTPUT ----------------
output_data = {
    "company": company,
    "source": source,
    "date_range": {
        "start": start_date,
        "end": end_date
    },
    "trend_table": trend_table,
    "reviews": filtered_reviews
}

os.makedirs("output", exist_ok=True)

with open("output/sample_reviews.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, indent=4)

# ---------------- PRINT TABLE ----------------
print("\n📊 TOPIC TREND TABLE")
print("-" * 45)
print(f"{'Topic':30} Frequency")
print("-" * 45)

for row in trend_table:
    print(f"{row['Topic']:30} {row['Frequency']}")

print("\n✅ Reviews and trend table saved successfully in output/sample_reviews.json")
