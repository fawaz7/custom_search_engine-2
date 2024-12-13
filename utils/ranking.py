def rank_results(results, inverted_index, words):
    file_scores = {}
    
    # Extract unique file paths from results
    unique_files = set(file_path for file_path, _ in results)
    
    # Calculate score and track lines for each unique file
    for file_path in unique_files:
        if file_path not in file_scores:
            file_scores[file_path] = {'score': 0, 'lines': set()}
        
        for word in words:
            if word in inverted_index:
                # Get all occurrences of the word in the current file
                occurrences = [loc for loc in inverted_index[word] if loc[0] == file_path]
                file_scores[file_path]['score'] += len(occurrences)  # Increment by total occurrences
                for loc in occurrences:
                    file_scores[file_path]['lines'].add(loc[1])  # Add line numbers
    
    # Convert to a list of tuples and sort by score in descending order
    ranked_results = sorted(file_scores.items(), key=lambda x: x[1]['score'], reverse=True)
    
    return ranked_results