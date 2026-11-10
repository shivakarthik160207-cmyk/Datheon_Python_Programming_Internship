import shutil
import pathlib

file_types = {
    "Documents": [".pdf", ".txt", ".docx"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".java", ".c"]
}
folder_path = input("Enter folder path to organize: ")
folder = pathlib.Path(folder_path)
if not folder.exists():
    print("Folder does not exist!")
    exit()
if not folder.is_dir():
    print("Please enter a valid folder!")
    exit()

for folder_name in file_types:
    new_folder = folder / folder_name
    new_folder.mkdir(exist_ok=True)

organized_count = 0
skipped_count = 0
error_count = 0


for file in folder.iterdir():
    if file.is_file():
        extension = file.suffix.lower()

        for folder_name, extensions in file_types.items():
            if extension in extensions:
                destination = folder / folder_name / file.name
                counter = 1

                while destination.exists():
                    destination = folder / folder_name / f"{file.stem}_{counter}{file.suffix}"
                    counter += 1
                try:
                    shutil.move(str(file), str(destination))
                    organized_count += 1
                    print(file.name, "moved to", folder_name)

                except PermissionError:
                    error_count += 1
                    print(file.name, "- Permission denied!")

                except FileExistsError:
                    error_count += 1
                    print(file.name, "- Destination file already exists!")

                break
                
        else:
            skipped_count += 1
            print(file.name, "skipped - Unsupported file type")

print("\nTotal files organized:", organized_count)
print("Total files skipped:", skipped_count)
print("Total files with errors:", error_count)
print("File organization completed successfully!")
