#!/bin/bash
echo "Setting up LangChain OpenTelemetry demo..."

python3 -m venv langchain-otel-demo
source langchain-otel-demo/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete! Activate with:"
echo "source langchain-otel-demo/bin/activate"