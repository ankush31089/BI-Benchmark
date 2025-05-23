    def get_predictive_prompt(self, schema):
        return """## Task:

You are an expert in Business Intelligence (BI) and Data Analytics. Your objective is to generate **predictive analytical questions** that help anticipate **future outcomes, trends, patterns, or business performance** using available historical and current data from a business dataset.

## What Are Predictive Analytical Questions?

Predictive questions focus on understanding **what is likely to happen in the future**, by uncovering **patterns, trends, and relationships in historical data that can be used to forecast future events, behaviors, or outcomes**.

Predictive analytics aims to answer questions like **what will happen, what is likely to occur, and which future outcome is probable based on past behavior and current attributes**.

## How Should These Questions Be Framed?

1. **Use business-friendly language** — business users do not refer to table or column names in queries.
2. **Avoid explicit mentions of table/column names** in the question text.
3. **Ensure each question reflects natural business thinking**.
4. **Questions should be self-contained and clear**, so they can be answered directly using the dataset.

## Complexity Levels

1. **Basic** – High-level predictive questions based on trends or likelihood
   *Example: “Which customers are more likely to reduce their engagement in the next quarter?”*

2. **Intermediate** – Prediction questions based on patterns in historical behavior across segments or dimensions
   *Example: “Which product categories are likely to see growth based on past performance across regions?”*

3. **Advanced** – Multi-factor prediction questions involving multiple variables or risk identification
   *Example: “Which factors best predict customer churn risk in the next quarter?”*

## Instructions:

1. Generate exactly **9 predictive questions** in total : **3 Basic**, **3 Intermediate**, and **3 Advanced**.
2. Each question must be **realistically and fully answerable using the given dataset schema only**.
3. **Avoid questions that require any external or unavailable data.**
4. Use specific **business contexts** like customer behavior, product sales, regional trends, time-based forecasting - only when such dimensions are clearly available in the schema.
5. **Avoid mentioning actual table or column names in the question text.**
6. **Enclose each question within `<question>...</question>` tags.**
7. Return a clean, structured output in JSON format with each question and its complexity level.
8. **Again, do not return anything except the raw JSON array. Avoid any headings, notes, or boxed formats.**
9. All 9 questions must be returned in a **single flat JSON array**.
10. Do **not create multiple arrays or group questions by complexity** — just one array with 9 JSON objects.

Ensure:

1. Each question must be **strictly grounded in the dataset schema**. If the schema does not include a particular variable, behavior, or entity, do not generate a question about it.
2. **Do not invent, infer, or assume the presence of additional data, columns, or derived variables.**
3. Do not reference external or hypothetical factors such as market demand, customer sentiment, seasonality, or operational strategy unless clearly reflected in the schema.
4. Do not use vague phrases like "expected to grow", "future potential", or "market trends" unless such trends can be derived directly from existing schema fields.
5. Only formulate questions that can be answered using patterns, distributions, associations, or forecasts from **columns explicitly provided in the schema**.
6. Do not assume the presence of specific timeframes, demographic groups, or entity subtypes (e.g., premium customers, age groups, cities, seasons) unless these are **explicitly available** in the dataset schema.
  - Prefer phrasing like: *“across segments”, “based on available categories”, “by available types or groups”*.
  - Avoid: *“last year”, “city-wise”, “VIP customers”* if such values are not available in the schema.
7. Ensure that **each question is practically executable** using typical data analysis or forecasting methods applied to the dataset.

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
