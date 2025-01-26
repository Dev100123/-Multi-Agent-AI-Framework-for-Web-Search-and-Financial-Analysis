# Multi-Agent AI Framework for Web Search and Financial Analysis

This project demonstrates how to utilize multiple AI agents to perform specific tasks such as web searching and financial data analysis. It combines the power of specialized AI tools and models to process data and provide meaningful outputs in a structured format.

## Features

- **Web Search Agent**: Uses DuckDuckGo to find information on the web with reliable sources.
- **Financial Agent**: Analyzes financial data, stock prices, fundamentals, and provides investment insights using `YFinanceTools`.
- **Multi-Agent Integration**: Combines both agents to provide comprehensive data, including stock analysis and company news.
- **Interactive Output**: Responses can be displayed in the terminal or the Phi Playground interface.

---

## Project Structure

- **Agents**:
  - **Web Search Agent**: Gathers information from the web.
  - **Financial Agent**: Retrieves and analyzes stock and company-related financial data.
  - **Multi-Agent**: Combines both agents for collaborative data analysis.
- **Models**:

  - The agents use advanced language models (e.g., `llama3-70b-8192`) for generating responses.

- **Tools**:
  - `DuckDuckGo`: For web searches.
  - `YFinanceTools`: For retrieving financial data like stock prices, analyst recommendations, and company news.

---

## Setup

### Prerequisites

1. **Python Environment**: Ensure Python 3.12+ is installed.
2. **Dependencies**: Install required Python packages.
   ```bash
   pip install -r requirments.txt
   ```
   **Configure Environment Variables**
3. **Windows**: setx GROQ_API_KEY <your_api_key_here>
4. **macOS/Linux**: export GROQ_API_KEY = your_api_key_here

### Configuration

**Clone the repository**
git clone <repository-url>
cd <repository-folder>

**Run the script in your terminal**
python main.py

**Optional: Run the Playground App**
python -m uvicorn playground:app --reload
