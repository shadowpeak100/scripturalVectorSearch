import argparse
import re
import json

from shared.bomRawLine import BomRawLine


# I acknowledge this code is a bit rigid, the gutenberg txt file is helpful but needs some formatting help

def main():
    parser = argparse.ArgumentParser(description='Handle connection string input')

    # Argument gets passed in as: """ -f="Your File HERE" """

    parser.add_argument('-f', type=str, required=True,
                        help='file to raw book of mormon text file')

    parser.add_argument('-o', type=str, required=True,
                        help='output file path')

    args = parser.parse_args()

    iterateFile(args.f, args.o)

def iterateFile(inputFilePath, outputFilePath):
    #for simplicity we are just looking at BOM verses so we will skip the intro information
    inBomProper = False

    with open(inputFilePath, 'r') as file, open(outputFilePath, 'w') as outputFile:
        lineObject = BomRawLine()
        currentlyInVerse = False

        for line in file:
            line = line.strip()

            #skip the introduction parts
            if not inBomProper and line == "THE FIRST BOOK OF NEPHI HIS REIGN AND MINISTRY (1 Nephi)":
                inBomProper = True

            if inBomProper:
                if isEndOfBom(line):
                    return
                if currentlyInVerse:
                    if line == "":
                        currentlyInVerse = False
                        # write line
                        lineObject.createUniqueID()
                        lineObject.buildWebLink()
                        json_data = json.dumps(lineObject.to_dict())
                        outputFile.write(json_data + "\n")
                        continue
                    else:
                        lineObject.verse += " " + line
                        continue
                if line == "":
                    # just a blank line
                    currentlyInVerse = False
                    continue

                if isHeader(line):
                    lineObject.book , lineObject.shortBookTitle = newBookTitles(line)
                # if none of the above we are likely at a new verse
                if isVerse(line):
                    lineObject.chapter, lineObject.verseNumber, lineObject.verse = extractChapterVerse(line)
                    currentlyInVerse = True


def extractChapterVerse(line):
    match = re.match(r'^(\d+):(\d+)\s*(.*)', line)

    if match:
        num1 = match.group(1)
        num2 = match.group(2)
        text = match.group(3)
        return num1, num2, text
    else:
        return None, None, None

def isEndOfBom(line):
    return line == "*** END OF THE PROJECT GUTENBERG EBOOK THE BOOK OF MORMON ***"

def isVerse(line):
    return re.match(r'^\d+:\d+', line) is not None

def isHeader(line):
    if line == "THE FIRST BOOK OF NEPHI HIS REIGN AND MINISTRY (1 Nephi)":
        return True
    elif line == "THE SECOND BOOK OF NEPHI":
        return True
    elif line == "THE BOOK OF JACOB":
        return True
    elif line == "THE BOOK OF ENOS":
        return True
    elif line == "THE BOOK OF JAROM":
        return True
    elif line == "THE BOOK OF OMNI":
        return True
    elif line == "THE BOOK OF JAROM":
        return True
    elif line == "THE WORDS OF MORMON":
        return True
    elif line == "THE BOOK OF MOSIAH":
        return True
    elif line == "THE BOOK OF ALMA":
        return True
    elif line == "THE BOOK OF HELAMAN":
        return True
    elif line == "THIRD BOOK OF NEPHI":
        return True
    elif line == "FOURTH NEPHI":
        return True
    elif line == "THE BOOK OF MORMON":
        return True
    elif line == "THE BOOK OF ETHER":
        return True
    elif line == "THE BOOK OF MORONI":
        return True
    else:
        return False

def newBookTitles(line):
    # returns the name in plain english and the way the name is used in a URL
    if line == "THE FIRST BOOK OF NEPHI HIS REIGN AND MINISTRY (1 Nephi)":
        return "1 Nephi", "1-ne"
    elif line == "THE SECOND BOOK OF NEPHI":
        return "2 Nephi", "2-ne"
    elif line == "THE BOOK OF JACOB":
        return "Jacob", "jacob"
    elif line == "THE BOOK OF ENOS":
        return "Enos", "enos"
    elif line == "THE BOOK OF JAROM":
        return "Jarom", "jarom"
    elif line == "THE BOOK OF OMNI":
        return "Omni", "omni"
    elif line == "THE BOOK OF JAROM":
        return "Jarom", "jarom"
    elif line == "THE WORDS OF MORMON":
        return "Words of Mormon", "w-of-m"
    elif line == "THE BOOK OF MOSIAH":
        return "Mosiah", "mosiah"
    elif line == "THE BOOK OF ALMA":
        return "Alma", "alma"
    elif line == "THE BOOK OF HELAMAN":
        return "Helaman", "hel"
    elif line == "THIRD BOOK OF NEPHI":
        return "3 Nephi", "3-ne"
    elif line == "FOURTH NEPHI":
        return "4 Nephi", "4-ne"
    elif line == "THE BOOK OF MORMON":
        return "Mormon", "morm"
    elif line == "THE BOOK OF ETHER":
        return "Ether", "ether"
    elif line == "THE BOOK OF MORONI":
        return "Moroni", "moro"
    else:
        return "", ""

if __name__ == '__main__':
    main()
