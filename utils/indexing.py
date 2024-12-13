# utils/indexing.py

import os
import re
from collections import defaultdict
from .chunking import read_file_in_chunks



stopwords = {
    'is', 'at', 'which', 'on', 'and', 'a', 'an', 'the', 'in', 'for',
    'to', 'with', 'of', 'from', 'she', 'are', 'not', 'who', 'you',
    'they', 'their', 'be', 'been', 'being', 'was', 'were', 'it', 'this',
    'that', 'these', 'those', 'has', 'have', 'had', 'do', 'does', 'did',
    'but', 'if', 'or', 'because', 'as', 'until', 'while', 'can', 'will',
    'just', 'don\'t', 'should', 'now'
}
def find_text_files(root_dir):
    """
    Recursively find all .txt files starting from root_dir.
    """
    text_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.txt'):
                text_files.append(os.path.join(root, file))
    return text_files

def Clean_word(word):
    return re.sub(r'[^\w\-]', '', word.lower())

def process_text(text):
    words = re.findall(r'\b\w+\b', text)
    cleaned_words = [Clean_word(word) for word in words]
    return [word for word in cleaned_words if word and word not in stopwords]

def tokenize(text):
    """
    Tokenize text into words, ignoring case and punctuation.
    """
    # Use regular expressions to remove punctuation and split into words
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens

def build_inverted_index(file_list, chunk_size=1024):
    """
    Build an inverted index mapping each word to the files, line numbers, and word positions where it appears.
    Processes files in chunks to handle large files efficiently.
    """
    inverted_index = defaultdict(list)
    for file_path in file_list:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                partial_data = ''
                line_num = 0
                for chunk in read_file_in_chunks(file, chunk_size):
                    data = partial_data + chunk
                    lines = data.split('\n')
                    partial_data = lines.pop()  # Save the last incomplete line
                    for line in lines:
                        line_num += 1
                        words = process_text(line)
                        for pos, word in enumerate(words):
                            entry = (file_path, line_num, pos)
                            inverted_index[word].append(entry)
                # Handle the last partial line if it exists
                if partial_data:
                    line_num += 1
                    words = process_text(partial_data)
                    for pos, word in enumerate(words):
                        entry = (file_path, line_num, pos)
                        inverted_index[word].append(entry)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    return inverted_index