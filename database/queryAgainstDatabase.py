import ast
import os

import numpy as np
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()
CONNECTION = os.getenv("DB_CONNECTION_STRING")

with psycopg2.connect(CONNECTION) as conn:
    cursor = conn.cursor()
    query = f"""
        WITH query_embedding AS (
            SELECT embedding
            FROM podcast_segment
            WHERE id = %s
        ),
        not_similar_segments AS (
            SELECT 
                ps.id AS segment_id,
                p.title AS podcast_title,
                ps.content AS segment_content,
                ps.start_time,
                ps.end_time,
                ps.embedding,
                ps.embedding <-> query_embedding.embedding AS distance
            FROM podcast_segment ps
            CROSS JOIN query_embedding
            JOIN podcast p ON ps.podcast_id = p.id
            WHERE ps.id <> %s
            ORDER BY distance DESC
            LIMIT 5
        )
        SELECT 
            podcast_title, 
            segment_id, 
            segment_content, 
            start_time, 
            end_time, 
            distance
        FROM not_similar_segments;
        """

    cursor.execute(query, (query_segment_id, query_segment_id))

    columns = ['podcast_title', 'segment_id', 'segment_content', 'start_time', 'end_time', 'distance']
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=columns)
    print(results)


def getChaptersOfBook(bookTitle):
    load_dotenv()
    CONNECTION = os.getenv("DB_CONNECTION_STRING")

    # Query the database
    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()

        query = "SELECT chapter FROM bom WHERE book = %s"
        cursor.execute(query, (bookTitle,))

        chapters = [row[0] for row in cursor.fetchall()]

    # Print the result
    print(chapters)
    return chapters