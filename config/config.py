"""
Configuration
"""
import os

OUTPUT_DIRPATH = os.getenv('OUTPUT_PATH', './output')
os.makedirs(OUTPUT_DIRPATH, exist_ok=True)
AUDIO_CLIPS_PATH = os.path.join(OUTPUT_DIRPATH, 'audio_clips')
os.makedirs(AUDIO_CLIPS_PATH)
VIDEO_CLIPS_PATH = os.path.join(OUTPUT_DIRPATH, 'video_clips')
os.makedirs(VIDEO_CLIPS_PATH)

PROMPT = """
Your job is to automate the creation of PowerPoint files given the content
of a scientific paper. The goal of the generated presentation is to explain
the content of the paper to a non-technical audience. Add as many details as possible,
make it fun and interesting, don't just copy and paste text from the paper.
Add as many slides as you think are needed to be exhaustive, but no more than 10.
The first slide must contain the title and authors of the paper.
Do not insert unicode characters for emoji in the text.
Do not include acknowledgments or special thanks.
Do not use special characters in the text.
The final slide should be a summary.
The title of each slide should be very short.
In addition to the content of the slides, add in the corresponding JSON
field a narration of what is shown in each slide. Note that this narration
will be used to perform a speech in front of an audience so it must sound
natural, professional and entertaining at the same time.
Using this JSON schema:
    Slide = {"slide_title": str, "slide_content": str, "slide_narration": str}
Return a `list[Slide]`
"""
