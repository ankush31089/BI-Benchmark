    def get_predictive_table_identification_prompt(self, schema, question):
        return """## Task:

You are given a dataset schema and a **predictive analytics** question.
Your goal is to identify the **minimum set of relevant tables** required to **build a model or analysis to predict the outcome mentioned in the question**.

### Instructions:
1. Determine the column(s) that represent the **target or outcome variable** to be predicted.
2. Identify all possible **predictor or feature variables (independent variables)** that could be used to forecast the outcome.
3. Select **only those tables** that contain either the outcome variable or columns that can serve as **predictive features**.
4. Include **supporting tables** only if they are **joinable and contribute meaningful input features for prediction**.
5. Do not include tables that are **not relevant to the prediction task**.
6. **Avoid listing redundant or unrelated tables**.
7. Do **not explain or justify your selections. Just return a JSON array** of table names.

### Input:
**Schema:**

""" + schema + """

**Question:**

""" + question + """

### Output Format:
```json
["TABLE_NAME_1", "TABLE_NAME_2"]"""
