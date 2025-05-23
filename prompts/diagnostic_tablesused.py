    def get_diagnostic_table_identification_prompt(self, schema, question):
        return """## Task:

You are given a dataset schema and a diagnostic analytics question.  
Your goal is to identify the **minimum set of relevant tables** required to identify the **factors or variables that may explain or influence the outcome mentioned in the question**.

### Instructions:
1. Determine the column(s) that represent the **outcome or dependent variable** (e.g., cancellations, delays, etc.).
2. Identify **all possible influencing or explanatory variables (independent variables)** that could be analyzed to explain variation in the outcome.
3. Select **only those tables** that contain either the outcome variable itself or columns that can be logically used as influencing factors (such as aircraft, airport, fare type, flight details, etc.).
4. Include **supporting tables** only if they are joinable and provide useful context (e.g., aircraft or airport metadata).
5. Do not include tables that are **not relevant** to either the outcome or its potential influencing factors.
6. **Avoid listing redundant or unrelated tables.**
7. Do **not explain or justify your selections. Just return a JSON array** of table names.

### Input:
**Schema:**

""" + schema + """

**Question:**

""" + question + """

### Output Format:
```json
["TABLE_NAME_1", "TABLE_NAME_2"]"""
