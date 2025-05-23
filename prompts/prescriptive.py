    def get_prescriptive_prompt(self, schema):
        return """## Task:

You are an expert in Business Intelligence (BI) and Data Analytics. Your objective is to generate **prescriptive analytical questions** that help determine **optimal actions, strategies, or decisions** based on the available data from a business dataset.

## What Are Prescriptive Analytical Questions?

Prescriptive questions focus on understanding **what actions should be taken** to achieve desired outcomes, such as increasing revenue, reducing risk, optimizing operations, improving customer retention, or enhancing resource allocation.

Prescriptive analytics aims to answer questions like **What should we do? How can we optimize performance? Which actions will yield the best results?**.

## How Should These Questions Be Framed?

1. **Use business-friendly language** — business users do not refer to table or column names in queries.
2. **Avoid explicit mentions of table/column names** in the question text.
3. **Ensure each question reflects natural business thinking**.
4. **Questions should be self-contained and clear**, so they can be answered directly using the dataset.

## Complexity Levels

1. **Basic** – High-level decision-making questions based on general patterns.
   *Example: “What actions can help reduce customer attrition?”*

2. **Intermediate** – Action-oriented questions based on specific conditions or business segments.
   *Example: “What pricing strategies should be considered to improve sales across low-performing regions?”*

3. **Advanced** – Optimization questions involving multi-variable trade-offs or scenario-based decisions.
   *Example: “Which combination of resource allocation and campaign targeting would maximize revenue with minimal cost increase?”*

## Instructions:

1. Generate exactly **9 prescriptive questions** in total : **3 Basic**, **3 Intermediate**, and **3 Advanced**.
2. Each question must be **realistically and fully answerable using the given dataset schema only**.
3. **Avoid questions that require any external or unavailable data.**
4. Use specific **business contexts** like customer decisions, pricing strategies, resource allocation, process optimization — only when such dimensions are clearly available in the schema.
5. **Avoid mentioning actual table or column names in the question text.**
6. **Enclose each question within `<question>...</question>` tags.**
7. Return a clean, structured output in JSON format with each question and its complexity level.
8. **Again, do not return anything except the raw JSON array. Avoid any headings, notes, or boxed formats.**
9. All 9 questions must be returned in a **single flat JSON array**.
10. Do **not create multiple arrays or group questions by complexity** — just one array with 9 JSON objects.

Ensure:

1. Each question must be **strictly grounded in the dataset schema**. If the schema does not include a particular variable, behavior, or entity, do not generate a question about it.
2. **Do not invent, infer, or assume the presence of additional data, columns, or derived variables.**
3. Do not reference external or hypothetical factors such as market demand, customer sentiment, seasonality, or competitive pricing unless clearly reflected in the schema.
4. Do not use vague phrases like "strategic improvements", or "business growth plans" unless such improvements can be directly tied to measurable variables in the schema.
5. Only formulate questions that can be answered using optimization, recommendation, segmentation, trade-off analysis, or decision modeling from **columns explicitly provided in the schema**.
6. Do not assume the presence of specific timeframes, demographic groups, or business categories (e.g., premium customers, quarterly targets, special campaigns) unless they are **explicitly available** in the dataset schema.
  - Prefer phrasing like: “based on available groups or categories”, “for the segments currently available”
  - Avoid: “VIP customers”, “holiday campaigns”, “urban customers” if not in the schema.
7. Ensure that **each question is practically actionable** using data-driven prescriptive modeling techniques such as optimization, scenario simulation, decision trees, or what-if analysis.
8. Only formulate questions that can be answered using optimization, recommendation, segmentation, trade-off analysis, or decision modeling with columns explicitly provided in the schema.

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

Return a single JSON array named `questions`, not multiple arrays.""";
