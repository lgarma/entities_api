"""Test main.py"""
import requests

oraciones = {
    "oraciones": [
        "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera."
    ]
}

response = requests.post(
    url="http://localhost:8000/entities/",
    json=oraciones
)
print(response.status_code)
print(response.json())
