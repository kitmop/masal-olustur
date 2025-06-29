from pydantic import BaseModel

class StoryRequest(BaseModel):
    karakter: str
    tema: str
    yas: int
    mekan: str
    ders: str
    uzunluk: int
