# Movie Recommendation System

A Streamlit web app that recommends five similar movies from a selected title and displays their posters. It loads a movie catalogue and precomputed similarity data from local pickle files.

## Features

- Select a movie from a dropdown.
- Retrieve the five nearest recommendations from precomputed similarity scores.
- Display movie posters using The Movie Database (TMDB) API.

## Tech stack

- Python, Streamlit, Pandas, Requests
- Pickle files containing the movie catalogue and similarity data

## Run locally

Use Python 3.10+ as a starting point; the saved pickle assets may require compatible library versions.

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:TMDB_API_KEY="your_tmdb_api_key"
streamlit run app.py
```

**macOS/Linux**
```bash
source .venv/bin/activate
pip install -r requirements.txt
export TMDB_API_KEY="your_tmdb_api_key"
streamlit run app.py
```

The repository needs compatible `movie_dict.pkl` and `similarity.pkl` assets in the project root. The similarity file is stored through Git LFS, so install Git LFS and download the actual asset before launching the app.

## Security

The app reads the TMDB credential from the `TMDB_API_KEY` environment variable. A credential was previously present in the source code; rotate it in your TMDB account because changing the current file does not remove it from Git history. Never commit real API keys.

## Limitations

Recommendations depend on the precomputed similarity matrix and catalogue. The data preparation and matrix-generation pipeline are not currently documented, so the full recommendation pipeline is not reproducible from the app alone.