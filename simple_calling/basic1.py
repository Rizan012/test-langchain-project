import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from google.genai.types import AutomaticFunctionCallingConfig

load_dotenv()
GOOGLE_GEMINI_API = os.getenv("GOOGLE_GEMINI_API")

Gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=GOOGLE_GEMINI_API,
).bind(
    automatic_function_calling=AutomaticFunctionCallingConfig(disable=True)
)

respond = Gemini_llm.invoke("what did kp oli said in the last interview for a un related program?")

print(respond.content[0]["text"])


