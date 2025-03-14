from dotenv import load_dotenv
import os
import requests


class GooglemapService():
    def __init__(self) -> None:
        load_dotenv()
        self.API_KEY = os.getenv("GOOGLE_MAP_API")
        pass
    
    def get_feedback(self, place_id: str):
        # Fetch feedback from place id in google map
        print("Hi")
        print(self.API_KEY)
        uri = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,reviews&key={self.API_KEY}"
        feedback_response = requests.get(uri)
        feedback_data = feedback_response.json()

        if "result" in feedback_data and "reviews" in feedback_data["result"]:
            print(feedback_data["result"]["reviews"])
        else:
            print("No data")
        return "Hello"
    

