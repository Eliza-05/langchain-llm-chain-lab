from langchain_google_genai import ChatGoogleGenerativeAI

def create_llm(
    model: str = "gemini-2.5-flash",
    temperature: float = 0.7,
    max_output_tokens: int | None = None,
) -> ChatGoogleGenerativeAI:
    """
    Initialize the Gemini chat model via LangChain.

    Args:
        model: Gemini model name.
        temperature: Controls randomness in responses (0-1).
        max_output_tokens: Optional output limit to control cost/verbosity.

    Returns:
        Configured ChatGoogleGenerativeAI instance.
    """
    kwargs = {"model": model, "temperature": temperature}

    if max_output_tokens is not None:
        kwargs["max_output_tokens"] = max_output_tokens

    return ChatGoogleGenerativeAI(**kwargs)
