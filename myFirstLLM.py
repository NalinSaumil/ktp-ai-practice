from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import pinecone

#load pdf into langchain
loader = UnstructuredPDFLoader("C:\\Users\\saumi\\Desktop\\Spring-2023\\KTP\\KTP-AI\\data\\LIT_2331_syllabus_7.pdf")

data = loader.load()

#print(f'You have {len(data)} document(s) in your data')
#print(f'There are {len(data[0].page_content)} characters in your document')

#split pdf into multiple documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)

#print(f'Now you have {len(texts)} documents')

#print(texts[0])

#create OpenAI embeddings
embeddings = OpenAIEmbeddings(openai_api_key="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")

#initiate the pinecone
pinecone.init(
    api_key="9e7b6706-4c48-45e4-9b04-cf72b1780962",
    environment="us-east-1-aws"
)
#ref pinecone index
index_name = "langchain1"

#store embeddings into Pinecone
docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name = index_name)

#create the LLM
llm = OpenAI(temperature=0, openai_api_key="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")
chain = load_qa_chain(llm, chain_type="stuff")

#Enter Query and find relevant docs to answer query
count = 0;
while count == 0 :
    query = input("Enter your question: ")
    if query == "":
        break
    docs = docsearch.similarity_search(query, include_metadata=True)

    #Use relevant docs and query to answer with the LLM
    print(chain.run(input_documents=docs, question=query))

#print(docs)
