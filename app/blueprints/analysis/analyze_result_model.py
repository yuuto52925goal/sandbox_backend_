from pydantic import BaseModel

class AnalyzeResult(BaseModel):
    action: str
    company_id: int
    id: int
    negative_atmosphere: int
    negative_location: int
    negative_price: int
    negative_quality: int
    negative_service: int
    negative_suggestions: int
    positive_atmosphere: int
    positive_location: int
    positive_price: int
    positive_quality: int
    positive_service: int
    positive_suggestions: int
    summarize: str
