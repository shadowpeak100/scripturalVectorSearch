class BomRawLine:
    custom_id: str
    url: str
    verse: str
    verseNumber: str
    chapter: str
    book: str
    shortBookTitle: str

    def createUniqueID(self):
        self.custom_id = self.shortBookTitle + ":" + self.chapter + ":" + self.verseNumber

    def buildWebLink(self):
        weblinkPrefix = "https://www.churchofjesuschrist.org/study/scriptures/bofm/"
        weblinkSuffix = "?lang=eng"
        #https://www.churchofjesuschrist.org/study/scriptures/bofm/moro/5?lang=eng
        self.url = weblinkPrefix + self.shortBookTitle + "/" + self.chapter + "/" + weblinkSuffix

    def to_dict(self):
        return {
            "custom_id": self.custom_id,
            "url": self.url,
            "verse": self.verse,
            "verseNumber": self.verseNumber,
            "chapter": self.chapter,
            "book": self.book,
            "shortBookTitle": self.shortBookTitle
        }


