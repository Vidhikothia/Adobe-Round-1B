# src/main.py
import json
import time
from extract_text import extract_text_from_pdfs
from analyze_sections import find_relevant_sections

def main():
    input_folder = "input"
    output_file = "output/results.json"

    # Step 1: Extract Text
    raw_data = extract_text_from_pdfs(input_folder)

    # Step 2: Define persona and job
    persona = "PhD Researcher in Computational Biology"
    job = "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks"

    # Step 3: Analyze
    ranked = find_relevant_sections(raw_data, persona, job)

    # Step 4: Format output
    output = {
        "metadata": {
            "input_documents": list(set([block["document"] for block in ranked])),
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        },
        "extracted_sections": []
    }

    for idx, block in enumerate(ranked[:10]):  # Take top 10
        output["extracted_sections"].append({
            "document": block["document"],
            "page_number": block["page"],
            "section_title": "Unknown",  # Optional if no clear title found
            "importance_rank": idx + 1
        })

    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()
