from ... import supabase

class AnalyzeResultDAO():

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

        if response.data:
            return response.data[0]  # Return the first (and only) analyze_result entry
        else:
            return None
        

        
    @staticmethod
    def update_analyze_result(company_id, update_data):
        """
        Updates the analyze_result entry for a given company_id.

        Parameters:
        company_id (str): The ID of the analyze_result to update.
        update_data (dict): A dictionary containing the updated values.

        Returns:
        dict: The updated analyze_result data if successful, or None if an error occurs.
        """
        response = supabase.table("analyze_result").update(update_data).eq("company_id", company_id).execute()

        if response.data:
            return response.data[0]  # Return the updated analyze_result entry
        else:
            return None
