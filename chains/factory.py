from langchain_core.output_parsers import StrOutputParser

def make_chain(llm, prompt):
    """
    Build a LCEL chain: prompt | llm | output_parser
    """
    return prompt | llm | StrOutputParser()
