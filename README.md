# paper2video

Tool designed to transform research papers from arXiv into engaging presentations and videos, ready for upload to YouTube. This repository automates the process of explaining complex papers, creating visually appealing presentations, and generating video content from those presentations.

Prerequisites
-------------

```bash
sudo apt-get install ffmpeg
sudo apt-get install latexmk
sudo apt-get install texlive-latex-extra
```

Poetry setup
-------------
```bash
poetry install
```
If you do not use poetry, you can manually install the dependencies contained in the pyproject.toml inside your virtual environment.

How to run
-------------
Create a `.env` file in the project root directory and add the environment variables specified in the `.env.example` file.
```bash
python generate.py --arxiv_paper <arxiv_paper_id>
```
