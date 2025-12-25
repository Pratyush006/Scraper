def get_reviews(url):
    """
    Returns sample review data in the required format.
    Multiple reviews are included to simulate real-world data.
    """

    # TrustRadius sample reviews
    if "trustradius" in url:
        return [
            {
                "title": "Excellent enterprise solution",
                "review": "Highly scalable and reliable for large teams",
                "date": "2024-07-10",
                "rating": "5",
                "reviewer": "Enterprise User"
            },
            {
                "title": "Strong analytics features",
                "review": "Provides detailed insights and reporting",
                "date": "2024-07-18",
                "rating": "4",
                "reviewer": "Data Analyst"
            },
            {
                "title": "Good but complex",
                "review": "Powerful tool but requires learning curve",
                "date": "2024-06-30",
                "rating": "3",
                "reviewer": "IT Manager"
            },
            {
                "title": "Reliable performance",
                "review": "Stable product with minimal downtime",
                "date": "2024-07-25",
                "rating": "5",
                "reviewer": "Operations Lead"
            },
            {
                "title": "Customer support could be better",
                "review": "Support team is helpful but response time is slow",
                "date": "2024-07-02",
                "rating": "3",
                "reviewer": "Project Manager"
            }
        ]

    # G2 / Capterra sample reviews
    return [
        {
            "title": "Great product",
            "review": "Easy to use and improves team productivity",
            "date": "2024-06-15",
            "rating": "5",
            "reviewer": "Verified User"
        },
        {
            "title": "Good but expensive",
            "review": "Features are good but pricing is high",
            "date": "2024-06-28",
            "rating": "4",
            "reviewer": "Anonymous"
        },
        {
            "title": "Needs improvement",
            "review": "Customer support response is slow",
            "date": "2024-07-05",
            "rating": "3",
            "reviewer": "Verified User"
        },
        {
            "title": "Average experience",
            "review": "Product is okay but lacks customization",
            "date": "2024-07-20",
            "rating": "3",
            "reviewer": "Small Business Owner"
        },
        {
            "title": "Easy onboarding",
            "review": "Getting started was quick and simple",
            "date": "2024-07-12",
            "rating": "4",
            "reviewer": "Startup Founder"
        },
        {
            "title": "Missing advanced features",
            "review": "Works well but lacks some advanced capabilities",
            "date": "2024-06-22",
            "rating": "3",
            "reviewer": "Product Manager"
        }
    ]


def assign_topic(review_text):
    """
    Assigns a topic to a review based on keywords.
    Used for simple trend analysis.
    """

    review_text = review_text.lower()

    if "price" in review_text or "expensive" in review_text:
        return "Pricing Issue"
    elif "support" in review_text:
        return "Customer Support Issue"
    elif "performance" in review_text or "stable" in review_text:
        return "Performance"
    elif "easy" in review_text or "onboarding" in review_text:
        return "Ease of Use"
    elif "feature" in review_text:
        return "Feature Request"
    else:
        return "General Feedback"
