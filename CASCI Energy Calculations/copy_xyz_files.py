import shutil
import os

def copy_files(indices, src_dir, dest_dir):
    for index in indices:

        file_name = f"open_g2m05_{index:04d}\\MB\\structure.xyz"

        src_path = os.path.join(src_dir, file_name)

        dest_path = os.path.join(dest_dir, f"{index}")

        #Print paths for debugging
        print(f"Source path: {src_path}")
        print(f"Destination path: {dest_path}")

        #Create the directory if it doesn't exist
        os.makedirs(dest_path, exist_ok=True)

        #Construct the full destination file path
        dest_file_path = os.path.join(dest_path, "structure.xyz")

        #Copy the file
        shutil.copy2(src_path, dest_file_path)
        print(f"Copied {src_path} to {dest_file_path}")
