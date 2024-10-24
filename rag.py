import langchain_community

from langchain_community.document_loaders import HuggingFaceDatasetLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer, pipeline
from langchain.chains import RetrievalQA

# Define dataset and page content column
dataset_name = "datasets/Combined_Dataset.md"
page_content_column = "context"

# Load the dataset
loader = HuggingFaceDatasetLoader(dataset_name, page_content_column)
data = loader.load()

# Display first two entries for verification
print(data[:2])

# Split the text into manageable chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
docs = text_splitter.split_documents(data)

# Define model and encoding parameters for embeddings
model_path = "sentence-transformers/all-MiniLM-l6-v2"
model_kwargs = {'device': 'cuda'}
encode_kwargs = {'normalize_embeddings': False}

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name=model_path,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# Example document for querying
text = "This is a test document."
query_result = embeddings.embed_query(text)

# Display the first three query results
print(query_result[:3])

# Create a FAISS vector store from the documents and embeddings
db = FAISS.from_documents(docs, embeddings)

# Display the embeddings of the vector store
print(db.embeddings)

# Define the question to be answered
question = "What is cheesemaking?"
search_docs = db.similarity_search(question)

# Print the content of the most relevant document
print(search_docs[0].page_content)

# Define the model for question answering
model_name = "Intel/dynamic_tinybert"
tokenizer = AutoTokenizer.from_pretrained(model_name, padding=True, truncation=True, max_length=512)

# Create a question-answering pipeline
question_answerer = pipeline(
    "question-answering",
    model=model_name,
    tokenizer=tokenizer,
    return_tensors='pt'
)

# Wrap the pipeline with HuggingFacePipeline
llm = HuggingFacePipeline(
    pipeline=question_answerer,
    model_kwargs={"temperature": 0.7, "max_length": 512}
)

# Use the retriever to get relevant documents for a new question
retriever = db.as_retriever()
docs = retriever.get_relevant_documents("What is Machine learning?")

# Print the content of the retrieved document
print(docs[0].page_content)

# Set the retriever to return top 4 documents
retriever = db.as_retriever(search_kwargs={"k": 4})

# Create a RetrievalQA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="refine",
    retriever=retriever,
    return_source_documents=False
)

# Ask a question and print the result
question = "Who is Thomas Jefferson?"
result = qa.run({"query": question})
print(result["result"])