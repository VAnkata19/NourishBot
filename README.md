# NourishBot

**Never waste money on groceries again.** NourishBot discovers the best deals at your local supermarket, generates AI-powered recipes based on what's on sale, creates your shopping list, and sends it all straight to your inbox—all with zero effort from you.

## Overview

NourishBot is an intelligent meal planning automation system that combines web scraping, AI-powered analysis, and email delivery. Every run intelligently searches for current grocery deals, transforms them into delicious meal options using GPT/LLM reasoning, and delivers personalized recipe recommendations to your inbox. Whether you're looking to save money, eat healthier, or simply make meal planning effortless, NourishBot handles the heavy lifting.

## Short Demo

https://github.com/user-attachments/assets/aece9f85-31d6-4ff2-bc8c-d6b436378984

## Features

- **Web Scraping**: Automatically scrapes current grocery offers from ICA Supermarket
- **Smart Deal Analysis**: Uses LangChain and LLMs to identify the best grocery deals
- **Recipe Generation**: Generates 3 easy recipes based on available deals using AI
- **Shopping List Creation**: Automatically creates a consolidated shopping list for the generated meals
- **Email Integration**: Sends meal suggestions and shopping lists directly to your email via Gmail API

## How It Works

1. **Scraper** (`modules/scraper.py`): Uses Selenium to scrape grocery store offers from ICA Supermarket
2. **Reasoning** (`modules/reasoning.py`): Leverages LangChain with LLM (OpenAI or Ollama) to:
   - Analyze deals and filter relevant meal ingredients
   - Generate creative meal recipes
   - Create consolidated shopping lists
3. **Gmail Integration** (`modules/gmail_api.py`): Sends results via Gmail API
4. **Main Script** (`main.py`): Orchestrates the entire workflow

## Installation

### Prerequisites
- Python 3.11+
- Chrome WebDriver (for Selenium)
- Google API credentials (for Gmail integration)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Langchain-Meal-Generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or using uv:
```bash
uv pip install -e .
```

3. Configure Google Gmail API:
   - Create a project in Google Cloud Console
   - Enable the Gmail API
   - Download your credentials and save as `credentials.json` in the project root
   - Run the script once to authenticate (it will create `token.json`)

## Usage

### Before Running

**Important:** Update the email addresses in `main.py` before running:
- Open `main.py` and replace `"From"` with your sender email address
- Replace `"To"` with the recipient email address

Run the main script:
```bash
python main.py
```

The script will:
1. Scrape current grocery deals from ICA Supermarket
2. Analyze deals to find the best meal ingredients
3. Generate 3 easy meal recipes
4. Create a shopping list for those meals
5. Send both the meal suggestions and shopping list to your email

## Project Structure

```
.
├── main.py                 # Entry point
├── modules/
│   ├── __init__.py
│   ├── scraper.py         # Web scraping logic (Selenium + BeautifulSoup)
│   ├── reasoning.py       # LLM-based deal analysis and recipe generation
│   └── gmail_api.py       # Gmail API integration
├── pyproject.toml         # Project configuration and dependencies
├── credentials.json       # Google API credentials (not tracked)
├── token.json            # Gmail API token (not tracked)
└── README.md             # This file
```

## Dependencies

- **beautifulsoup4**: HTML parsing for scraped content
- **selenium**: Browser automation for web scraping
- **langchain**: LLM framework for reasoning and recipe generation
- **langchain-openai**: OpenAI integration for LangChain
- **langchain-ollama**: Ollama integration (local LLMs)
- **google-api-python-client**: Gmail API client
- **google-auth-oauthlib**: Google authentication
- **python-dotenv**: Environment variable management

## Configuration

Create a `.env` file in the project root to configure:
```env
OPENAI_API_KEY=your_openai_key
OLLAMA_BASE_URL=http://localhost:11434  # If using Ollama
```

## Notes

- The scraper targets ICA Supermarket's offers page. Update the URL in `scraper.py` to target different stores
- The script uses LLM reasoning to ensure meal recipes are practical and ingredient-based
- Email credentials are handled securely through Google OAuth 2.0

## License

This project is open source and available under the MIT License.
