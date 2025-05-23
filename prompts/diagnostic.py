    def get_diagnostic_prompt(self, schema):
        return """## Task:

You are an expert in Business Intelligence (BI) and Data Analytics. Your objective is to generate **diagnostic analytical questions** that help uncover **underlying reasons, contributing factors, and relationships behind observed patterns or outcomes** in a business dataset.

## What Are Diagnostic Analytical Questions?

Diagnostic questions focus on understanding **why something happened**, by exploring **drivers, influencing factors, relationships, root causes, correlations, and segment-wise variations** in historical data.

Diagnostic questions aim to go **beyond just what happened**, to explain **what caused it, what influenced it, or how different dimensions contribute to it**.

## How Should These Questions Be Framed?

1. **Use business-friendly language** — business users do not refer to table or column names in queries.
2. **Avoid explicit mentions of table/column names** in the question text.
3. **Ensure each question reflects natural business thinking**.
4. **Questions should be self-contained and clear**, so they can be answered directly using the dataset.

## Complexity Levels

1. **Basic** – High-level questions on causes, drivers, or dimension-wise contribution
   *Example: “What factors contributed to the decline in customer orders?”*

2. **Intermediate** – Segment-wise diagnosis or breakdowns of key changes or outcomes
   *Example: “How did different regions contribute to the drop in quarterly revenue?”*

3. **Advanced** – Multi-factor analysis, correlation-based reasoning, or comparative root cause exploration
   *Example: “What are the key customer attributes driving churn in high-value segments?”*

## Instructions:

1. Generate exactly **9 diagnostic questions** in total : **3 Basic**, **3 Intermediate**, and **3 Advanced**.
2. Each question should be **fully answerable using the given dataset schema**.
3. Avoid questions that require external data or are ambiguous.
4. Use specific **business contexts** like customer behavior, product sales, regional trends, time-based diagnosis, etc.
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
- Prefer: “...across segments”, “by region”, “based on customer type”
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
