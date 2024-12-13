# utils/graph.py

from collections import defaultdict
from itertools import islice

class WordGraph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_cooccurrence(self, word1, word2, count=1):
        if word2 in self.graph[word1]:
            self.graph[word1][word2] += count
        else:
            self.graph[word1][word2] = count

    def build_graph(self, inverted_index, window_size=5):
        """
        Build a word co-occurrence graph based on window_size.
        Words appearing within 'window_size' positions of each other in the same file and line are considered co-occurring.
        """
        # Organize occurrences by file and line for efficient processing
        file_line_map = defaultdict(lambda: defaultdict(list))  # file -> line -> list of positions and words

        for word, occurrences in inverted_index.items():
            for loc in occurrences:
                file_path, line_num, pos = loc
                file_line_map[file_path][line_num].append((pos, word))

        # Iterate through each file and line to find co-occurring words
        for file_path, lines in file_line_map.items():
            for line_num, word_positions in lines.items():
                # Sort words in the line based on position
                sorted_words = sorted(word_positions, key=lambda x: x[0])
                words_in_line = [word for pos, word in sorted_words]

                # Slide a window over the words to find co-occurrences
                for i in range(len(words_in_line)):
                    window = words_in_line[i+1:i+window_size+1]
                    word1 = words_in_line[i]
                    for word2 in window:
                        if word1 != word2:
                            self.add_cooccurrence(word1, word2)

    def get_related_words(self, word, top_n=5):
        if word not in self.graph:
            return []
        related = sorted(self.graph[word].items(), key=lambda item: item[1], reverse=True)
        return [w for w, count in related[:top_n]]