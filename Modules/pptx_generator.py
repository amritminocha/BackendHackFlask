from pptx import Presentation
from pptx.dml.color import RGBColor
import json 

with open("slides.json", "r") as f:
    slides_data = json.load(f)

presentation_path = 'Static/pptx_templates/powerpoint1.pptx'
# Load the existing presentation
presentation = Presentation(presentation_path)

# Loop through each slide in the presentation and the JSON data
for i, (slide, slide_data) in enumerate(zip(presentation.slides, slides_data["slides"])):

    # First Slide: Title Slide
    if i == 0:
        if slide.shapes.title:
            slide.shapes.title.text = slide_data["title"]
        if slide.shapes.placeholders[1]:
            slide.shapes.placeholders[1].text = slide_data["subtitle"]
        
    # Second Slide: Table of Contents
    elif i == 1:
        if slide.shapes.title:
            slide.shapes.title.text = slide_data["title"]
        if slide.shapes.placeholders[1]:
            slide.shapes.placeholders[1].text = "\n".join(slide_data["bullets"])
        
    # Last Slide: Thank You
    elif i == len(slides_data["slides"]) - 1:
        if slide.shapes.title:
            slide.shapes.title.text = slide_data["title"]
        
    # In-between Slides: Content Slides
    else:
        print("Slide",i)
        if slide.shapes.title:
            slide.shapes.title.text = slide_data["title"]
        if slide.shapes.placeholders[1]:
            slide.shapes.placeholders[1].text = "\n".join(slide_data["content"])

# Save the modified presentation
presentation.save("NewModified_Presentation.pptx")
