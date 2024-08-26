# paper2video

Tool designed to transform research papers from arXiv into engaging presentations and videos, ready for upload to YouTube.

This repository automates the process of explaining complex papers, creating visually appealing presentations, and generating video content from those presentations.

Almost everything is AI generated:
- the content of each slide, both title and main text (via Gemini API)
- the narration for each slide, which is then converted to audio (via Gemini API)
- the audio (via Text-to-Speech Google API)
- the animated character lip synched (via Wav2Vec2 using the [PyToon](https://github.com/lukerbs/pytoon) library)

<p align="center">
    <img src="/img/example_frame.png" style="width: 80%;" alt="Sample frame of the final video">
</p>

Some notes:
- I used Gemini Flash 1.5 to reduce costs (it's also a bit faster).
- I used [PyLaTeX](https://jeltef.github.io/PyLaTeX/current/) to generate the presentation. At first I was trying to use python-pptx but
I was having issues with text formatting and the conversion to PDF is a nightmare.

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

Add an animated speaking character
-------------
Going a step further we can add an animated speaking character to the video.
I took inspiration from this YT video: https://www.youtube.com/watch?v=ItVnKlwyWwA, and searching online I found out this repository: https://github.com/lukerbs/pytoon.

PyToon uses character images created by https://github.com/carykh/lazykh, the author of the mentioned video.

PyToon uses `ForceAlign` (https://github.com/lukerbs/forcealign), a library for forced alignment of English text to English Audio.
ForceAlign uses Pytorch's `WAV2VEC2` pretrained model for acoustic feature extraction.

My setup does not have enough RAM to run the above model (I'm on WSL2 on an old PC), hence I decided to split the code and run this part on Colab (the free version, I used a T4 GPU).
You can do the same or you can modify the `convert_to_video()` function in order to directly generate the final result.

You can find the notebook in `animate.ipynb`. It contains all the instructions to make it work.