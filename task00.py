import os

def rename_images_in_folder(folder_path):
    files = os.listdir(folder_path)

    for i, filename in enumerate(files):
      
        old_path = os.path.join(folder_path, filename)
        new_filename = f"image-{i:02d}.png"
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_filename}")

folder_path = r"C:\Users\bouak\OneDrive\Desktop\idk but ye\horse"
rename_images_in_folder(folder_path)
