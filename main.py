import os
import shutil
#defining a fuction for copying the files from one folder to another
def copy_files_with_extension(source_folder, destination_folder, file_extension):
 # Create the destination folder if it doesn't exist
 if not os.path.exists(destination_folder):
 os.makedirs(destination_folder)
 # Walk through the source folder and its subdirectories
 for foldername, subfolders, filenames in os.walk(source_folder):
 for filename in filenames:

 if filename.endswith(file_extension):
 source_path = os.path.join(foldername, filename)
 destination_path = os.path.join(destination_folder, filename)
 # Copy the file to the destination folder
8
 try:
 shutil.copy(source_path, destination_path)
 print(f"Copied: {source_path} -> {destination_path}")
 except Exception as e:
 print(f"Error copying {source_path}: {str(e)}")
if __name__ == "__main__":
 source_folder = input("Enter the source folder path: ")
 destination_folder = input("Enter the destination folder path: ")
 file_extension = input("Enter the file extension (e.g., .pdf, .jpg): ")
 copy_files_with_extension(source_folder, destination_folder, file_extension) 
