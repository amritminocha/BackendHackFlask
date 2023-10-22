def get_prompt_summarize_ppt(topic, total_slides):
    return f"""
Create a {total_slides}-slide in total (the slides array should have {total_slides} objects) PowerPoint presentation in JSON format on {topic}. Include:
- Slide 1: Title and subtitle.
- Slide 2: Table of Contents with bullet points.
- Last Slide: 'THANK YOU' text.
- Other Slides: Title and 3 paragraphs of Content

For example for a {total_slides}-slide, the JSON format would look like:
{{
  "slides": [
    {{"title": "", "subtitle": ""}},
    {{"title": "Table of Contents", "bullets": ["", "", ""]}},
    // {total_slides-3} objects for {{"title":"", "content": ["","",""]}}
    {{"title": "THANK YOU"}}
  ]
}}
"""
