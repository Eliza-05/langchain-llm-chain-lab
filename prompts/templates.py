from langchain_core.prompts import PromptTemplate

def make_prompt(template: str, input_variables: list[str]) -> PromptTemplate:
    """Create a reusable prompt template."""
    return PromptTemplate(template=template, input_variables=input_variables)
