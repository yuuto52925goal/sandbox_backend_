from ... import supabase
import datetime

class FeedbackDAO():

    @staticmethod
    def create_new_feedback(created_date, rate, display_name, comment, update_at, reply, company_id):
        # If it is exsit, don't duplicate
        if isinstance(update_at, datetime.time):
            update_at = update_at.isoformat()
        elif isinstance(update_at, str):
            update_at = datetime.datetime.fromisoformat(update_at).time().isoformat()

        if isinstance(created_date, datetime.time):
            created_date = created_date.isoformat()
        elif isinstance(created_date, str):
            created_date = datetime.datetime.fromisoformat(created_date).time().isoformat()

        feedback_data = {
            "created_at": created_date,
            "update_at": update_at,
            "rate": rate,
            "display_name": display_name,
            "comment": comment,
            "reply": reply,
            "company_id": company_id
        }
        feedback_data = {k: v for k, v in feedback_data.items() if v is not None}
        print(feedback_data)
        response = supabase.table("feedback").insert(feedback_data).execute() 
        print(response)

    @staticmethod
    def get_feedback_by_id(feedback_id):
        """
        Retrieves feedback from the database based on the feedback ID.

        Parameters:
        feedback_id (str): The ID of the feedback to retrieve.

        Returns:
        dict: The feedback data if found, or None if not found.
        """
        response = supabase.table("feedback").select("*").eq("id", feedback_id).execute()
        
        if response.data:
            return response.data[0]  # Return the first (and only) feedback entry
        else:
            return None

    @staticmethod
    def get_feedback_by_company_id(company_id):
        """
        Retrieves feedback from the database based on the feedback ID.

        Parameters:
        company_id (str): The ID of the feedback to retrieve.

        Returns:
        dict: The feedback data if found, or None if not found.
        """
        response = supabase.table("feedback").select("*").eq("company_id", company_id).execute()
        
        if response.data:
            return response.data[0]  # Return the first (and only) feedback entry
        else:
            return None
    
    @staticmethod
    def get_company_by_place_id(place_id: str):
        response = supabase.table('company').select('id').eq("placeId", place_id).execute()
        print(response)

        if response.data: 
            return response.data[0]
        else: 
            print("data None")
            return None