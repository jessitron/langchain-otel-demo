# Python LangChain OpenTelemetry Demo

Super simple python program that makes some calls to OpenAI, and sends telemetry with OpenTelemetry.

## Installation

Do this once, to set up venv:

`./setup.sh`

## daily

```
source langchain-otel-demo/bin/activate
export OPENAI_KEY=...
export OTEL_SERVICE_NAME=langchain-otel-demo
```

... then if you aren't running a local collector (you probably aren't), set these env vars to send directly to Honeycomb:

(set your-api-key to a [Honeycomb](https://www.honeycomb.io/) ingest key. A free account is great.)

```
export OTEL_TRACES_EXPORTER="otlp"
export OTEL_LOGS_EXPORTER="otlp"
export OTEL_METRICS_EXPORTER="none"
export OTEL_EXPORTER_OTLP_PROTOCOL="http/protobuf"
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.honeycomb.io:443" # US instance
export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=<your-api-key>"
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
```

source of how to get otel working: [https://docs.honeycomb.io/send-data/python/opentelemetry-sdk/]()

## every time

Run the demo:

`opentelemetry-instrument python showit.py`
