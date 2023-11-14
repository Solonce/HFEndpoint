# HFEndpoint - Set up local API Endpoint for any HuggingFace model

### This package provides the user with one method that opens a local API endpoint for any from [HuggingFace Model Hub](https://huggingface.co/models). 

This package utilizes the `FastAPI` library to set up an API Endpoint under `127.0.0.1:8000/docs`. It also makes use of HuggingFace's `transformers` package, `pydantic`, and a package I created `hfloader`.  Which can be found [here](https://github.com/Solonce/HFLoader).

# Installation
The package can be installed with the following command:

    pip install hfendpoint

# How to Use
To use this package, all you need to do is import the package via this command.

    from hfendpoint import LoadApiEndpoint
The function `LoadApiEndpoint` expects one variable of type `str`. This can be a local path to a model, or any package on the [HuggingFace Model Hub](https://huggingface.co/models).

Usage may look something along the lines of:

    from hfendpoint import LoadApiEndpoint
    
    app = LoadApiEndpoint("cardiffnlp/twitter-roberta-base-sentiment")

### Important:
After running the script and loading the api endpoint, you have to call this command in cmd:

    uvicorn script:app --reload
 
 So, if the script that was written was called `script.py`, you need to exclude the `.py` in the command call.

## Requirements
> pip install transformers
> pip install fastapi
> pip install uvicorn
> pip install pydantic

## Notes
I don't have plans to upkeep this project unless it necessitates it. I was able to achieve the goal I had set out when developing the package.