# Automated File Organizer & Cleanup Utility

## Project Overview
The Automated File Organizer is a Python-based utility that automatically organizes files into separate folders based on their file extensions.

It helps users keep their directories clean and organized, reducing the need to manually sort files.

## Features
- Automatically organizes files by extension.
- Creates category folders automatically.
- Supports Documents, Images, Videos, Archives, and Code files.
- Detects unsupported file types.
- Prevents duplicate filenames by renaming them.
- Handles permission and destination file errors.
- Validates the selected folder path.
- Displays a summary of organized, skipped, and error files.

## Technologies Used
- Python 3
- pathlib
- shutil

## Supported File Types

| Category | Extensions |
|---|---|
| Documents | .pdf, .txt, .docx |
| Images | .jpg, .jpeg, .png |
| Videos | .mp4, .mkv |
| Archives | .zip, .rar |
| Code | .py, .java, .c |

## How to Run

1. Clone or download this repository.
2. Open the project folder.
3. Run the following command:

```bash
python organizer.py
```

4. Enter the folder path you want to organize.
5. The program will automatically create folders and move supported files.

## Example Output

```text
Enter folder path to organize: C:\Users\shiva\FileOrganizer_Test

song.mp3 skipped - Unsupported file type

Total files organized: 0
Total files skipped: 1
Total files with errors: 0
File organization completed successfully!
```

## Project Structure

```text
Task_3_File_Organizer/
│
├── organizer.py
└── README.md
```

## Author
Shiva Karthik

## Internship Project
Datheon Python Programming Internship