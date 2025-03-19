import openai
import os
from dotenv import load_dotenv
from typing import List
from flask import jsonify

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI API client
client = openai.OpenAI(api_key=OPENAI_API_KEY)


def send_review_to_categorizer(review):
    # Create a new thread
    thread = client.beta.threads.create()

    # Categorizer Assistant ID
    ASSISTANT_ID = "asst_ZGxgQZW4fxhtalPyS3kFckAb"

    # Send message to the assistant
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=review
    )

    # Run the assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID
    )

    # Wait for the response
    while run.status in ["queued", "in_progress"]:
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    # Get the response message
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    
    # Extract the latest response
    response = messages.data[0].content[0].text.value if messages.data else "No response received."

    return response

# Example usage
'''
user_message = "Categorize this review: 'The food was cold and the service was slow.'"
response = send_review_to_ai(user_message)
'''

#  Response Example1:
'''
{
  "positive": [
    "Product/Service Quality",
    "Atmosphere/Environment"
  ],
  "negative": [
    "Customer Service"
  ]
}
'''
#  Response Example2:
'''
{
  "negative": [
    "Product/Service Quality",
    "Customer Service"
  ]
}
'''

# Here is the category types
'''
- Product/Service Quality
- Customer Service
- Pricing
- Atmosphere/Environment
- Location/Accessibility
- Suggestions
'''

def send_reviews_to_summarizer(reviews: List[str]):
    # Create a new thread
    thread = client.beta.threads.create()

    # Categorizer Assistant ID
    ASSISTANT_ID = "asst_35MwiYRkiqOhrWhtx112hQG3"

    combined_reviews = ""
    for review in reviews:
        combined_reviews += review

    # Send message to the assistant
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=combined_reviews
    )

    # Run the assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID
    )

    # Wait for the response
    while run.status in ["queued", "in_progress"]:
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    # Get the response message
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    
    # Extract the latest response
    response = messages.data[0].content[0].text.value if messages.data else "No response received."

    return response

# Example Response
'''
{
  "summary": "The salad was inadequately prepared, with large lettuce chunks and missing ingredients
        like banana peppers, olives, and tomatoes. In contrast, the service was commendable with friendly
        staff and quick food delivery.",
  "next_action": "Review and standardize salad preparation procedures and provide staff training to 
        ensure consistency, especially for to-go orders."
}
'''