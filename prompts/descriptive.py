    def get_descriptive_prompt(self, schema):
        return """## Task:

You are an expert in Business Intelligence (BI) and Data Analytics. Your objective is to generate **descriptive analytical questions** that help uncover **patterns, summaries, trends, and key performance indicators** from a business dataset.

## What Are Descriptive Analytical Questions?

Descriptive questions focus on understanding **what happened**, providing summaries of historical data such as totals, averages, comparisons, trends over time, and breakdowns by different business dimensions.

Descriptive questions **do NOT explore reasons**, drivers, impacts, correlations, or causality. Avoid "what influences", "why", "what causes", "impact of", etc.

## How Should These Questions Be Framed?

1. **Use business-friendly language** — business users do not refer to table or column names in queries.
2. **Avoid explicit mentions of table/column names** in the question text.
3. **Ensure each question reflects natural business thinking**.
4. **Questions should be self-contained and clear**, so they can be answered directly using the dataset.

## Complexity Levels

1. **Basic** – Simple aggregations, trends, and summaries  
   *Example: “What was the total revenue last year?”*

2. **Intermediate** – Multi-dimensional summaries or comparisons  
   *Example: “How did sales vary across different regions and product categories?”*

3. **Advanced** – More granular breakdowns, trend analysis over time, or customer segmentation  
   *Example: “What are the top customer segments contributing to quarterly growth in product sales?”*

## Instructions:

1. Generate exactly **9 descriptive questions** in total : **3 Basic**, **3 Intermediate**, and **3 Advanced**.
2. Each question should be **fully answerable using the given dataset schema**.
3. Avoid questions that require external data or are ambiguous.
4. Use specific **business contexts** like customer behavior, product sales, regional trends, time-based comparisons, etc.
5. **Avoid mentioning actual table or column names in the question text.**
6. **Enclose each question within `<question>...</question>` tags.**
7. Return a clean, structured output in JSON format with each question and its complexity level.
8. **Again, do not return anything except the raw JSON array. Avoid any headings, notes, or boxed formats.**
9. All 9 questions must be returned in a **single flat JSON array**.
10. Do **not create multiple arrays or group questions by complexity** — just one array with 9 JSON objects.

Ensure:

1. Each question must be fully answerable using only the columns and data types explicitly provided in the schema.
2. Do not invent additional columns or assume missing information.
3. Only use the column names and sample values shown in the schema.
4. If a question depends on unavailable data, skip it.
5. Do not make assumptions about data availability or granularity (e.g., specific time periods, locations, customer types, etc.) unless clearly stated in the schema.
- Prefer: “...across time”, “by region”, “per category”
- Avoid: “last year”, “premium customers”, “city-wise” if such details are not explicitly part of the dataset.

## Dataset Schema:

""" + schema + """

## Output Format:

```json
[
  {
    "question": "<question_text>",
    "complexity": "Basic | Intermediate | Advanced"
  }
]

Return a single JSON array named `questions`, not multiple arrays."""
