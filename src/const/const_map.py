PROMP_SUGGESTION_TEMPLATE = """
    You are an expert english teacher .\n
    Based on grammar ielts 7.0 in {list_grammar}.\n 
    Based on vocabulary ielts 7.0 in {list_vocabulary}\n 
    Given the student essay delimited by ```,\n
    Can you give me suggestion  how to improve grammar, vocabulary, context for the student essay based on vocabulary , grammar and list out a list of vocabulary words, grammar words,context string that need to be replaced with format: 
    ````
    Response:
        Vocabulary:
            1.Vocabulary to be replaced -> alternative vocabulary
            2 ...
        Grammar:
            1.Grammar to be replaced -> alternative Grammar
            2 ...
        Context:
            1.Context to be replaced -> alternative Context
            2 ...
    ````
    Student essay: ```
    {essay}
    ```
"""

MODEL_NAME="gpt-3.5-turbo"

GRAMMAR_TOPIC = {
    "study_abroad_canada_ielts_7.0" : "Topic-EnglishWing-Travel-Canada-7.0-200-Grammar"
}

VOCABULARY_TOPIC = {
    "study_abroad_canada_ielts_7.0" : "Topic-EnglishWing-Travel-Canada-7.0-200-Vocabulary"
}