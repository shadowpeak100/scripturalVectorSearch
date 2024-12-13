from simple_term_menu import TerminalMenu

def doVerseView(book, chapterNumber, verseNumber):
    pass

def doVersesView(book, chapterNumber):
    pass

def doChapterView(book):
    print("welcome to the book of " + book)
    pass

def doMainMenuView():
    print("Welcome to the Book Of Mormon study companion. Please select a book")
    options = ["1 Nephi", "2 Nephi", "Jacob", "Enos", "Jarom", "Omni", "Words of Mormon", "Mosiah", "Alma", "Helaman", "3 Nephi", "4 Nephi", "Mormon", "Ether", "Moroni", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index < len(options) - 1:
        doChapterView(options[menu_entry_index])
    else:
        print("Thank you for visiting, exiting program.")

def main():
    doMainMenuView()

if __name__ == "__main__":
    main()