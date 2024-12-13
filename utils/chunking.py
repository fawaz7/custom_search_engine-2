def read_file_in_chunks(file_object, chunk_size=124*124):
    """
    Generator to read a file piece by piece. Default chunk size: 1MB.
    """
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data