Custom Search Engine

This project focuses on designing and implementing a search engine for .txt files. It is built to handle large datasets, provide information about searched queries, and suggest related queries.

Objective

The aim of this project is to create an advanced and feature-rich search function that can index and search through text files effectively. It uses algorithms such as recursion, divide and conquer, dynamic programming, and greedy algorithms to achieve efficient and accurate search results.

Core Functionalities

Recursive File Indexing (Recursion and Backtracking)

Traverse Directories: Navigates through directories and subdirectories to locate all text files.

Tokenization: Breaks down text files into individual words, ignoring case and punctuation.

Inverted Indexing: Maps each word to the files and specific line numbers where it appears.

Divide and Conquer for Large File Processing (Divide and Conquer)

Chunking Large Files: Splits large text files into smaller, manageable chunks.

Parallel Processing: Processes each chunk separately to build partial indexes.

Merging Results: Combines partial indexes from all chunks into a single comprehensive index.

Query Suggestion with Dynamic Programming (Dynamic Programming)

Edit Distance Calculation: Calculates the similarity between the user's query and words in the index to suggest corrections for misspelled queries.

Caching Mechanism: Stores intermediate results to improve efficiency, especially when handling multiple queries.

Greedy Algorithms for Ranking Results (Greedy Algorithms)

Ranking by Frequency: Ranks search results based on how frequently the search terms appear in each file.

Proximity Scoring: Considers how close the search terms are to each other within the text to determine relevance.

Graph-Based Related Query Search

Word Co-occurrence Graph: Captures relationships between words based on their co-occurrence within a specified window size.

Methodology

Recursive File Indexing (Recursion and Backtracking)

Directory Traversal: Recursively explores each directory and its subdirectories to locate all text files.

Tokenization: Reads the content of each text file, removes punctuation, and converts all characters to lowercase.

Inverted Index Creation: Builds an inverted index where each word maps to a list of tuples containing the file path and line number.

Divide and Conquer for Large File Processing

File Chunking: Divides large text files into smaller chunks to manage memory usage and enhance processing speed.

Parallel Processing: Processes each chunk independently to tokenize words and update partial inverted indexes.

Index Merging: Merges all partial inverted indexes into a single comprehensive inverted index.

Query Suggestion with Dynamic Programming

Edit Distance Calculation: Computes the edit distance between the user's query and each word in the inverted index.

Caching Mechanism: Enhances efficiency by caching results of edit distance calculations.

Greedy Algorithms for Ranking Results

Frequency-Based Ranking: Ranks files based on the frequency of search terms.

Proximity Scoring: Considers the proximity of search terms within the text in addition to frequency.

Graph-Based Related Query Search

Word Co-occurrence Graph: Builds a graph capturing relationships between words based on co-occurrence within a specified window size.

Code Documentation

File: indexing.py

Function: find_text_files(root_dir): Recursively traverses the specified root directory to locate all .txt files.

Function: tokenize(text): Converts a string of text into a list of lowercase words, removing punctuation.

Function: build_inverted_index(file_list): Constructs an inverted index mapping each word to the files and line numbers where it appears.

File: ranking.py

Function: rank_results(results, inverted_index, words): Calculates and ranks the relevance of search results based on the frequency of search terms.

File: query_suggestion.py

Function: edit_distance(word1, word2): Computes the edit distance between two words using dynamic programming.

Function: suggest_corrections(words, vocabulary, cache): Provides suggestions for misspelled words based on the closest matches in the vocabulary.

File: graph.py

Class: WordGraph: Builds and manages a word relationship graph for related query suggestions.

Method: add_cooccurrence(word1, word2, count=1): Adds or updates the co-occurrence count between two words in the graph.

Method: build_graph(inverted_index, window_size=5): Constructs the word relationship graph based on word co-occurrence.

Method: get_related_words(word, top_n=5): Retrieves the top related words for a given word based on co-occurrence frequency.

File: search_engine.py

Function: search(inverted_index, query, vocabulary, cache, word_graph, proximity=1): Handles user queries by searching the inverted index, ranking results, and suggesting related queries.

Function: perform_search(inverted_index, words, proximity): Processes valid queries to retrieve common results and ranks them.

Function: main(): Initializes the search engine, builds the indexes, and handles user interaction.

Usage

Clone the repository and navigate to the project directory.

Run the main() function in search_engine.py:

python search_engine.py

Enter your search queries when prompted.

Future Improvements

Enhance query suggestions using machine learning models.

Support for additional file formats (e.g., .pdf, .docx).

Integrate a web-based user interface for ease of use.

Optimize graph-based related query suggestions using advanced graph algorithms.

