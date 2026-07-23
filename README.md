# RepoInsight

A command-line tool that analyzes a source code repository using the Gemini API and generates a PDF summary report.

## What it does

1. **Scan** — walks the given directory and collects all supported source files (C/C++, Python, JS/TS, Go, Rust, Java, and many more — see `config.py`).
2. **Analyze** — sends each file's content to Gemini, which produces a concise Markdown analysis (purpose, key classes/functions, notable issues).
3. **Summarize** — combines all per-file analyses into a single project-level summary (purpose, architecture, code quality, improvement suggestions).
4. **Export** — converts the summary from Markdown to HTML and renders it as a PDF report.

## Requirements

- Python 3.10+
- A Gemini API key
- Dependencies:
  ```
  pip install google-genai markdown xhtml2pdf
  ```

## Setup

Set your API key as an environment variable:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

## Usage

```bash
python main.py /path/to/repository
```

This scans the given repository and produces `project_summary.pdf` in the current directory.

## Project structure

```
RepoInsight/
├── main.py         # CLI entry point
├── repository.py   # Repository class: scan, analyze, summarize, export
├── prompts.py       # Prompt templates for file- and project-level analysis
└── config.py         # Supported file extensions
```

## Known limitations

- Files are analyzed sequentially (with a fixed delay between requests), which can be slow for large repositories.
- No retry/error handling around API calls — a failed request currently stops the whole run.
- Very large files are not truncated or chunked before being sent to the model.

## Possible improvements

- Batch or parallelize file analysis requests
- Add retry logic and graceful error handling
- Chunk large files to respect model context limits
- Add a `requirements.txt` / `pyproject.toml`
