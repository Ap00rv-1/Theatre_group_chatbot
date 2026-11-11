from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Optional, List  #some schemas for the output of the model which are optional.
from langchain_core.output_parsers import PydanticOutputParser  

load_dotenv()
model = ChatMistralAI(model="mistral-small-2506")

class TheatrePlayAnalysis(BaseModel):
    title: str
    summary: str
    primary_social_issue: str
    root_cause: Optional[str] = None
    key_events: Optional[List[str]] = None
    people_affected: Optional[List[str]] = None
    important_facts: Optional[List[str]] = None
    why_issue_matters: Optional[str] = None
    long_term_impact: Optional[str] = None
    keywords: Optional[List[str]] = None

parser = PydanticOutputParser(pydantic_object=TheatrePlayAnalysis)


prompt = ChatPromptTemplate.from_messages([
     ('system', """
      Extract the social issues that can be used for a street play from the given news article.
      {format_instructions}
      """),
      ('human', "{news_article}")

])


para = input("Enter the news article to analyze: ")

final_prompt = prompt.invoke({"news_article": para,
                              "format_instructions": parser.get_format_instructions()}
                             )

response = model.invoke(final_prompt)

print(response.content)