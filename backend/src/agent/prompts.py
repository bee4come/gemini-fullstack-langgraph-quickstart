from datetime import datetime


# Get current date in a readable format
def get_current_date():
    return datetime.now().strftime("%B %d, %Y")


query_writer_instructions = """You are building a database of Feynman diagram TikZ code. 
Generate search queries that will help locate web pages containing TikZ examples
for drawing the physics process described below.

Instructions:
- Prefer a single query unless multiple are clearly necessary.
- Keep each query focused on one aspect of the process.
- Never produce more than {number_queries} queries.
- Ensure queries are diverse and mention keywords like `tikz` and `feynman diagram`.
- Queries should gather the most current information. The current date is {current_date}.

Format:
- Respond as a JSON object with the keys:
   - "rationale": short reason why these queries should return relevant TikZ code
   - "query": a list of search queries

Example:

Topic: What revenue grew more last year apple stock or the number of people buying an iphone
```json
{{
    "rationale": "To answer this comparative growth question accurately, we need specific data points on Apple's stock performance and iPhone sales metrics. These queries target the precise financial information needed: company revenue trends, product-specific unit sales figures, and stock price movement over the same fiscal period for direct comparison.",
    "query": ["Apple total revenue growth fiscal year 2024", "iPhone unit sales growth fiscal year 2024", "Apple stock price growth fiscal year 2024"],
}}
```

Context: {research_topic}"""


web_searcher_instructions = """Search the web for pages that contain TikZ code
for drawing the following particle physics process: "{research_topic}".

Instructions:
- Ensure queries gather the most up-to-date sources. Today is {current_date}.
- Look for code blocks containing `\\begin{tikzpicture}` or mentioning
  `tikz-feynman`.
- Summarize any snippets you find and include their source URLs.
- Do not fabricate code; only return what is present in the search results.

Research Topic:
{research_topic}
"""

reflection_instructions = """You are an expert assistant gathering TikZ code for Feynman diagrams. Analyse the summaries about "{research_topic}".

Instructions:
- Identify knowledge gaps or areas that need deeper exploration and generate a follow-up query. (1 or multiple).
- If provided summaries are sufficient to answer the user's question, don't generate a follow-up query.
- If there is a knowledge gap, generate a follow-up query that would help expand your understanding.
- Focus on technical details, implementation specifics, or emerging trends that weren't fully covered.

Requirements:
- Ensure the follow-up query is self-contained and includes necessary context for web search.

Output Format:
- Format your response as a JSON object with these exact keys:
   - "is_sufficient": true or false
  - "knowledge_gap": Describe what information is missing or needs clarification
  - "follow_up_queries": Write a specific question to address this gap

Example:
```json
{{
    "is_sufficient": true, // or false
    "knowledge_gap": "The summary lacks information about performance metrics and benchmarks", // "" if is_sufficient is true
    "follow_up_queries": ["What are typical performance benchmarks and metrics used to evaluate [specific technology]?"] // [] if is_sufficient is true
}}
```

Reflect carefully on the Summaries to identify knowledge gaps and produce a follow-up query. Then, produce your output following this JSON format:

Summaries:
{summaries}
"""

answer_instructions = """From the gathered summaries create a JSON object describing a Feynman diagram entry.

Required keys:
  - "topic": short title of the process
  - "reaction": LaTeX reaction string
  - "particles": list of the particles involved
  - "description": one sentence description of the process
  - "tikz": TikZ code snippet if available (leave empty string if not found)
  - "source": URL where the TikZ code was found
  - "process_type": type of the process (e.g. scattering, decay)
  - "source_type": type of the website (wikipedia, stackexchange, etc)

Only return the JSON. Use the information from the summaries and the user's request below.

User Context:
{research_topic}

Summaries:
{summaries}"""
