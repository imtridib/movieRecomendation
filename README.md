# Movie Recommendation System

A Streamlit web app that recommends five similar movies from a selected title and displays their posters. It loads a movie catalogue and precomputed similarity data from local pickle files.

## Features

- Select a movie from a dropdown.
- Retrieve the five nearest recommendations from the precomputed similarity scores.
- Display movie posters using The Movie Database (TMDB) API.

## Tech stack

- Python
- Streamlit
- Pandas
- Requests
- Pickle files containing the movie catalogue and similarity data

## Run locally

Use Python 3.10+ as a starting point; older environments may be needed if the saved pickle files were generated with different library versions.

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

**macOS/Linux**
```bash
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The repository must contain the compatible `movie_dict.pkl` and `similarity.pkl` assets in the project root. The similarity file is stored through Git LFS; ensure Git LFS is installed and the actual asset has been downloaded before launching the app.

## Important security note

Before using or publishing this project, rotate any TMDB credential that has ever been committed to the source code. Do not commit API keys. A follow-up improvement is to load the key from an environment variable and provide a `.env.example` file containing only a placeholder.

## Limitations

Recommendations depend on the supplied precomputed similarity matrix and catalogue. This repository does not currently document the original dataset preparation or similarity-matrix generation pipeline, so the model/data preparation process is not fully reproducible from the app alone.
