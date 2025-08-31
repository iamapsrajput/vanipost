# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

vanipost is a Python-based social media automation tool that fetches news headlines and generates tweets using OpenAI's GPT models. The project follows a modular pipeline architecture with separate components for news fetching, tweet generation, scheduling, and dashboard monitoring.

## Development Setup

### Prerequisites
- Python 3.11 (managed via pyenv)
- Poetry for dependency management

### Environment Setup
```bash
# Install dependencies and create virtual environment
poetry install

# Activate virtual environment
poetry shell
```

### Environment Variables
Create a `.env` file in the root directory with:
```
NEWS_API_KEY=your_newsapi_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## Common Commands

### Running the Main Pipeline
```bash
# Run the complete news-to-tweet pipeline
poetry run python run_pipeline.py
```

### Running Individual Components
```bash
# Test news fetching only
poetry run python news_fetcher/fetch_news.py

# Test tweet generation only
poetry run python tweet_generator/generate_tweet.py

# Run dashboard (when implemented)
poetry run python dashboard/flask_app.py
```

### Development and Testing
```bash
# Run with different news categories
poetry run python -c "from news_fetcher.fetch_news import fetch_top_headlines; print(fetch_top_headlines('us', 'business'))"

# Test tweet generation with custom headline
poetry run python -c "from tweet_generator.generate_tweet import generate_tweet; print(generate_tweet('Your custom headline here'))"

# Add new dependencies
poetry add package_name

# Add development dependencies
poetry add --group dev package_name

# Update dependencies
poetry update
```

## Code Architecture

### Core Components

**news_fetcher/**: News API integration
- `fetch_news.py`: Main news fetching logic using NewsAPI
- Fetches top headlines by country and category
- Returns list of article titles for tweet generation

**tweet_generator/**: OpenAI integration for content generation  
- `generate_tweet.py`: GPT-3.5-turbo integration for tweet creation
- Configurable tone/style parameters
- Handles OpenAI API calls and response parsing

**scheduler/**: Tweet scheduling functionality
- `schedule_tweet.py`: Cron job setup and tweet timing (placeholder)

**dashboard/**: Web interface for monitoring
- `flask_app.py`: Flask-based dashboard (placeholder)

**utils/**: Shared utilities
- `config.py`: Configuration management (placeholder)
- `api_clients.py`: Shared API client utilities (placeholder)  
- `logger.py`: Logging utilities (placeholder)

### Pipeline Flow
1. `run_pipeline.py` orchestrates the main workflow
2. News fetcher retrieves headlines from NewsAPI
3. Tweet generator creates social media content using OpenAI
4. Results are printed to console (scheduling/posting not yet implemented)

### Key Dependencies
- `requests`: HTTP client for NewsAPI integration
- `openai`: Official OpenAI Python client for GPT integration
- `python-dotenv`: Environment variable management
- `flask`: Web framework for dashboard (when implemented)
- `poetry`: Modern dependency management and packaging tool

### Configuration Pattern
- Python 3.11 version managed via pyenv (see `.python-version`)
- Dependencies managed via Poetry (see `pyproject.toml` and `poetry.lock`)
- Virtual environment created in project directory as `.venv`
- Environment variables loaded via `python-dotenv`
- API keys stored in `.env` file (never committed)
- Modular design allows easy swapping of news sources or AI models

## Development Notes

### API Integration
- NewsAPI requires valid API key for headline fetching
- OpenAI API key needed for tweet generation
- Both APIs have rate limits - implement backoff strategies for production use

### Module Structure  
- Each component is self-contained with `__init__.py` files
- Individual modules can be run standalone for testing
- Main pipeline in `run_pipeline.py` imports and orchestrates all components

### Extensibility Points
- News sources can be expanded beyond NewsAPI
- Tweet generation prompts are customizable via function parameters
- Scheduling system designed to support multiple platforms
- Dashboard framework ready for monitoring and control features
