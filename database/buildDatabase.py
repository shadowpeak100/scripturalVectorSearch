import os

from dotenv import load_dotenv
import psycopg2

load_dotenv()
CONNECTION = os.getenv("DB_CONNECTION_STRING")
# need to run this to enable vector data type
CREATE_EXTENSION = "CREATE EXTENSION vector"


DROP_TABLE_BOM = """
DROP TABLE IF EXISTS bom
"""

CREATE_BOM_TABLE = """
CREATE TABLE bom (
    custom_id TEXT PRIMARY KEY,
    url TEXT,
    verse TEXT,
    verseNumber Text,
    chapter Text,
    book TEXT,
    shortBookTitle TEXT,
    vector VECTOR(1536)
);
"""

with psycopg2.connect(CONNECTION) as conn:
    cursor = conn.cursor()
    # make the tables
    # apparently this exists already to commenting out for now but required for new builds
    # cursor.execute(CREATE_EXTENSION)
    # cursor.execute(DROP_TABLE_BOM)
    # cursor.execute(CREATE_BOM_TABLE)

    cursor.execute("SELECT * FROM bom LIMIT 10")
    resultRestaurants = cursor.fetchall()

    for row in resultRestaurants:
        print(row)