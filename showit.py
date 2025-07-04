import os
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from opentelemetry import trace
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("test") as span:
    print("hi")
    print(span.get_span_context().trace_id)

# Add console exporter to see traces
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

# Instrument OpenAI to capture API calls
OpenAIInstrumentor().instrument()

def main():
    # Initialize LangChain with conversation memory
    llm = ChatOpenAI(
        temperature=0.7,
        model_name="gpt-3.5-turbo",
        openai_api_key=os.getenv("OPENAI_KEY")
    )
    
    # This memory buffer automatically manages conversation history
    memory = ConversationBufferMemory()
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True  # Shows what LangChain is doing
    )
    
    print("=== LangChain Conversation Demo ===")
    print("Each call looks simple but sends growing conversation history...\n")
    
    # First exchange - looks innocent
    print("1. Simple question:")
    response1 = conversation.predict(input="What's the capital of France?")
    print(f"Response: {response1}\n")
    
    # Second exchange - now sends previous context
    print("2. Follow-up question:")
    response2 = conversation.predict(input="What's its population?")
    print(f"Response: {response2}\n")
    
    # Third exchange - even more context
    print("3. Another follow-up:")
    response3 = conversation.predict(input="What's the weather like there today?")
    print(f"Response: {response3}\n")
    
    # Fourth exchange - conversation keeps growing
    print("4. One more question:")
    response4 = conversation.predict(input="What are some good restaurants there?")
    print(f"Response: {response4}\n")
    
    # Show what's actually stored in memory
    print("=== What LangChain is Actually Tracking ===")
    print("Memory buffer contents:")
    print(memory.buffer)
    
    print(f"\nTotal conversation turns: {len(memory.chat_memory.messages)}")

if __name__ == "__main__":
    with tracer.start_as_current_span("main") as span:
        print("hi main")
        print(span.get_span_context().trace_id)
        main()