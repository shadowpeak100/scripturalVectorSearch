import json
import os
import pandas as pd

from dotenv import load_dotenv

from database.fastInsert import fast_pg_insert
from shared.bomRawLine import BomRawLine
from shared.bomVectorizedLine import BomVectorizedLine

load_dotenv()

bomVectorizedFilePath = os.getenv("BOM_VECTORIZED_FILE_PATH")

id_info_map = {}

with open(bomVectorizedFilePath, 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line.strip())
        bomRawLine = BomRawLine()

        bomRawLine.custom_id = data.get('custom_id')
        bomRawLine.url = data.get('url')
        bomRawLine.verse = data.get('verse')
        bomRawLine.verseNumber = data.get('verseNumber')
        bomRawLine.chapter = data.get('chapter')
        bomRawLine.book = data.get('book')
        bomRawLine.shortBookTitle = data.get('shortBookTitle')

        info_object = BomVectorizedLine()
        info_object.rawLine = bomRawLine
        info_object.vector = data.get('vector')
        id_info_map[bomRawLine.custom_id] = info_object

CONNECTION = os.getenv("DB_CONNECTION_STRING")

bom_data = [
    {
        'custom_id': bomVectorLine.rawLine.custom_id,
        'url': bomVectorLine.rawLine.url,
        'verse': bomVectorLine.rawLine.verse,
        'verseNumber': bomVectorLine.rawLine.verseNumber,
        'chapter': bomVectorLine.rawLine.chapter,
        'book': bomVectorLine.rawLine.book,
        'shortBookTitle': bomVectorLine.rawLine.shortBookTitle,
        'vector': bomVectorLine.vector,
    }
    for bomVectorLine in id_info_map.values()
]

df = pd.DataFrame(bom_data)
fast_pg_insert(df, CONNECTION, "bom", ["custom_id", "url", "verse", "versenumber", "chapter", "book", "shortbooktitle", "vector"])
