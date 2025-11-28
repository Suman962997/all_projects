from pydantic import BaseModel
from typing import Optional

class PDFTableUpdate(BaseModel):
    section: Optional[str]
    title: Optional[str]
    categoryNo: Optional[str]
    subtitle: Optional[str]
    question_no: Optional[str]
    question: Optional[str]
    answer: Optional[str]