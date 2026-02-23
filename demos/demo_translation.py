from llm.gemini import create_llm
from prompts.templates import make_prompt
from chains.factory import make_chain

def run_demo_translation() -> None:
    print("\n" + "=" * 60)
    print("DEMO 4: Technical Rewrite (Clarity + Tone)")
    print("=" * 60)

    llm = create_llm(temperature=0.3)

    prompt = make_prompt(
        template=(
            "Rewrite the following text to be clear and professional.\n"
            "Constraints:\n"
            "- Keep the meaning\n"
            "- Use a technical tone\n"
            "- 70 to 110 words\n"
            "- End with a single-sentence summary starting with 'In summary,'\n\n"
            "Text:\n{text}\n"
        ),
        input_variables=["text"],
    )

    chain = make_chain(llm, prompt)

    raw = (
        "RAG is cool because the model can look things up, so it doesn't hallucinate as much "
        "and it can answer about our docs. It’s like it has google but for your files."
    )

    print("\nOriginal:")
    print("-" * 40)
    print(raw)

    print("\nRewritten:")
    print("-" * 40)
    print(chain.invoke({"text": raw}))
