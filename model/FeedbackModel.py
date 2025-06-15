from pydantic import BaseModel

class userFeedback(BaseModel):
    productId: int
    text: str