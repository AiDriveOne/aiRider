import os

def monitor_and_fix():
    # Set up the project folder path
    project_folder = 'aiDrive_company_ecosystem'

    # Dictionary mapping folder names to the files they should contain
    folder_mapping = {
        'gems_folder': ['gems/neural.gems', 'gems/ai.gems', 'gems/ml.gems', 'gems/dl.gems', 'gems/scikit.gems'],
        'words_folder': ['words/neural.words', 'words/ai.words', 'words/ml.words', 'words/dl.words', 'words/scikit.words'],
        'text_folder': ['text/neural.text', 'text/ai.text', 'text/ml.text', 'text/dl.text', 'text/scikit.text'],
        'scripts_folder': []
    }

    # Dictionary mapping file names to their default contents
    default_contents = {
        'neural.gems': 'neural\n',
        'ai.gems': 'ai\n',
        'ml.gems': 'machine learning\n',
        'dl.gems': 'deep learning\n',
        'scikit.gems': 'scikit-learn\n',
        'neural.words': 'neural\n',
        'ai.words': 'ai\n',
        'ml.words': 'machine learning\n',
        'dl.words': 'deep learning\n',
        'scikit.words': 'scikit-learn\n',
        'neural.text': 'neural\n',
        'ai.text': 'ai\n',
        'ml.text': 'machine learning\n',
        'dl.text': 'deep learning\n',
        'scikit.text': 'scikit-learn\n'
    }

    # Create a log file to store changes
    log_file = 'fixes.log'

    # Monitor the project folder and files continuously
    while True:
        # Dictionary to keep track of missing files
        missing_files = {}

        # Check for missing files in each folder
        for folder_name, files in folder_mapping.items():
            folder_path = os.path.join(project_folder, folder_name)
            if not os.path.isdir(folder_path):
                os.makedirs(folder_path)
            
            for file_name in files:
                file_path = os.path.join(folder_path, file_name)
                if not os.path.isfile(file_path):
                    # File is missing, create it with default content
                    with open(file_path, 'w') as f:
                        f.write(default_contents[file_name])
                    missing_files[file_path] = True

        # Log changes to the log file
        with open(log_file, 'a') as log:
            log.write("Detected Issues:\n")
            if not missing_files:
                log.write("No missing files found.\n")
            for file_path in missing_files:
                log.write(f"Missing file: {file_path}\n")
        
        if missing_files:
            # Print an explanation of the changes made
            print("Detected Issues:")
            if not missing_files:
                print("No missing files found.")
            for file_path in missing_files:
                print(f"Missing file: {file_path}")

        # Sleep for a specified interval before rechecking the folder
        sleep_duration = 60  # Sleep for 60 seconds (adjust as needed)
        time.sleep(sleep_duration)

if __name__ == '__main__':
    monitor_and_fix()
