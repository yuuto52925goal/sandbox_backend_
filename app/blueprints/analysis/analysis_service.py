from ..feedback.feedback_dao import FeedbackDAO
from .analyze_result_dao import AnalyzeResultDAO
from .chatgpt import send_review_to_categorizer, send_reviews_to_summarizer
import json

class AnalysisService:
    def categorize_feedbacks(self, company_id):
        """
        Get All Feedback data that is tagged with Company ID from Supabase.
        Send them to chatgpt to categorize and summarize.
        Store the result in Analyze result.

        Return None
        """

        feedbacks = FeedbackDAO.get_feedback_by_company_id(company_id)
        analyze_result = AnalyzeResultDAO.get_analyze_result_by_company_id(company_id)

        categories_dict = {
            "positive":{   
                "Product/Service Quality": "positive_quality", 
                "Customer Service": "positive_service", 
                "Pricing": "positive_price", 
                "Atmosphere/Environment": "positive_atmosphere",
                "Location/Accessibility": "positive_location", 
                "Suggestions": "positive_suggestions"
                },
            "negative": {
                "Product/Service Quality": "negative_quality", 
                "Customer Service": "negative_service", 
                "Pricing": "negative_price", 
                "Atmosphere/Environment": "negative_atmosphere",
                "Location/Accessibility": "negative_location", 
                "Suggestions": "negative_suggestions"
                }
            }
        
        for feedback in feedbacks:
            comment = feedback["comment"]

            categorizer_result = send_review_to_categorizer(comment)
            categorizer_result = json.loads(categorizer_result)

            if "positive" in categorizer_result: # Check if the result contains any postive category
                for category in categories_dict["positive"]:
                    if category in categorizer_result["positive"]: # Check if the category exists

                        column_name = categories_dict["positive"][category]
                        analyze_result[column_name] += 1

            if "negative" in categorizer_result:
                for category in categories_dict["negative"]:
                    if category in categorizer_result["negative"]:

                        column_name = categories_dict["negative"][category]
                        analyze_result[column_name] += 1

        AnalyzeResultDAO.update_analyze_result(analyze_result["company_id"], analyze_result)

        return None
    
    def summarize_feedbacks(self, company_id):
        """
        Get all Feedback data tagged with Company ID from Supabase.
        Send them to ChatGPT to summarize.
        Store the summarized result in AnalyzeResult.

        Return None
        """
        
        feedbacks = FeedbackDAO.get_feedback_by_company_id(company_id)
        analyze_result = AnalyzeResultDAO.get_analyze_result_by_company_id(company_id)

        all_comments = []

        # Store all feedbacks in a single array
        for feedback in feedbacks:
            all_comments.append(feedback["comment"])

        summarizer_result = send_reviews_to_summarizer(all_comments)
        summarizer_result = json.loads(summarizer_result)


        if "next_action" in summarizer_result:
            action_suggestion = summarizer_result["next_action"]
        if "summary" in summarizer_result:
            feedback_summary = summarizer_result["summary"]
            

        # Store the summarized results in AnalyzeResult
        analyze_result["action"] = action_suggestion
        analyze_result["summarize"] = feedback_summary

        AnalyzeResultDAO.update_analyze_result(analyze_result["company_id"], analyze_result)

        return None
