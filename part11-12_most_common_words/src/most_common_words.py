# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as file:
        full_doc = []
        for line in file:
            words = line.strip().split(" ")
            for word in words:
                full_doc.append(word.replace('.', '').replace(',', ''))

    return {item : full_doc.count(item) for item in full_doc if full_doc.count(item) >= lower_limit}

# print(most_common_words("programming.txt", 4))
