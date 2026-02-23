from llm.gemini import create_llm
from prompts.templates import make_prompt
from chains.factory import make_chain

def run_demo_creative() -> None:
    print("\n" + "=" * 60)
    print("DEMO 2: Temperature A/B Test")
    print("=" * 60)

    prompt = make_prompt(
        template=(
            "Write a concise explanation of {concept}.\n"
            "Audience: {audience}\n"
            "Keep it under 120 words."
        ),
        input_variables=["concept", "audience"],
    )

    chain_low = make_chain(create_llm(temperature=0.1), prompt)
    chain_high = make_chain(create_llm(temperature=0.9), prompt)

    payload = {"concept": "RAG vs fine-tuning", "audience": "a first-year engineering student"}

    print("\nLow temperature (0.1):")
    print("-" * 40)
    print(chain_low.invoke(payload))

    print("\nHigh temperature (0.9):")
    print("-" * 40)
    print(chain_high.invoke(payload))
