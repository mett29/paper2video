import os
import json
import argparse

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

from utils.arxiv_client import ArxivClient
from utils.editing import create_beamer, convert_to_video
from config import config


parser = argparse.ArgumentParser(description="Generate presentation video given an arXiv paper.")
parser.add_argument('--arxiv_paper', type=str, required=True, help="arXiv paper id, e.g. 2408.08781")
args = parser.parse_args()


if __name__ == "__main__":

    arxiv_client = ArxivClient()
    paper_id, paper_path = arxiv_client.download_paper(args.arxiv_paper)
    print(f"Downloaded {paper_id} paper to {paper_path}.")

    genai.configure(
        api_key=os.environ.get("GOOGLE_API_KEY")
    )

    model = genai.GenerativeModel(
        model_name='models/gemini-1.5-flash',
        system_instruction=config.PROMPT
    )

    # Upload paper (pdf) via File API
    paper_file = genai.upload_file(path=paper_path)
    print(f"Uploaded file '{paper_file.display_name}' as: {paper_file.uri}")

    raw_response = model.generate_content(
        contents=["PAPER: ", paper_file],
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json"
        )
    )

    # Check how many input and output tokens we're processing
    print(raw_response.usage_metadata)

    response = json.loads(raw_response.text)

    with open(os.path.join(config.OUTPUT_DIRPATH, 'slides_content.json'), 'w') as f_out:
        json.dump(response, f_out, indent=4)

    presentation_path = create_beamer(slides_content=response)
    convert_to_video(
        slides_content=response,
        presentation_path=presentation_path
    )
