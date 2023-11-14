# Import the libraries
from fastapi import FastAPI, Request
from transformers import pipeline
from pydantic import BaseModel
import hfloader            

app = FastAPI()     

#Funtion to load an api endpoint 
def LoadApiEndpoint (model):
	# Create a class for the input data
	class InputData(BaseModel):
		prompt: str

	# Create a class for the output data
	class OutputData(BaseModel):
		response: str


	#Loads a tokenizr and model for a specified model using the package HFLoader.
	tokenizer, model = hfloader.load_model(model)

	#Creates an agent pipeline that you can easily pipe information to.
	agent = pipeline("text-classification", tokenizer=tokenizer, model=model)

	# Create a route for the web application
	@app.post("/generate", response_model=OutputData)
	def generate(request: Request, input_data: InputData):
		prompt = input_data.prompt
		output = agent(prompt)[0]
		response = str(output)
		return OutputData(response=response)

	return app