#Import the Necessary Libraries
import os
import shutil
import pandas as pd
from pathlib import Path

#Set up the paths
csv_file = os.path.join("Dissertation Data","Data_Entry_2017.csv")
NIH_root = os.path.join("Dissertation Data", "NIH_ChestXray14_Images")


#Create the output directories
imageDir = "images"
outputDir = "NIH_pneumonia_dataset"

pneumonia_dir = os.path.join(outputDir, "Pneumonia")
normal_dir = os.path.join(outputDir, "Normal")

#Create the directories if they don't exist'
os.makedirs(pneumonia_dir, exist_ok=True)
os.makedirs(normal_dir, exist_ok=True)

#Read the csv file
df = pd.read_csv(csv_file)

#Split the dataset into pneumonia and normal images
pneumonia_df = df[df["Finding Labels"].str.contains("Pneumonia", na = False)]
normal_df = df[df["Finding Labels"] == "No Finding"]

#Shuffle the dataframes to ensure that the pneumonia images are in the same order as the normal images
normal_df = normal_df.sample(n=len(pneumonia_df), random_state=42)

#Create a dictionary to store the image paths
NIH_Images = {}

#Find all the png files in the NIH_root directory
for path in Path(NIH_root).rglob("*.png"):
    NIH_Images[path.name] = path

#Print the number of images found, a test to see that the dictionary is working correctly
print(f"Total images found: {len(NIH_Images)}")

#Copy the images to the output directories
def copy_images(data_frame, label_folder):
    copied = 0
    missing = 0

    for image_name in data_frame["Image Index"]:
        if image_name in NIH_Images:
            src = NIH_Images[image_name]
            dst = os.path.join(label_folder, image_name)
            shutil.copy(src, dst)
            copied += 1
        else:
            missing += 1

    return copied, missing

#Call the function to copy the images
pneu_img_copied, pneu_img_missing = copy_images(pneumonia_df, pneumonia_dir)
norm_img_copied, norm_img_missing = copy_images(normal_df, normal_dir)

#Print the results
print("Dataset created successfully!")
print("Pneumonia images copied to: ", pneumonia_dir, "Images: ", len(os.listdir(pneumonia_dir)))
print("Normal images copied to: ", normal_dir, "Images: ", len(os.listdir(normal_dir)))
print("Total images copied: ", pneu_img_copied + norm_img_copied)
print("Total images missing: ", pneu_img_missing + norm_img_missing)