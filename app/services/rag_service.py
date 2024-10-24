# app/services/rag_service.py
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

def enrich_data_with_rag(query: str, dataset):
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
    retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", index_name="exact", indexed_dataset=dataset)
    rag_model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq", retriever=retriever)

    input_ids = tokenizer(query, return_tensors="pt").input_ids
    output_ids = rag_model.generate(input_ids, num_return_sequences=1)
    generated_output = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0]
    return generated_output
