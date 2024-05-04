from llama_index.core import VectorStoreIndex
from llama_index.readers.file import PDFReader
from pathlib import Path

pdfReader = PDFReader()

# load idexx
idexxPdf = Path("./data/idexx/4682_BN661250-1_20240416_153637_2129.pdf")
idexxDocs = pdfReader.load_data(idexxPdf)

# load vetscan
vetscanPdf = Path("./data/vetscan/4683_20240416_1552.pdf")
vetscanDocs = pdfReader.load_data(vetscanPdf)

# create index
documents = idexxDocs + vetscanDocs
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("display data as CSV")

print(response)