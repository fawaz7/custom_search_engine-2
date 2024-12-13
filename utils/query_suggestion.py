# utils/query_suggestion.py

def edit_distance(word1, word2):
    """
    Compute the Levenshtein edit distance between two words.
    """
    m, n = len(word1), len(word2)
    # Initialize a matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases: empty strings
    for i in range(m + 1):
        dp[i][0] = i  # Deletion
    for j in range(n + 1):
        dp[0][j] = j  # Insertion

    # Compute distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # Deletion
                dp[i][j - 1] + 1,      # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
            )
    return dp[m][n]

def suggest_corrections(words, vocabulary, cache):
    """
    Suggest corrections for misspelled words using edit distance.
    """
    suggestions = []
    for word in words:
        if word in vocabulary:
            # Word is correct
            suggestions.append(word)
        else:
            # Check cache first
            if word in cache:
                suggested_word = cache[word]
            else:
                # Find the closest word from the vocabulary
                min_distance = float('inf')
                suggested_word = word
                for vocab_word in vocabulary:
                    distance = edit_distance(word, vocab_word)
                    if distance < min_distance:
                        min_distance = distance
                        suggested_word = vocab_word
                # Add to cache
                cache[word] = suggested_word
            suggestions.append(suggested_word)
    return suggestions