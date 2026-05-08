"""
Image Conversion to PNG
"""
#Import Libraries
import numpy as np
from PIL import Image
from pathlib import Path
from tqdm import tqdm

#Set up the paths
Direct = Path(r"C:\Uni Stuff PC\Dissertation Data\Lung_Cancer_Data")

Cancer_Input = Direct / "Nodule154images"
Normal_Input = Direct / "NonNodule93images"

Output_path = Direct / "Lung Cancer Data"

Cancer_Output = Output_path/ "lung_cancer"
Normal_Output = Output_path / "normal"

Cancer_Output.mkdir(parents = True, exist_ok=True)
Normal_Output.mkdir(parents = True, exist_ok=True)

#Define the dimensions of the images
width = 2048
height = 2048

#Define the conversion function
def conversion_to_png(img_path, output_file):
    """
    Converts a JRST .IMG file to PNG format.
    """

    img = np.fromfile(img_path, dtype=">u2")

    expected_size = width * height

    if img.size != expected_size:
        print(f"Skipped {img_path.name}: unexpected file size {img.size}")
        return False

    img = img.reshape((height, width))

    img = img.astype(np.float32)

    img = (img - img.min()) / (img.max() - img.min())
    img = (img * 255).astype(np.uint8)

    Image.fromarray(img).save(output_file)

    return True

#Define the conversion function for a folder
def folder_conversion(input_folder, output_folder):
    """
    Converts all IMG files in the folder to PNG format.
    """
    files = list(input_folder.glob("*"))

    converted_files = 0
    skipped_files = 0

    for file in tqdm(files, desc = f"Converting {input_folder.name} to PNG"):
        if file.is_file():
            output_file = output_folder / f"{file.stem}.png"

            success = conversion_to_png(file, output_file)

            if success:
                converted_files += 1
            else:
                skipped_files += 1

    return converted_files, skipped_files

#Call the conversion function
Cancer_Converted, Cancer_Skipped = folder_conversion(
    Cancer_Input,
    Cancer_Output
)
#Call the conversion function
Normal_Converted, Normal_Skipped = folder_conversion(
    Normal_Input,
    Normal_Output
)

#Print the results
print("Conversion complete.")
print("Nodule images converted:", Cancer_Converted)
print("Nodule images skipped:", Cancer_Skipped)
print("Normal images converted:", Normal_Converted)
print("Normal images skipped:", Normal_Skipped)
print("PNG files saved in:", Output_path)