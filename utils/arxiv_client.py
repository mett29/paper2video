import os
from typing import Tuple

import arxiv


class ArxivClient:

    def __init__(self) -> None:
        self.download_dirpath = os.getenv("PAPERS_DIRPATH", "./papers")
        os.makedirs(self.download_dirpath, exist_ok=True)

    def download_paper(self, paper_id: str) -> Tuple[str, str]:
        paper = next(arxiv.Client().results(arxiv.Search(id_list=[paper_id])))
        paper.download_pdf(dirpath=self.download_dirpath, filename=f"{paper_id}.pdf")
        return paper_id, os.path.join(self.download_dirpath, f"{paper_id}.pdf")
