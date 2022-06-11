# RssFeed

Only support Rss Feeds form BBC and CNN now  

# Installation
```
# linux  
python3 -m venv .venv
source .venv/bin/activate  
pip install -r requirements.txt  
  
# windows  
python -m venv .venv  
.venv/Scripts/activate
pip install -r requirements.txt  
```

# How to start
run
```
cd app/
uvicorn api:app
```
go to http://127.0.0.1:8000/docs to see documentation

# How to use
Method GET '/rss'  
url: RSS_URL  
limit: NUM_OF_PASSAGE_FETCH  
detail: true (get content of news)  

## Example
```
curl -X 'GET' \
  'http://127.0.0.1:8000/rss?url=http://feeds.bbci.co.uk/news/rss.xml&limit=2&detail=true' \
  -H 'accept: application/json'
```

```json
[
  {
    "title": "Rwanda asylum plan: UK court allows removal flight planned for Tuesday",
    "link": "https://www.bbc.co.uk/news/uk-61763818",
    "content": "A flight to take asylum seekers from the UK to Rwanda next Tuesday has been allowed to go ahead by the High Court.\n\nCampaigners failed in an initial legal bid to halt the removals to the east African country, but have confirmed they will take the case to the Court of Appeal on Monday..."
  },
  {
    "title": "Dom Phillips: Possible human remains found in hunt for journalist",
    "link": "https://www.bbc.co.uk/news/world-latin-america-61767385",
    "content": "Brazilian police have found possible human remains in their search for UK journalist Dom Phillips and indigenous expert Bruno Pereira.\n\nThe police say experts will analyse the \"organic material\" found in a river near the town of Atalaia do Norte in the remote Amazon rainforest..."
  }
]
```
