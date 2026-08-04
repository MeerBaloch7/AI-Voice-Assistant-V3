from pydantic import BaseModel


class ChatRequest(BaseModel):

    message: str


class ChatResponse(BaseModel):

    response: str


class PreferenceRequest(BaseModel):

    key: str

    value: str


class PreferenceResponse(BaseModel):

    key: str

    value: str