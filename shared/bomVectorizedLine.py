from shared.bomRawLine import BomRawLine


class BomVectorizedLine:
    rawLine: BomRawLine
    vector: list

    def __init__(self):
        self.rawLine = BomRawLine()

    def completeObject(self):
        if self.vector is None:
            return False
        if self.rawLine is None:
            return False
        if self.rawLine.custom_id is None:
            return False
        if self.rawLine.url is None:
            return False
        if self.rawLine.verse is None:
            return False
        if self.rawLine.verseNumber is None:
            return False
        if self.rawLine.chapter is None:
            return False
        if self.rawLine.book is None:
            return False
        if self.rawLine.shortBookTitle is None:
            return False
        return True

    def to_dict(self):
        return {
            "custom_id": self.rawLine.custom_id,
            "url": self.rawLine.url,
            "verse": self.rawLine.verse,
            "verseNumber": self.rawLine.verseNumber,
            "chapter": self.rawLine.chapter,
            "book": self.rawLine.book,
            "shortBookTitle": self.rawLine.shortBookTitle,
            "vector": self.vector,
        }

    def from_dict(self, dictionary):
        self.rawLine.from_dict(dictionary)
        if "vector" in dictionary:
            self.vector = dictionary["vector"]