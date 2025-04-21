'''import os

def rename_images_in_folder(folder_path):
    files = os.listdir(folder_path)

    for i, filename in enumerate(files):
      
        old_path = os.path.join(folder_path, filename)
        new_filename = f"image-{i:02d}.png"
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_filename}")

folder_path = r"C:\Users\bouak\OneDrive\Desktop\idk but ye\horse"
rename_images_in_folder(folder_path)'''

# updated script

import os

def rename(folder_path):
    for idx, filename in enumerate(os.listdir(folder_path)):
        src = f"{folder_path}\\{filename}"
        dst = f"{folder_path}\\imaage-{idx:02d}.png"
        os.rename(src, dst)
        print(f"Renamed {src} to {dst}")

root_folder = r"C:\Users\bouak\OneDrive\Desktop\Dataloader Dataset"

for subfolder in os.listdir(root_folder):
    subfolder_path = f"{root_folder}\\{subfolder}"
    rename(subfolder_path)
