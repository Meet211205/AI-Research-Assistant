# AI Research Assistant

An autonomous AI research assistant built with LangChain and a locally hosted Mistral 7B model through Ollama. It accepts a research topic, uses Wikipedia and web search tools, generates a structured research report, extracts sources, and can save the report to a text file.

## Features

- Local Mistral 7B inference through Ollama
- LangChain agent architecture
- Wikipedia research for definitions, background, history, and established information
- DuckDuckGo web search for additional and recent information
- Structured research reports
- Source extraction
- Optional TXT report saving

## Tech Stack

Python, LangChain, LangChain Ollama, Ollama, Mistral 7B, Wikipedia, DuckDuckGo Search, python-dotenv

## Project Structure

```text
AI-Research-Assistant/
├── main.py
├── tools.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

## How It Works

```text
User Topic
   ↓
LangChain Agent
   ↓
Wikipedia + DuckDuckGo
   ↓
Mistral 7B via Ollama
   ↓
Structured Research Report
   ↓
Source Extraction
   ↓
Optional TXT Save
```

## Requirements

- Python 3.10+ recommended
- Ollama installed and running
- Mistral 7B available locally
- Internet connection for web research

## Installation

### 1. Clone

```bash
git clone https://github.com/YOUR_USERNAME/AI-Research-Assistant.git
cd AI-Research-Assistant
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare Mistral with Ollama

```bash
ollama pull mistral:7b
```

Verify:

```bash
ollama list
```

### 5. Run

```bash
python main.py
```

Then enter a topic, such as `Artificial Intelligence`.

## Report Format

The agent is instructed to produce an approximately 800–1500 word research report when sufficient information is available, with relevant sections such as Introduction, Overview, Background, History, Key Features, Concepts, Types, How It Works, Applications, Examples, Advantages, Limitations, Current Developments, Future Scope, Conclusion, and Sources.

## Important Notes

- The application expects the Ollama model name `mistral:7b`.
- Wikipedia and DuckDuckGo research require internet access.
- `.env` is ignored to protect secrets.
- Generated `research_output.txt` is ignored by Git.

## Future Improvements

- Streamlit or FastAPI interface
- PDF and Markdown export
- Persistent research history
- Citation validation
- Multi-agent research workflow
- Source ranking and deduplication
- RAG for uploaded documents
- Configurable model settings

## License

For educational and portfolio use. Add an appropriate open-source license if you plan to distribute the project publicly.
