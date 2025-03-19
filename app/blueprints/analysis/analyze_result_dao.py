from ... import supabase
import datetime

class AnalyzeResultDAO():

    # @staticmethod
    # def create_new_analyze_result(created_date, rate, display_name, comment, update_at, reply, company_id):
    #     if isinstance(update_at, datetime.time):
    #         update_at = update_at.isoformat()
    #     elif isinstance(update_at, str):
    #         update_at = datetime.datetime.fromisoformat(update_at).time().isoformat()

    #     if isinstance(created_date, datetime.time):
    #         created_date = created_date.isoformat()
    #     elif isinstance(created_date, str):
    #         created_date = datetime.datetime.fromisoformat(created_date).time().isoformat()

    #     feedback_data = {
    #         "created_at": created_date,
    #         "update_at": update_at,
    #         "rate": rate,
    #         "display_name": display_name,
    #         "comment": comment,
    #         "reply": reply,
    #         "company_id": company_id
    #     }
    #     feedback_data = {k: v for k, v in feedback_data.items() if v is not None}
    #     print(feedback_data)
    #     response = supabase.table("feedback").insert(feedback_data).execute() 
    #     print(response)

    @staticmethod
    def get_analyze_result_by_id(analyze_result_id):
        """
        Retrieves analyze_result from the database based on the analyze_result ID.

        Parameters:
        analyze_result_id (str): The ID of the analyze_result to retrieve.

        Returns:
        dict: The analyze_result data if found, or None if not found.
        """
        response = supabase.table("analyze_result").select("*").eq("id", analyze_result_id).execute()
        
        if response.data:
            return response.data[0]  # Return the first (and only) feedback entry
        else:
            return None

    @staticmethod
    def get_analyze_result_by_company_id(company_id):
        """
        Retrieves analyze_result from the database based on the analyze_result ID.

        Parameters:
        company_id (str): The ID of the analyze_result to retrieve.

        Returns:
        dict: The analyze_result data if found, or None if not found.
        """
        response = supabase.table("analyze_result").select("*").eq("company_id", company_id).execute()
        
        print(f'response {response}')

        if response.data:
            return response.data  # Return the first (and only) analyze_result entry
        else:
            return None