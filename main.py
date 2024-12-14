import shutil
import textwrap
from simple_term_menu import TerminalMenu
from database.queryAgainstDatabase import *
from printables import *
from vectorize.vectorize import get_embeddings


def printGreen(str) -> str:
    return "\033[32m" + str + "\033[0m"

def printRed(str) -> str:
    return "\033[31m" + str + "\033[0m"

def printYellow(str) -> str:
    return "\033[33m" + str + "\033[0m"

def printBlue(str) -> str:
    return "\033[34m" + str + "\033[0m"

def printCyan(str) -> str:
    return "\033[36m" + str + "\033[0m"

def printMagenta(str) -> str:
    return "\033[35m" + str + "\033[0m"

def printWhite(str) -> str:
    return "\033[37m" + str + "\033[0m"

def printBlack(str) -> str:
    return "\033[30m" + str + "\033[0m"

def clear_screen():
    print("\033[H\033[2J", end="")

def line():
    return "--------------------"

def pretty_print(text, max_width=80):
    terminal_width = shutil.get_terminal_size().columns
    effective_width = min(max_width, terminal_width)
    return textwrap.fill(text, width=effective_width)

def doVerseView(book, chapterNumber, verseNumber):
    print(printRed(line()))
    print(printBlue("You are viewing " + book + " chapter " + str(chapterNumber) + " verse " + verseNumber))
    verse = getVerseOfVerseChapterBook(book, str(chapterNumber), str(verseNumber))

    if len(verse) == 0:
        print("No verse found for this chapter book verse combination")
        doVerseView(book, chapterNumber)

    print("\n" + pretty_print(verse[0]) + "\n")

    menu_entry_index = 0
    while menu_entry_index == 0 or menu_entry_index == 1:
        options = ["Get 5 most similar scriptures", "Get 5 most dissimilar scriptures", "Return to verses view"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()


        if menu_entry_index == 0:
            verses = get5SimilarVerses(book, chapterNumber, verseNumber)
            print(printGreen("The 5 most similar scriptures are:\n"))
            for i in range(len(verses)):
                bookNum = verses.at[i, 'book']
                chapterNum = verses.at[i, 'chapter']
                verseNum = verses.at[i, 'verseNumber']
                verse_text = verses.at[i, 'verse']
                similarity = verses.at[i, 'distance']
                output = pretty_print(verse_text)
                print(printGreen("similarity score: " + str(similarity)))
                print(printCyan(str(bookNum) + " " + str(chapterNum) + ":" + str(verseNum)))
                print(output + "\n")

        elif menu_entry_index == 1:
            verses = get5DissimilarVerses(book, chapterNumber, verseNumber)
            print(printRed("The 5 most dissimilar scriptures are:\n"))
            for i in range(len(verses)):
                bookNum = verses.at[i, 'book']
                chapterNum = verses.at[i, 'chapter']
                verseNum = verses.at[i, 'verseNumber']
                verse_text = verses.at[i, 'verse']
                similarity = verses.at[i, 'distance']
                output = pretty_print(verse_text)
                print(printRed("similarity score: " + str(similarity)))
                print(printCyan(str(bookNum) + " " + str(chapterNum) + ":" + str(verseNum)))
                print(output + "\n")

        else:
            doVersesView(book, chapterNumber)


def doVersesView(book, chapterNumber):
    print(printRed(line()))
    print(printBlue("You are viewing " + book + " chapter " + str(chapterNumber)))
    verses = getVersesOfChapterBook(book, str(chapterNumber))
    verses.append("Back to chapter view")
    terminal_menu = TerminalMenu(verses)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index < len(verses) - 1:
        doVerseView(book, chapterNumber, verses[menu_entry_index])
    else:
        doChapterView(book)

def doChapterView(book):
    print(printRed(line()))
    print(printBlue("Welcome to the book of " + book))
    chapters = getChaptersOfBook(book)
    chapters.append("Back to main menu")
    terminal_menu = TerminalMenu(chapters)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index < len(chapters) - 1:
        doVersesView(book, chapters[menu_entry_index])
    else:
        doMainMenuView()

def doMainMenuView():
    print(printRed(line()))
    printSlice = [liahona, america, oliveTree, prayer, commandments, crown, dove, towerOfBenjamin, sword, spear, glory, cornocopia, war, stones, plates]
    print(printBlue("Welcome to the Book Of Mormon study companion. Please select a book"))

    options = ["1 Nephi", "2 Nephi", "Jacob", "Enos", "Jarom", "Omni", "Words of Mormon", "Mosiah", "Alma", "Helaman", "3 Nephi", "4 Nephi", "Mormon", "Ether", "Moroni", "Custom", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index < len(options) - 2:
        print(printYellow(printSlice[menu_entry_index]()))
        doChapterView(options[menu_entry_index])
    elif menu_entry_index == len(options) - 2:
        doCustomView()
    else:
        print(printRed(line()))
        print("Thank you for visiting, exiting program.")

def doCustomView():
    print("doing custom view")
    print(printRed(line()))
    print(printBlue("Please type a text you would like to compare to the scriptures"))
    user_input = input()
    user_input_vector = get_embeddings(user_input)

    menu_entry_index = 0
    while menu_entry_index == 0 or menu_entry_index == 1:
        options = ["Get 5 most similar scriptures", "Get 5 most dissimilar scriptures", "Back to main menu"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            verses = get5MostSimilarEntriesFromVector(user_input_vector)
            print(printGreen("The 5 most similar scriptures are:\n"))
            for i in range(len(verses)):
                bookNum = verses.at[i, 'book']
                chapterNum = verses.at[i, 'chapter']
                verseNum = verses.at[i, 'verseNumber']
                verse_text = verses.at[i, 'verse']
                similarity = verses.at[i, 'distance']
                output = pretty_print(verse_text)
                print(printGreen("similarity score: " + str(similarity)))
                print(printCyan(str(bookNum) + " " + str(chapterNum) + ":" + str(verseNum)))
                print(output + "\n")

        elif menu_entry_index == 1:
            verses = get5MostDissimilarEntriesFromVector(user_input_vector)
            print(printRed("The 5 most dissimilar scriptures are:\n"))
            for i in range(len(verses)):
                bookNum = verses.at[i, 'book']
                chapterNum = verses.at[i, 'chapter']
                verseNum = verses.at[i, 'verseNumber']
                verse_text = verses.at[i, 'verse']
                similarity = verses.at[i, 'distance']
                output = pretty_print(verse_text)
                print(printRed("similarity score: " + str(similarity)))
                print(printCyan(str(bookNum) + " " + str(chapterNum) + ":" + str(verseNum)))
                print(output + "\n")
        else:
            doMainMenuView()

def main():
    doMainMenuView()

if __name__ == "__main__":
    main()