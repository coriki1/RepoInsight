FILE_ANALYSIS_PROMPT = (
    "Analyze the following source file: {name}\n\n"
    "Summarize concisely in Markdown format, covering:\n"
    "- The main purpose/responsibility of the file\n"
    "- Key classes/functions it contains\n"
    "- Any notable issues or improvement suggestions\n\n"
    "The code:\n```\n{content}\n```"
)

PROJECT_SUMMARY_PROMPT = (
    "Based on the following per-file code analyses, write a comprehensive project summary "
    "in Markdown format. Cover: (1) the project's purpose and main features, "
    "(2) the architecture and relationships between main components, "
    "(3) overall code quality and potential improvement suggestions. "
    "Avoid ASCII-art diagrams; describe relationships using plain nested lists instead.\n\n"
    "{combined}"
)