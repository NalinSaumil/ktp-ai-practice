from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import os

os.environ['OPENAI_API_KEY']= "INSERT KEY HERE" # add openai api key here

prompt_helper = PromptHelper(max_input_size=4096, num_output=256, max_chunk_overlap=20, chunk_size_limit=600)

llm_p = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))

documents = SimpleDirectoryReader("C:\\Users\\saumi\\Desktop\\Spring-2023\\KTP\\KTP-AI\\data_dir").load_data() #Import pdf directory for data here

index = GPTSimpleVectorIndex.from_documents(documents=documents)

index.save_to_disk("index.json")

index = GPTSimpleVectorIndex.load_from_disk("index.json")

count = 0
while count == 0 :
    query = input("Enter your question: ")
    if query == "":
        break
    response = index.query(query)
    print(response)