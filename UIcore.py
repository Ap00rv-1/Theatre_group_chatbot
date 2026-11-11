import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Optional, List
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

st.set_page_config(page_title="Theatre Play Analysis", page_icon="🎭", layout="centered")

st.title("🎭 Theatre Play Social Issue Analyzer")
st.caption("Extract social issues from news articles for street play (Nukkad Natak) scripting.")

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

news_article = st.text_area("Paste the news article below:", height=280, placeholder="Enter or paste the news article text here...")

analyze_clicked = st.button("Analyze Article", use_container_width=True)

if analyze_clicked:
    if news_article.strip() == "":
        st.warning("Please enter a news article to analyze.")
    else:
        with st.spinner("Analyzing article..."):
            final_prompt = prompt.invoke({
                "news_article": news_article,
                "format_instructions": parser.get_format_instructions()
            })
            response = model.invoke(final_prompt)

            try:
                result = parser.parse(response.content)
            except Exception as e:
                result = None
                st.error(f"Failed to parse structured output: {e}")
                st.text(response.content)

        if result:
            st.markdown("---")
            st.subheader(result.title)
            st.markdown(f"**Summary:** {result.summary}")
            st.markdown(f"**Primary Social Issue:** {result.primary_social_issue}")

            if result.root_cause:
                st.markdown(f"**Root Cause:** {result.root_cause}")

            if result.key_events:
                st.markdown("**Key Events:**")
                for event in result.key_events:
                    st.markdown(f"- {event}")

            if result.people_affected:
                st.markdown("**People Affected:**")
                for person in result.people_affected:
                    st.markdown(f"- {person}")

            if result.important_facts:
                st.markdown("**Important Facts:**")
                for fact in result.important_facts:
                    st.markdown(f"- {fact}")

            if result.why_issue_matters:
                st.markdown(f"**Why This Issue Matters:** {result.why_issue_matters}")

            if result.long_term_impact:
                st.markdown(f"**Long-Term Impact:** {result.long_term_impact}")

            if result.keywords:
                st.markdown("**Keywords:**")
                st.write(", ".join(result.keywords))