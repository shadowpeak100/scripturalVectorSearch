import argparse
import re
import openai
import json

parser = argparse.ArgumentParser(description='Handle connection string input')
    # Argument gets passed in as: """ -k="Your key HERE" """
parser.add_argument('-k', type=str, required=True,
                        help='key for open ai')

args = parser.parse_args()

openai.api_key = args.k

# Function to check if a line matches the pattern (number: number)
def matches_pattern(line):
    return re.match(r'^\d+:\d+', line) is not None

def get_embeddings(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']

results = []

with open('your_file.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if matches_pattern(line):
            print(f"Processing line: {line}")
            embedding = get_embeddings(line)
            results.append({
                "line": line,
                "embedding": embedding
            })

with open('results.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

print("Embeddings saved to results.json")