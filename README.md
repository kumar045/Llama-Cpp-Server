# Llama-Cpp-Server

- Git clone https://github.com/ggerganov/llama.cpp
  
### Run the make commands:

- Linux: cd llama.cpp && make

### pip install openai 'llama-cpp-python[server]' pydantic instructor

### Single Model Chat with CPU
- python3 -m llama_cpp.server --model models/mistral-7b-instruct-v0.1.Q4_0.gguf 
### Single Model Chat with GPU 
- python3 -m llama_cpp.server --model models/mistral-7b-instruct-v0.1.Q4_0.gguf  --n_gpu -1

### Run multiple models at the same time using the config.json
- python3 -m llama_cpp.server --config_file config.json
```
response = client.chat.completions.create(
        model="llama.cpp/models/mistral-7b-instruct-v0.1.Q4_0.gguf",
        messages=st.session_state.messages,
        stream=True,
    )
```
Replace this with model_alias
```
response = client.chat.completions.create(
        model="mistral",
        messages=st.session_state.messages,
        stream=True,
    )
```
