def generator_zero_chunks(code: str) -> str:
    """Generator that replace code chunks to 0000 starting from the end

    :param code: B001-00AA-0001-0002-0007
    :type code: str
    :return: "B001-00AA-0001-0002-0007", "B001-00AA-0001-0002-0000", "B001-00AA-0001-0000-0000", "B001-00AA-0000-0000-0000", "B001-0000-0000-0000-0000"
    :rtype: str
    """
    if code == "0000-0000-0000-0000-0000":
        raise Exception("Code has only 0000 chunks")

    chunks = code.split("-")
    if len(chunks) != 5:
        raise Exception("Code don't have 5 chunks separated by '-'")

    for index, chunk in enumerate(chunks):
        if len(chunk) != 4:
            raise Exception("Code chunks aren't equal 4 letters")
        if index < 4 and chunk == "0000" and chunks[index + 1] != "0000":
            raise Exception("'0000' chunk is followed by a non-zero chunk")

    number_of_zero_chunks = chunks.count("0000")

    for index in range(5 - number_of_zero_chunks):
        yield "-".join(chunks)
        chunks[4 - number_of_zero_chunks - index] = "0000"
