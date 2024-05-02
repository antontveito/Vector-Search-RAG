import pymongo
import os
import requests

from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
HF_TOKEN = os.getenv('HF_TOKEN')
EMBEDDING_URL = 'https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2'

client = pymongo.MongoClient(MONGO_URI)
db = client.sample_mflix
collection = db.movies

def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        EMBEDDING_URL,
        headers={'Authorization': f'Bearer {HF_TOKEN}'},
        json={'inputs': text}
    )

    if response.status_code != 200:
        raise ValueError(f'Request failed with status code {response.status_code}: {response.text}')
    
    return response.json()

#Create embeddings for 50 movie plots
#for doc in collection.find({'plot':{"$exists": True}}).limit(50):
#    doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
#    collection.replace_one({'_id': doc['_id']}, doc)

query = 'A guy that fought in France during the world war 2'

results = collection.aggregate([
    {'$vectorSearch': {
        'queryVector': generate_embedding(query),
        'path': 'plot_embedding_hf',
        'numCandidates': 100,
        'limit': 1,
        'index': 'PlotSemanticSearch',
    }}
])

for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')