    def get_descriptive_table_identification_prompt(self, schema, question):
        return """## Task:

You are given a dataset schema and a natural language question.

Your task is to identify the **minimum set of tables required to answer the question**, based strictly on the columns available in each table.

### Instructions:
1. Carefully analyze the question and identify what data elements are required to answer it.
2. Refer to the dataset schema and determine which tables contain those elements.
3. Select **only the relevant tables** — avoid including unnecessary ones.
4. **Do not guess or assume columns/tables that are not explicitly in the schema.**
5. Return the output as a clean **flat JSON array of table names**, without any extra text, formatting, or explanations.
6. Do **not return any explanation or additional formatting**.
7. **Do not print multiple separate JSON arrays — return just one complete JSON array.**

### Input:
**Schema:**

""" + schema + """

**Question:**

""" + question + """

### Output Format:
```json
["TABLE_NAME_1", "TABLE_NAME_2"]"""
