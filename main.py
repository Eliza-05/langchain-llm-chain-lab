"""
LangChain LLM Chain Basics - Modular Version (Gemini)
Author: <TU NOMBRE>
"""

from config.env import load_environment

from demos.demo_simple import run_demo_simple
from demos.demo_creative import run_demo_creative
from demos.demo_structured import run_demo_structured
from demos.demo_translation import run_demo_translation
from demos.interactive import run_interactive


def main() -> None:
    print("=" * 60)
    print("LangChain LLM Chain Basics (Gemini) - Modular")
    print("=" * 60)

    load_environment()
    print("Environment loaded successfully!")

    run_demo_simple()
    run_demo_creative()
    run_demo_structured()
    run_demo_translation()

    print("\n" + "=" * 60)
    user_input = input("Would you like to enter interactive mode? (yes/no): ").strip().lower()
    if user_input in ["yes", "y"]:
        run_interactive()
    else:
        print("\nAll demonstrations completed successfully!")
        print("=" * 60)


if __name__ == "__main__":
    main()
