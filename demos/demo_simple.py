from llm.gemini import create_llm
from prompts.templates import make_prompt
from chains.factory import make_chain

def run_demo_simple() -> None:
    print("\n" + "=" * 60)
    print("DEMO 1: Controlled Explanation (Style + Constraints)")
    print("=" * 60)

    llm = create_llm(temperature=0.4)

    prompt = make_prompt(
        template=(
            "You are a technical tutor.\n"
            "Explain the concept: {topic}\n\n"
            "Constraints:\n"
            "- Use exactly 4 bullet points\n"
            "- Each bullet must be <= 15 words\n"
            "- Include one short analogy in the last bullet\n"
        ),
        input_variables=["topic"],
    )

    chain = make_chain(llm, prompt)

    for topic in ["embeddings", "vector database", "prompt injection"]:
        print(f"\nTopic: {topic}")
        print("-" * 40)
        print(chain.invoke({"topic": topic}))
