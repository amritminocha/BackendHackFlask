from pptx import Presentation
from pptx.dml.color import RGBColor
import json 

def create_presentation(presentation_template, json_path):
    # Load JSON data for slides
    with open(json_path, "r") as f:
        slides_data = json.load(f)

    # Load the existing presentation
    presentation = Presentation(presentation_template)

    # Loop through each slide in the presentation and the JSON data
    for i, (slide, slide_data) in enumerate(zip(presentation.slides, slides_data["slides"])):
        # Use shapes.title and shapes.placeholders[1] if they exist in the slide
        title = slide.shapes.title if slide.shapes.title else None
        placeholder = slide.shapes.placeholders[1] if slide.shapes.placeholders[1] else None

        # First Slide: Title Slide
        if i == 0:
            if title:
                title.text = slide_data["title"]
            if placeholder:
                placeholder.text = slide_data["subtitle"]
        
        # Second Slide: Table of Contents
        elif i == 1:
            if title:
                title.text = slide_data["title"]
            if placeholder:
                placeholder.text = "\n".join(slide_data["bullets"])
        
        # Last Slide: Thank You
        elif i == len(slides_data["slides"]) - 1:
            if title:
                title.text = slide_data["title"]
        
        # In-between Slides: Content Slides
        else:
            if title:
                title.text = slide_data["title"]
            if placeholder:
                placeholder.text = "\n".join(slide_data["content"])

    # Save the modified presentation
    presentation.save("NewModified_Presentation.pptx")