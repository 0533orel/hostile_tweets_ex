# Malicious Text Feature Engineering API

A tiny FastAPI service that:
- Fetches documents from MongoDB
- Engineers simple text features
- Serves the processed data via REST

## Quick Start (Local)
```bash
pip install -r requirements.txt

# set your DB connection
export MONGO_URI="YOUR_MONGO_URI"           # required
export MONGO_DB="IranMalDB"                 # optional (default)
export MONGO_COLLECTION="tweets"            # optional (default)

uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open:  
- `GET /health` → `{"ok": true}`  
- `GET /get_data_processed` → JSON list with: `id`, `original_text`, `rarest_word`, `sentiment`, `weapons_detected`

## Docker
```bash
docker build -t hostile-tweets-ex:latest .
docker run --rm -p 8000:8000   -e MONGO_URI="YOUR_MONGO_URI"   -e MONGO_DB="IranMalDB"   -e MONGO_COLLECTION="tweets"   hostile-tweets-ex:latest
```

> Tip (NLTK): if the cluster cannot download data at runtime, bake VADER into the image:
> 
> ```dockerfile
> RUN python -c "import nltk; nltk.download('vader_lexicon')"
> ```

## OpenShift (Very Short)
Apply your manifests (deployment/service/route/secret/configmap) from `infra/` **or** repo root, e.g.:
```bash
oc apply -f secrets.yaml
oc apply -f configmap.yaml
oc apply -f deployment.yaml
oc apply -f service.yaml
oc apply -f route.yaml
```
Then:
```bash
oc rollout status deployment/hostile-tweets
oc get route
```

## Notes
- Make sure `data/weapons.txt` is included in the image (e.g., `COPY data/weapons.txt ...`).
- The fetcher expects a text field named `Text` in MongoDB documents. Adjust if your schema differs.
