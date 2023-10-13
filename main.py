"""API for entity recognition using the spacy library."""
from typing import Any

from fastapi import FastAPI
import spacy

app = FastAPI()

nlp = spacy.load("es_core_news_sm")


@app.post("/entities/")
def get_entities(sentences: dict[str, list[str]]) -> dict[str, Any]:
    """Return the named entities in a list of sentences.

    Parameters:
        sentences (Sentences):
        List of sentences to be processed by spacy.
    """
    response = []
    for sentence in sentences["oraciones"]:
        sentence_response = {"oración": sentence, "entidades": {}}
        doc = nlp(sentence)
        for ent in doc.ents:
            sentence_response["entidades"][ent.text] = ent.label_
        response.append(sentence_response)
    return {"resultado": response}
