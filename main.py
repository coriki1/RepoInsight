import argparse
import os
from google import genai
from repository import Repository


def main():
    parser = argparse.ArgumentParser(
        description="Analyzes a project repository using AI."
    )
    parser.add_argument("path", help="Path to the repository")
    args = parser.parse_args()

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    project_repository = Repository(args.path, client)
    project_repository.scan()
    project_repository.analyze_files()
    project_repository.summarize_project()
    project_repository.export_pdf("project_summary.pdf")

    print("Done! Report saved as: project_summary.pdf")


if __name__ == "__main__":
    main()