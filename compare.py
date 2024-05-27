import difflib
import os

def calculate_similarity(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()

    sequence_matcher = difflib.SequenceMatcher(None, content1, content2)
    similarity = sequence_matcher.ratio() * 100
    return similarity


def compare_directories_textually(dir1, dir2):
    common_files = set(os.listdir(dir1)) & set(os.listdir(dir2))
    for filename in common_files:
        file1 = os.path.join(dir1, filename)
        file2 = os.path.join(dir2, filename)
        if os.path.isfile(file1) and os.path.isfile(file2):
            print(f"Comparaison des fichiers {file1} et {file2}:")

            # Calculate similarity
            similarity = calculate_similarity(file1, file2)
            print(f"Similitude: {similarity:.2f}%")

folder1 = "folder1"
folder2 = "folder2"
compare_directories_textually(folder1, folder2)
