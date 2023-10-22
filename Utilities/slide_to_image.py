import os
from comtypes.client import CreateObject

def clear_folder(folder_path: str):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)

def save_pptx_as_png(png_foldername: str, pptx_filename: str, overwrite_folder: bool = False):
    if os.path.isdir(png_foldername):
        if overwrite_folder:
            clear_folder(png_foldername)
        else:
            print(f"Folder {png_foldername} already exists. Set overwrite_folder=True, if you want to overwrite folder content.")
            return

    # Create PowerPoint Application Object
    powerpoint = CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1  # Make PowerPoint visible (helpful for debugging)

    # Open the PowerPoint presentation
    pres = powerpoint.Presentations.Open(pptx_filename)

    # Save as PNG
    ppSaveAsPNG = 17  # The code for PNG format
    pres.SaveAs(png_foldername, ppSaveAsPNG)

    # Close the presentation
    pres.Close()

    # Quit PowerPoint if no other presentations are open
    if powerpoint.Presentations.Count == 0:
        powerpoint.Quit()

# Usage example with properly escaped file paths
save_pptx_as_png(r"C:\Users\hadiz\OneDrive\Desktop\Coding Projects\Hackathon\BackendHackFlask\images", r"C:\Users\hadiz\OneDrive\Desktop\Coding Projects\Hackathon\BackendHackFlask\Static\powerpoint1.pptx", overwrite_folder=True)
