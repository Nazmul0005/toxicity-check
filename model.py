# Modern approach using transformers
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="unitary/toxic-bert" 
    #small model : Model	Size	Architecture
    #unitary/toxic-bert	~438MB	BERT-base
    #martin-ha/toxic-comment-model	~267MB	DistilBERT
    #s-nlp/roberta_toxicity_classifier	~150MB	Mini RoBERTa
)
