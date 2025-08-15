# Modern approach using transformers
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="unitary/toxic-bert"
)
