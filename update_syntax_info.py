import os
import shutil
import requests

def update_syntax_info():
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

    # Dictionary to keep track of missing files
    missing_files = {}

    # Get list of all files in aiDrive company ecosystem folders
    all_files = []
    for folder_name in folder_mapping:
        folder_path = os.path.join('aiDrive_company_ecosystem', folder_name)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    all_files.append(file_path)

    # Check for missing files in each folder
    for folder_name, files in folder_mapping.items():
        folder_path = os.path.join('aiDrive_company_ecosystem', folder_name)
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if not os.path.isfile(file_path):
                # File is missing, create it with default content
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'w') as f:
                    f.write(default_contents[file_name])
                missing_files[file_path] = f"https://remote_repository.com/{folder_name}/{file_name}"

    # Copy missing files to appropriate folders
    for file_path, url in missing_files.items():
        if url:
            # Copy file from remote repository
            response = requests.get(url)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)

if __name__ == '__main__':
    update_syntax_info()
