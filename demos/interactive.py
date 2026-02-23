from llm.gemini import create_llm
from prompts.templates import make_prompt
from chains.factory import make_chain

def run_interactive() -> None:
    print("\n" + "=" * 60)
    print("INTERACTIVE MODE (Commands: /help, /temp <0-1>, exit)")
    print("=" * 60)

    temperature = 0.7
    llm = create_llm(temperature=temperature)

    prompt = make_prompt(
        template=(
            "You are a helpful assistant for AI/ML students.\n"
            "Answer clearly and concisely.\n\n"
            "Question: {question}"
        ),
        input_variables=["question"],
    )
    chain = make_chain(llm, prompt)

    while True:
        user = input("\n> ").strip()

        if not user:
            continue

        if user.lower() in ["exit", "quit", "q"]:
            print("Goodbye!")
            break

        if user.startswith("/help"):
            print("Commands:")
            print("- /temp <value>   Set temperature (0.0 - 1.0)")
            print("- exit | quit | q  Exit interactive mode")
            continue

        if user.startswith("/temp"):
            parts = user.split()
            if len(parts) != 2:
                print("Usage: /temp 0.3")
                continue
            try:
                temperature = float(parts[1])
                if not (0.0 <= temperature <= 1.0):
                    raise ValueError()
            except ValueError:
                print("Temperature must be a number between 0.0 and 1.0")
                continue

            llm = create_llm(temperature=temperature)
            chain = make_chain(llm, prompt)
            print(f"Temperature updated to {temperature}")
            continue

        print("\nResponse:")
        print("-" * 40)
        print(chain.invoke({"question": user}))
