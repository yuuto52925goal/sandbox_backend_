from .. import supabase
import datetime

class FeedbackDAO():
    def create_new_feedback(created_date, rate, display_name, comment, update_at, reply, company_id):
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