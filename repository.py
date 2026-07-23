from pathlib import Path
from config import SUPPORTED_EXTENSIONS
import prompts
import time
import markdown
from xhtml2pdf import pisa


class Repository:
    def __init__(self, path, client):
        self.path = Path(path)
        self.name = self.path.name
        self.client = client
        self.files = []
        self.summary = None

    def scan(self):
        self.files = []
        for file in self.path.rglob("*"):
            if not file.is_file():
                continue
            if file.suffix not in SUPPORTED_EXTENSIONS:
                continue

            try:
                content = file.read_text(encoding="utf-8")
            except (UnicodeDecodeError, PermissionError):
                content = None

            self.files.append({
                "name": file.name,
                "extension": file.suffix,
                "content": content,
                "ai_analysis": None
            })

    def analyze_files(self):
        for file in self.files:
            if file["content"] is None:
                continue

            name = file["name"]
            content = file["content"]

            print(f"Processing item: {name}...")

            interaction = self.client.interactions.create(
                model="gemini-3.5-flash-lite",
                input=prompts.FILE_ANALYSIS_PROMPT.format(name=name, content=content)
            )
            file["ai_analysis"] = interaction.output_text

            time.sleep(3)  # rate limit átlépésének megelőzésére

    def summarize_project(self):
        parts = []
        for file in self.files:
            if file["ai_analysis"]:
                parts.append(f"### {file['name']}\n{file['ai_analysis']}")

        combined = "\n\n".join(parts)

        print(f"Generating summary...")

        interaction = self.client.interactions.create(
            model="gemini-3.6-flash",
            input=prompts.PROJECT_SUMMARY_PROMPT.format(combined=combined)
        )

        self.summary = interaction.output_text
        return self.summary

    def export_pdf(self, output_path="summary.pdf"):
        if not self.summary:
            raise ValueError("No summary available.")

        html_content = markdown.markdown(self.summary)

        with open(output_path, "wb") as f:
            pisa.CreatePDF(html_content, dest=f)