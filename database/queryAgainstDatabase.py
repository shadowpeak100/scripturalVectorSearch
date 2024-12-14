import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
CONNECTION = os.getenv("DB_CONNECTION_STRING")

def get5MostDissimilarEntriesFromVector(input_vector):
    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()

        query = """
        WITH query_vector AS (
            SELECT %s::VECTOR(1536) AS vector
        )
        SELECT
            b.custom_id,
            b.url,
            b.verse,
            b.verseNumber,
            b.chapter,
            b.book,
            b.shortBookTitle,
            b.vector <-> query_vector.vector AS distance
        FROM bom b
        CROSS JOIN query_vector
        ORDER BY distance DESC
        LIMIT 5;
        """

        cursor.execute(query, (input_vector,))

        columns = [
            'custom_id',
            'url',
            'verse',
            'verseNumber',
            'chapter',
            'book',
            'shortBookTitle',
            'distance'
        ]

        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=columns)

        return df


def get5MostSimilarEntriesFromVector(input_vector):
    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()

        query = """
        WITH query_vector AS (
            SELECT %s::VECTOR(1536) AS vector
        )
        SELECT
            b.custom_id,
            b.url,
            b.verse,
            b.verseNumber,
            b.chapter,
            b.book,
            b.shortBookTitle,
            b.vector <-> query_vector.vector AS distance
        FROM bom b
        CROSS JOIN query_vector
        ORDER BY distance
        LIMIT 5;
        """

        cursor.execute(query, (input_vector,))

        columns = [
            'custom_id',
            'url',
            'verse',
            'verseNumber',
            'chapter',
            'book',
            'shortBookTitle',
            'distance'
        ]

        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=columns)

        return df

def bookChapterVerseToID(bookTitle, chapterNumber, verseNumber):
    mapping = {"1 Nephi": "1-ne",
    "2 Nephi": "2-ne",
    "Jacob": "jacob",
    "Enos": "enos",
    "Jarom": "jarom",
    "Omni": "omni",
    "Words of Mormon": "w-of-m",
    "Mosiah": "mosiah",
    "Alma": "alma",
    "Helaman": "hel",
    "3 Nephi": "3-ne",
    "4 Nephi": "4-ne",
    "Mormon": "morm",
    "Ether": "ether",
    "Moroni": "moro",}

    return mapping[bookTitle] + ":" + str(chapterNumber) + ":" + str(verseNumber)

def get5SimilarVerses(bookTitle, chapterNumber, verseNumber):
    verseId = bookChapterVerseToID(bookTitle, chapterNumber, verseNumber)

    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()

        query = """
        WITH query_vector AS (
            SELECT vector
            FROM bom
            WHERE custom_id = %s
        )
        SELECT
            b.custom_id,
            b.url,
            b.verse,
            b.verseNumber,
            b.chapter,
            b.book,
            b.shortBookTitle,
            b.vector <-> query_vector.vector AS distance
        FROM bom b
        CROSS JOIN query_vector
        WHERE b.custom_id <> %s
        ORDER BY distance
        LIMIT 5;
        """

        cursor.execute(query, (verseId, verseId))

        columns = [
            'custom_id',
            'url',
            'verse',
            'verseNumber',
            'chapter',
            'book',
            'shortBookTitle',
            'distance'
        ]
        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=columns)

        return df

def get5DissimilarVerses(bookTitle, chapterNumber, verseNumber):
    verseId = bookChapterVerseToID(bookTitle, chapterNumber, verseNumber)
    print(verseId)

    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()

        query = """
        WITH query_vector AS (
            SELECT vector
            FROM bom
            WHERE custom_id = %s
        )
        SELECT
            b.custom_id,
            b.url,
            b.verse,
            b.verseNumber,
            b.chapter,
            b.book,
            b.shortBookTitle,
            b.vector <-> query_vector.vector AS distance
        FROM bom b
        CROSS JOIN query_vector
        WHERE b.custom_id <> %s
        ORDER BY distance DESC
        LIMIT 5;
        """

        cursor.execute(query, (verseId, verseId))

        columns = [
            'custom_id',
            'url',
            'verse',
            'verseNumber',
            'chapter',
            'book',
            'shortBookTitle',
            'distance'
        ]
        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=columns)

        return df


def getVerseOfVerseChapterBook(bookTitle, chapterNumber, verseNumber):
    load_dotenv()
    CONNECTION = os.getenv("DB_CONNECTION_STRING")

    # Query the database
    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()

        query = "SELECT verse FROM bom WHERE book = %s AND chapter = %s AND versenumber = %s"
        cursor.execute(query, (bookTitle,chapterNumber,verseNumber))

        verse = [row[0] for row in cursor.fetchall()]

    return verse

def getVersesOfChapterBook(bookTitle, chapterNumber):
    load_dotenv()
    CONNECTION = os.getenv("DB_CONNECTION_STRING")

    # Query the database
    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()

        query = "SELECT DISTINCT versenumber FROM bom WHERE book = %s AND chapter = %s"
        cursor.execute(query, (bookTitle,chapterNumber))

        verses = [row[0] for row in cursor.fetchall()]
        sortedVerses = sorted(verses, key=int)

    return sortedVerses

def getChaptersOfBook(bookTitle):
    load_dotenv()
    CONNECTION = os.getenv("DB_CONNECTION_STRING")

    # Query the database
    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()

        query = "SELECT DISTINCT chapter FROM bom WHERE book = %s"
        cursor.execute(query, (bookTitle,))


        chapters = [row[0] for row in cursor.fetchall()]
        sorted_chapters = sorted(chapters, key=int)

    return sorted_chapters