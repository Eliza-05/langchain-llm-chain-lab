from llm.gemini import create_llm
from prompts.templates import make_prompt
from chains.factory import make_chain

REQUIRED_KEYS = ["title:", "definition:", "when_to_use:", "pitfalls:"]

def run_demo_structured() -> None:
    print("\n" + "=" * 60)
    print("DEMO 3: Semi-Structured Output (YAML-like) + Basic Validation")
    print("=" * 60)

    llm = create_llm(temperature=0.2)

    prompt = make_prompt(
        template=(
            "Return a YAML-like block (no code fences) with the following keys:\n"
            "title:\n"
            "definition:\n"
            "when_to_use:\n"
            "pitfalls:\n\n"
            "Topic: {topic}\n\n"
            "Rules:\n"
            "- Keep each value to 1-2 lines\n"
            "- pitfalls must include exactly 3 items separated by ';'\n"
        ),
        input_variables=["topic"],
    )

    chain = make_chain(llm, prompt)

    topic = "Prompt Templates in LangChain"
    result = chain.invoke({"topic": topic})

    print("\nGenerated output:")
    print("-" * 40)
    print(result)

    missing = [k for k in REQUIRED_KEYS if k not in result.lower()]
    print("\nValidation:")
    if missing:
        print(f"- Missing keys: {missing}")
    else:
        print("- All required keys detected ✅")
