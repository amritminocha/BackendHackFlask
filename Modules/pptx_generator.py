from pptx import Presentation
from pptx.dml.color import RGBColor

presentation_path = 'Static/pptx_templates/powerpoint1.pptx'
# Load the existing presentation
presentation = Presentation(presentation_path)

first_slide = presentation.slides[0]
if first_slide.shapes.title:
    first_slide.shapes.title.text = "Hello Amrit"
    
    # Access the text frame of the title
    text_frame = first_slide.shapes.title.text_frame
    # If there's no run in the text frame (newly added text), 
    # then we set the font color for the entire text frame.
    if len(text_frame.paragraphs[0].runs) == 0:
        text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
    else:
        # If there's already a run, set the font color for that specific run
        text_run = text_frame.paragraphs[0].runs[0]
        text_run.font.color.rgb = RGBColor(255, 255, 255)

presentation.save('modified_presentation2.pptx')


