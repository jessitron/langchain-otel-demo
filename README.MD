#

## once

`./setup.sh`

## once a day

```
source langchain-otel-demo/bin/activate
export OPENAI_KEY=...
export OTEL_SERVICE_NAME=langchain-otel-demo
```

## every time

Run the demo:

`opentelemetry-instrument python showit.py`
