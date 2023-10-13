# Entity recognition API

Send a POST request with a list of sentences to be analyzed by spacy.

## Getting started

- Clone the repository

```bash
git clone
```

- Install Poetry

```bash 
pip install poetry
```

- Install dependencies from pyproject, and activate the virtual environment

```bash
poetry install
poetry shell
```

- Download the spacy model

```bash
python -m spacy download es_core_web_sm
```

- Run the local server

```bash
uvicorn main:app --reload
```

- Test the entities endpoint in http://localhost:8000/docs using the
following format:

```json
{
  "oraciones": [
    "Apple es una empresa de tecnología",
    "El Gran Cañón es un impresionante lugar en Arizona.",
    "La ONU trabaja en la promoción de la paz mundial."
  ]
}
```
