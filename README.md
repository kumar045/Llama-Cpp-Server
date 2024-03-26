# Llama-Cpp-Server

- Git clone https://github.com/ggerganov/llama.cpp
  
### Run the make commands:

- Linux: cd llama.cpp && make

### pip install openai 'llama-cpp-python[server]' pydantic instructor streamlit

### Single Model Chat for CPU
- python -m --model models/mistral-7b-instruct-v0.1.Q4_0.gguf 
### Single Model Chat with GPU 
- python -m --model models/mistral-7b-instruct-v0.1.Q4_0.gguf --n_gpu -1
