# search_engine.py

from utils.indexing import find_text_files, build_inverted_index
from utils.query_suggestion import suggest_corrections
from utils.ranking import rank_results
from utils.graph import WordGraph


def search(inverted_index, query, vocabulary, cache, word_graph, proximity=1):
    words = query.lower().split()
    if not words:
        print("Please enter a valid query.")
        return

    # Check if all words are in the vocabulary
    missing_words = [word for word in words if word not in vocabulary]

    if not missing_words:
        # Proceed with normal search
        perform_search(inverted_index, words, proximity)
        # Suggest related queries
        related = set()
        for word in words:
            related_words = word_graph.get_related_words(word)
            related.update(related_words)
        if related:
            print("Related queries:")
            print(", ".join(related))
    else:
        # Suggest corrections
        suggestions = suggest_corrections(words, vocabulary, cache)
        corrected_query = ' '.join(suggestions)
        print(f"No exact match found for '{query}'.")
        print(f"Did you mean: '{corrected_query}'?")

        user_input = input("Press 'y' to search with the suggested query, or any other key to skip: ").strip().lower()
        if user_input == 'y':
            search(inverted_index, corrected_query, vocabulary, cache, word_graph, proximity)
        else:
            print("No results found.")

def perform_search(inverted_index, words, proximity):
    results = []
    for word in words:
        if word in inverted_index:
            results.append(set((loc[0], loc[1]) for loc in inverted_index[word]))
        else:
            print(f"No results found for '{word}'.")
            return

    common_results = set.intersection(*results)

    if common_results:
        ranked_results = rank_results(common_results, inverted_index, words)
        print(f"Results for '{' '.join(words)}':")
        for file_path, details in ranked_results:
            print(f"File: {file_path}")
            print(f"Lines: {', '.join(map(str, sorted(details['lines'])))}")
            print(f"Number of Occurrences: {details['score']}")
    else:
        print(f"No documents contain all the words in '{' '.join(words)}'.")

def check_proximity(positions_list, proximity):
    # positions_list is a list of sets of positions for each word
    positions = [sorted(pos_list) for pos_list in positions_list]
    for pos_combination in zip(*positions):
        if max(pos_combination) - min(pos_combination) <= proximity:
            return True
    return False

def main():
    try:
        root_dir = 'data/'
        text_files = find_text_files(root_dir)
        inverted_index = build_inverted_index(text_files)

        # Build the word relationship graph
        word_graph = WordGraph()
        word_graph.build_graph(inverted_index)

        print("Welcome to the Custom Search Engine!")
        print("You can search for words or phrases.")
        print("Type 'exit' to quit the search engine.")

        vocabulary = set(inverted_index.keys())  # Build a vocabulary of all indexed words
        cache = {}

        while True:
            query = input("\nEnter your search query: ").strip()
            if query.lower() == 'exit':
                print("Exiting the search engine. Goodbye!")
                break
            elif not query:
                print("Please enter a non-empty query.")
                continue
            search(inverted_index, query, vocabulary, cache, word_graph)
    except KeyboardInterrupt:
        print("\nSearch engine interrupted by user. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()