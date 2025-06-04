# Gemini LangGraph Quickstart

This project demonstrates a LangGraph-powered backend agent that gathers Feynman diagram **TikZ** snippets from the web. It generates search terms for a given particle physics process, scrapes pages for relevant code, reflects on the findings and finally outputs a structured JSON entry describing the diagram. The project showcases how to build research‑augmented conversational AI using LangGraph and Google's Gemini models.

![Gemini Fullstack LangGraph](./app.png)

## Features

- 🧠 Powered by a LangGraph agent for advanced research and conversational AI.
- 🔍 Dynamic search query generation using Google Gemini models.
- 🌐 Integrated web research via Google Search API.
- 🤔 Reflective reasoning to identify knowledge gaps and refine searches.
- 📄 Generates answers with citations from gathered sources.
- 🎨 Outputs structured JSON entries with TikZ snippets for Feynman diagrams.

## Project Structure

The project is divided into two main directories:

-   `backend/`: Contains the LangGraph/FastAPI application, including the research agent logic.

## Getting Started: Development and Local Testing

Follow these steps to get the application running locally for development and testing.

**1. Prerequisites:**

-   Python 3.8+
-   **`GOOGLE_API_KEY`**: The backend agent requires a Google Gemini API key.
    1.  Navigate to the `backend/` directory.
    2.  Create a file named `.env` by copying the `backend/.env.example` file.
    3.  Open the `.env` file and add your key: `GOOGLE_API_KEY="YOUR_ACTUAL_API_KEY"`

**2. Install Dependencies:**

**Backend:**

```bash
cd backend
pip install .
```

**3. Run the CLI Agent:**

```bash
cd backend
python -m agent.cli "<topic>"
```
The CLI prints each step of the agent and writes the final JSON output to `result.json`.

## How the Backend Agent Works (High-Level)

The core of the backend is a LangGraph agent defined in `backend/src/agent/graph.py`. It follows these steps:

![Agent Flow](./agent.png)

1.  **Generate Initial Queries:** Based on your input, it generates a set of initial search queries using a Gemini model.
2.  **Web Research:** For each query, it uses the Gemini model with the Google Search API to find relevant web pages.
3.  **Reflection & Knowledge Gap Analysis:** The agent analyzes the search results to determine if the information is sufficient or if there are knowledge gaps. It uses a Gemini model for this reflection process.
4.  **Iterative Refinement:** If gaps are found or the information is insufficient, it generates follow-up queries and repeats the web research and reflection steps (up to a configured maximum number of loops).
5.  **Finalize Answer:** Once the research is deemed sufficient, the agent synthesizes the gathered information into a coherent answer, including citations from the web sources, using a Gemini model.

## Agent Configuration

You can customize the agent by setting environment variables (or passing a
`RunnableConfig` in code). The defaults are defined in
`backend/src/agent/configuration.py`.

- `QUERY_GENERATOR_MODEL` – LLM model for generating search queries (default
  `gemini-2.0-flash`).
- `REFLECTION_MODEL` – Model used to analyse knowledge gaps (default
  `gemini-2.5-flash-preview-04-17`).
- `ANSWER_MODEL` – Model used to produce the final structured answer (default
  `gemini-2.5-pro-preview-05-06`).
- `NUMBER_OF_INITIAL_QUERIES` – How many search queries to generate initially
  (default `3`).
- `MAX_RESEARCH_LOOPS` – Maximum number of web research loops (default `2`).

Add these variables to your `.env` file to override the defaults.

## Technologies Used

- [LangGraph](https://github.com/langchain-ai/langgraph) - For building the backend research agent.
- [Google Gemini](https://ai.google.dev/models/gemini) - LLM for query generation, reflection, and answer synthesis.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details. 