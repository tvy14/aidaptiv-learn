## Start the Backend Server
docker run --runtime nvidia --rm --gpus='"device=0"' \
--mount type=bind,source=/usr/local/models/,target=/usr/local/models/ \
-p 21554:8000 --ipc=host vllm/vllm-openai:v0.6.3.post1 \
--model /usr/local/models/Meta-Llama-3.1-8B-Instruct-AWQ-INT4/ --max-model-len 8192
