"""API for entity recognition using the spacy library."""
from fastapi import FastAPI
from pydantic import BaseModel, Field
import spacy

app = FastAPI()

nlp = spacy.load("es_core_news_sm")


class Sentences(BaseModel):
    """Base class for typing validation of the request body."""
    sentences: list[str]
    # Field(description="List of sentences to be processed by the API.")


@app.post("/")
def get_entities(sentences: Sentences):
    """Return the named entities in a list of sentences.

    Parameters:
        sentences (Sentences):
        List of sentences to be processed by spacy.
    """
    response = {"resultado": []}
    for sentence in sentences.sentences:
        response = {"oración": sentence}
        doc = nlp(sentence)
        entities = [ent.text for ent in doc.ents]
        labels = [ent.label_ for ent in doc.ents]
        for entity, label in zip(entities, labels):
            response[entity] = label
        response["resultado"].append(response)
    return response

