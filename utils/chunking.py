def read_file_in_chunks(file_object, chunk_size=124*124):

    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data