# Business Feedback Categorization Project

## Purpose

This project aims to visualize and categorize the different types of problems faced by businesses based on reviews found on Google Maps. The goal is to categorize reviews, count the feedback in each category, and generate insightful reports that can help businesses address customer concerns. Additionally, it provides notifications for new reviews and may suggest solutions based on feedback trends.

## Features

### Must Have
- **Categorize and Count Feedback**: Automatically categorize each review into predefined categories (Product/Service Quality, Customer Service, Pricing, Atomosphere/Environment, Location/Accessibility, Suggestions) and count the number of feedback items in each category.

### Should Have
- **Store Comments**: Keep a record of all customer comments, allowing users to view detailed feedback history.
- **Weekly or Monthly Reports**: Generate periodic reports (weekly or monthly) summarizing feedback across categories, offering a high-level view of customer sentiment.
- **New Feedback Notifications**: Notify the user when new feedback or reviews are posted on the Google Maps business listing.
  
### Nice to Have
- **Analyze Feedback and Suggest Solutions**: Based on categorized feedback, the system can analyze trends and suggest solutions for issues such as improving customer service, product quality, or pricing strategies.
- **Keyword Trend Gueeser**: Based on the all feedbacks, they system can analyze what specific thing they mention in a positive and a negative feedback.

## Tech Stack
- **Frontend**: [Next.js](https://nextjs.org/) with [TypeScript](https://www.typescriptlang.org/)
- **Backend**: [Flask](https://flask.palletsprojects.com/)
- **Database**: [Supabase](https://supabase.io/)
  

## Data Model Classes

**Company Data**
| Field   | Type   |
| ------- | -----  |
| id      | int    |
| name    | String |


**Feedback Data**
| Field        | Type   |
| -------      | -----  |
| id           |  int   |
| company_id   |  int   |
| display_name | String |
| star_rating  | int    |
| comment      | String |
| created_at   | String/Date |
| updated_at   | String/Date |
| reply        | String |


**Company Feedback**
| Field   | Type   |
| ------- | -----  |
| id      |  int   |
| company_id  | id |


## Install Dependencies
In the terminal, 
1, "python3 -m venv venv" to download python
2, "source venv/bin/activate"
3, "pip install -r requirements.txt" to install all required dependencies.
4, 


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
