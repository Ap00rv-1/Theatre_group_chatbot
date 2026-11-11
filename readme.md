#  AI-Powered Theatre Play Analysis Chatbot

An LLM-powered chatbot that analyzes news articles and extracts important social issues, root causes, key events, and their societal impact. The extracted insights can be used as a foundation for developing meaningful and impactful street plays (Nukkad Natak).

## Overview

The Theatre Play Analysis Chatbot uses **Mistral AI** through LangChain to analyze news articles and convert unstructured news content into structured, meaningful insights.

Instead of manually researching social issues for theatre performances, users can provide a news article and receive an organized analysis highlighting the key social concerns, affected communities, important events, and long-term implications.

## Features

- **News Article Analysis:** Accepts news articles as input and analyzes their content.
- **Social Issue Identification:** Identifies the primary social issue discussed in the article.
- **Root Cause Analysis:** Extracts the underlying causes of the identified issue.
- **Key Event Extraction:** Identifies important incidents and developments.
- **Affected Communities:** Highlights the individuals or communities impacted.
- **Societal Impact:** Explains why the issue matters and its potential long-term consequences.
- **Keyword Extraction:** Generates relevant keywords for further research and creative development.
- **Structured Output:** Uses Pydantic schemas to define a consistent JSON-compatible response structure.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Mistral AI | Large Language Model |
| LangChain | LLM integration and prompt management |
| Pydantic | Structured output schema |
| python-dotenv | Environment variable management |

## Project Structure

```text
Insan(e)iyat/
│
├── .venv/                  # Python virtual environment
├── .env                    # API credentials (not committed)
├── core.py                 # Main chatbot implementation
├── UIcore.py               # Additional UI-related module
├── requirements.txt        # Project dependencies
├── .gitignore              # Git ignored files
└── README.md               # Project documentation
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Insan(e)iyat
```

### 2. Create a Virtual Environment

Using `uv`:

```bash
uv venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

Alternatively:

```bash
pip install -r requirements.txt
```

### 4. Configure API Credentials

Create a `.env` file in the project root directory:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

Get your API key from the [Mistral AI Console](https://console.mistral.ai/).

**Important:** Never upload your `.env` file or expose your API credentials publicly.

### 5. Run the Chatbot

```bash
python core.py
```

Enter a news article when prompted.

## 🧠 How It Works

The chatbot follows a simple LLM-powered processing pipeline:

1. **Input:** The user provides a news article.
2. **Prompt Engineering:** LangChain constructs a system prompt instructing the model to identify social issues relevant to street theatre.
3. **LLM Processing:** Mistral Small (`mistral-small-2506`) analyzes the article.
4. **Output Structuring:** A Pydantic model defines the expected structure of the analysis.
5. **Response:** The model generates an analysis that can be used for further creative development.

### Processing Pipeline

```text
      News Article
           |
           v
    User Input (Python)
           |
           v
   LangChain Prompt Template
           |
           v
      Mistral AI LLM
           |
           v
    Social Issue Analysis
           |
           v
   Structured Analysis Schema
           |
           v
    Theatre Play Insights
```

## Output Schema

The chatbot uses a Pydantic model named `TheatrePlayAnalysis` to define the expected analysis fields.

| Field | Description |
|---|---|
| `title` | Title of the news article |
| `summary` | Brief summary of the article |
| `primary_social_issue` | Main social issue identified |
| `root_cause` | Underlying cause of the issue |
| `key_events` | Important events mentioned |
| `people_affected` | Communities or individuals affected |
| `important_facts` | Relevant facts and statistics |
| `why_issue_matters` | Social significance of the issue |
| `long_term_impact` | Potential long-term consequences |
| `keywords` | Relevant keywords for further exploration |

Some fields are optional and may be left empty if the article does not provide sufficient information.

## Objective

The ultimate objective of this project is to bridge the gap between **current social realities and meaningful street theatre**.

By transforming news articles into structured social insights, the chatbot can help theatre practitioners and creative teams:

- Discover relevant and impactful social issues.
- Understand the root causes behind societal problems.
- Identify perspectives of affected communities.
- Develop research-backed narratives for street plays.
- Create theatre that encourages awareness, discussion, and social change.

## Future Improvements

- [ ] Interactive web-based chatbot interface.
- [ ] Support for multiple news articles.
- [ ] Automatic news article URL extraction.
- [ ] Better structured JSON output validation.
- [ ] Identification of potential street-play storylines.
- [ ] Character and dialogue suggestions based on analyzed issues.
- [ ] Hindi and other regional language support.
- [ ] Export analysis into downloadable reports.

---

**Built with Python, LangChain, Pydantic, and Mistral AI.**

*Turning news into narratives. Turning narratives into social awareness.* 