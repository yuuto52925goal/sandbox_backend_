from dotenv import load_dotenv
import os
import requests
from ..dataaccess.feedback_dao import FeedbackDAO

class GooglemapService():
    def __init__(self) -> None:
        load_dotenv()
        self.API_KEY = os.getenv("GOOGLE_MAP_API")
        pass
    
    def get_feedback(self, place_id: str):
        # Fetch feedback from place id in google map
        uri = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,reviews&key={self.API_KEY}"
        feedback_response = requests.get(uri)
        feedback_data = feedback_response.json()

        if "result" in feedback_data and "reviews" in feedback_data["result"]:
            print(feedback_data["result"]["reviews"])
            data = feedback_data["result"]["reviews"][0]
            FeedbackDAO.create_new_feedback(None, data["rating"], data["author_name"], data["text"], None, None, None)
        else:
            print("No data")
        return "Hello"
    

