    def get_prescriptive_table_identification_prompt(self, schema, question):
        return """## Task:

You are given a dataset schema and a **prescriptive analytics** question.
Your goal is to identify the **minimum set of relevant tables** required to **analyze the scenario and recommend optimal actions or decisions** as mentioned in the question.

### Instructions:
1. Determine the column(s) that represent the **objective or decision variable** to be optimized.
2. Identify all possible **input variables (constraints, parameters, influencing factors)** that are required to perform the optimization or decision-making task.
3. Select **only those tables** that contain either the decision variables or columns that can act as **input factors for decision optimization**.
4. Include **supporting tables** only if they are **joinable and contribute meaningful information for decision-making**.
5. Do not include tables that are **not relevant to the prescriptive task**.
6. **Avoid listing redundant or unrelated tables**.
7. Do **not explain or justify your selections. Just return a JSON array** of table names.

### Input:
**Schema:**

""" + schema + """

**Question:**

""" + question + """

### Output Format:
```json
["TABLE_NAME_1", "TABLE_NAME_2"]""";
