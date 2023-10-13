"""API for entity recognition using the spacy library."""
from typing import Any
from pydantic import BaseModel, Field
from fastapi import FastAPI
import spacy

app = FastAPI()

nlp = spacy.load("es_core_news_sm")


class SentencesRequest(BaseModel):
    """Request model for the get_entities endpoint.

    Attributes:
        oraciones (list[str]): List of sentences to be processed by spacy.
    """
    oraciones: list[str] = Field(..., example=[
        "Apple está buscando comprar una startup del Reino Unido por mil millones "
        "de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera."]
                                 )


@app.post("/entities/")
def get_entities(sentences: SentencesRequest) -> dict[str, Any]:
    """Get named entities from a list of sentences.

    Parameters:
        sentences (dict[str, list[str]]):
        List of sentences to be processed by spacy.

    Returns:
        dict[str, Any]: Dictionary with the sentences and their entities.
    """
    response = []
    for sentence in sentences.oraciones:
        sentence_response = {"oración": sentence, "entidades": {}}
        doc = nlp(sentence)
        for ent in doc.ents:
            sentence_response["entidades"][ent.text] = ent.label_
        response.append(sentence_response)
    return {"resultado": response}
