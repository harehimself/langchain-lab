## Import necessary components from LangChain
from langchain.llms import OpenAI
from langchain.chains import SingleLM

## Initialize the language model with your API key
## Replace "your-api-key" with your actual OpenAI API key
llm = OpenAI(api_key="your-api-key")

## Create a chain with the language model
chain = SingleLM(llm)

## Define a prompt to process
prompt = "What is the capital of France?"

## Use the chain to generate a response to the prompt
response = chain.run(prompt)

## Print the response
print(response)

## Replace "your-api-key" with your actual OpenAI API key.
## Ensure that LangChain is installed in your Python environment. If not, install it using pip install langchain.
## Save the script in a .py file, e.g., langchain_example.py.
## Run the script in your Python environment.
