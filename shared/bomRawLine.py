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

    def from_dict(self, dictionary):
        if "custom_id" in dictionary:
            self.custom_id = dictionary["custom_id"]
        if "url" in dictionary:
            self.url = dictionary["url"]
        if "verse" in dictionary:
            self.verse = dictionary["verse"]
        if "verseNumber" in dictionary:
            self.verseNumber = dictionary["verseNumber"]
        if "chapter" in dictionary:
            self.chapter = dictionary["chapter"]
        if "book" in dictionary:
            self.book = dictionary["book"]
        if "shortBookTitle" in dictionary:
            self.shortBookTitle = dictionary["shortBookTitle"]



