import os


def rename_images(root_dir, ext='png'):
    for subfolder in os.listdir(root_dir):
        subfolder_path = os.path.join(root_dir,subfolder)
        if os.path.isdir(subfolder_path):
            files = sorted([f for f in os.listdir(subfolder_path)])[:20]

            for index, filename in enumerate(files):
                old_path = os.path.join(subfolder_path, filename)
                new_name = f"image-{index:02d}.{ext}"
                new_path = os.path.join(subfolder_path, new_name)

                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

rename_images("Dataloader Dataset", 'png')
