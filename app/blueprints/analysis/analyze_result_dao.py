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
        
        print(f'response {response}')

        if response.data:
            return response.data  # Return the first (and only) analyze_result entry
        else:
            return None