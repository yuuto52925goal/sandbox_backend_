from dotenv import load_dotenv
import os
import requests
from ..blueprints.feedback.feedback_dao import FeedbackDAO

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
            data = feedback_data["result"]["reviews"]
            return data
        else:
            return "No Data"
        
    def save_all_feedback(self, place_id):
        data_list = self.get_feedback(place_id)
        for data in data_list:
            FeedbackDAO.create_new_feedback(None, data["rating"], data["author_name"], data["text"], None, None, None)
    

# googleservice = GooglemapService()
# print(googleservice.get_feedback("ChIJgSylYwqaTYcRqg0630gwyY0"))