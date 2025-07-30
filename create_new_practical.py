import os
import re

# --- Configuration ---
# This should be the folder containing your practical files.
TARGET_DIR = 'aipack05'


# -------------------

def create_next_file():
    """Scans the target directory and creates the next file in the sequence."""
    latest_num = 0

    # This regular expression finds the number in your filenames (e.g., AIPRACTICAL117.py)
    pattern = re.compile(r'AIPRACTICAL(\d+)\.py$')

    try:
        # Get a list of all files in the target directory
        files_in_dir = os.listdir(TARGET_DIR)

        # Loop through the files to find the highest number
        for filename in files_in_dir:
            match = pattern.match(filename)
            if match:
                num = int(match.group(1))
                if num > latest_num:
                    latest_num = num

        # If no files were found (latest_num is still 0), start from 100
        # so the first file created will be 101.
        if latest_num == 0:
            latest_num = 100

        # Determine the new file number and create the full path
        new_num = latest_num + 1
        new_filename = f'AIPRACTICAL{new_num}.py'
        new_filepath = os.path.join(TARGET_DIR, new_filename)

        # Create the new, empty file
        with open(new_filepath, 'w') as f:
            pass  # Creates an empty file

        print(f"✅ Success! Created new file: {new_filepath}")

    except FileNotFoundError:
        print(f"❌ Error: The directory '{TARGET_DIR}' was not found.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# This makes the script runnable from the command line
if __name__ == '__main__':
    create_next_file()