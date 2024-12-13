Custom Search Engine
This project focuses on designing and implementing a search engine for .txt files. It is built to handle large datasets, provide information about searched queries, and suggest related queries.

Objective
The aim of this project is to create an advanced and feature-rich search function that can index and search through text files effectively. It uses algorithms such as recursion, divide and conquer, dynamic programming, and greedy algorithms to achieve efficient and accurate search results.

Core Functionalities
Recursive File Indexing (Recursion and Backtracking)

Traverse Directories: The search engine navigates through directories and subdirectories to locate all text files.
Tokenization: It breaks down text files into individual words, ignoring case and punctuation.
Inverted Indexing: An inverted index is created, mapping each word to the files and specific line numbers where it appears.
Divide and Conquer for Large File Processing (Divide and Conquer)

Chunking Large Files: Large text files are split into smaller, manageable chunks.
Parallel Processing: Each chunk is processed separately to build partial indexes.
Merging Results: The partial indexes from all chunks are combined into a single comprehensive index.
Query Suggestion with Dynamic Programming (Dynamic Programming)

Edit Distance Calculation: The search engine calculates the similarity between the user's query and words in the index to suggest corrections for misspelled queries.
Caching Mechanism: Intermediate results are stored to improve efficiency, especially when handling multiple queries.
Greedy Algorithms for Ranking Results (Greedy Algorithms)

Ranking by Frequency: Search results are ranked based on how frequently the search terms appear in each file.
Proximity Scoring: The engine considers how close the search terms are to each other within the text to determine relevance.
Graph-Based Related Query Search

Word Co-occurrence Graph: A graph is built to capture the relationships between words based on their co-occurrence within a specified window size.
Methodology
This section details the implementation of each core functionality, explaining the role of specific algorithms and how they contribute to the overall functionality of the search engine.

Recursive File Indexing (Recursion and Backtracking)
Directory Traversal: A recursive function explores each directory and its subdirectories to locate all text files.
Tokenization: The content of each text file is read, and words are extracted by removing punctuation and converting all characters to lowercase.
Inverted Index Creation: An inverted index is built where each word maps to a list of tuples containing the file path and the line number where the word appears.
Divide and Conquer for Large File Processing
File Chunking: Large text files are divided into smaller chunks to manage memory usage and enhance processing speed. Each chunk is processed independently to build partial inverted indexes.
Parallel Processing: Each chunk is processed to tokenize words and update a partial inverted index.
Index Merging: After processing all chunks, partial inverted indexes are merged into a single inverted index.
Query Suggestion with Dynamic Programming
Edit Distance Calculation: The search engine calculates the edit distance between the user's query and each word in the inverted index. Words with the smallest edit distances are suggested as corrections.
Caching Mechanism: To enhance efficiency, results of edit distance calculations are cached.
Greedy Algorithms for Ranking Results
Frequency-Based Ranking: The search engine ranks files based on how frequently the search terms appear.
Proximity Scoring: In addition to frequency, the engine considers the proximity of search terms within the text.
Graph-Based Related Query Search
Word Co-occurrence Graph: A graph is built to capture the relationships between words based on their co-occurrence within a specified window size.
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
Method: build_graph(inverted_index, window_size=5): Constructs the word relationship graph based on word co-occurrence within a specified window size.
Method: get_related_words(word, top_n=5): Retrieves the top related words for a given word based on co-occurrence frequency.
File: search_engine.py
Function: search(inverted_index, query, vocabulary, cache, word_graph, proximity=1): Handles user queries by searching the inverted index, ranking results, and suggesting related queries.
Function: perform_search(inverted_index, words, proximity): Processes valid queries to retrieve common results and ranks them.
Function: main(): Initializes the search engine, builds the indexes, and handles user interaction.
Usage
To use this search engine:

Run the main() function in search_engine.py.
Enter your search queries when prompted.
