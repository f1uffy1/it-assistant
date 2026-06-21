# it-assistant

Local AI troubleshooting tool for IT support. You describe a problem, it walks you through fixes.

Built this because I wanted to see if I could run an AI model completely locally without 
paying for an API. Ended up being a pretty useful tool for working through common help desk 
issues quickly.

## how it works

- Ollama runs Mistral 7B locally on your machine
- Flask serves a simple chat interface in the browser
- you type in an IT problem, the model responds with troubleshooting steps

## setup

1. install Ollama from ollama.com and run `ollama pull mistral`
2. install dependencies: `pip install -r requirements.txt`
3. run `python app.py`
4. open browser to http://127.0.0.1:5000

## tools used

- Python
- Flask
- Ollama (local AI runtime)
- Mistral 7B (the actual AI model)

## why local

didn't want to rely on an external API or pay per request. running it locally also means 
it works without internet which is useful in a data center environment