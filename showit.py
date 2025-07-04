import os
import warnings
warnings.filterwarnings("ignore")
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def main():
    llm = ChatOpenAI(
        temperature=0.7,
        model_name="gpt-3.5-turbo",
        openai_api_key=os.getenv("OPENAI_KEY")
    )
    
    conversation = ConversationChain(
        llm=llm
    )
    
    print("=== LangChain Conversation Demo ===")
    
    print("1. Simple question:")
    input = "What is your favorite programming language?"
    print(input)
    response1 = conversation.predict(input=input)
    print(f"Response: {response1}\n")
    
    print("2. Follow-up question:") 
    input = "What are its disadvantages?"
    print(input)
    response2 = conversation.predict(input=input)
    print(f"Response: {response2}\n")
    
    print("3. Separate question:")
    input = "What is a programming language that you struggle with?"
    print(input)
    response3 = conversation.predict(input=input)
    print(f"Response: {response3}\n")
    
    print("4. Completely unrelated:")
    input = "Who shot Abraham Lincoln? Give your response in JSON format."
    print(input)
    response4 = conversation.predict(input=input)
    print(f"Response: {response4}\n")

if __name__ == "__main__":
    with tracer.start_as_current_span("main") as span:
        print("Trace ID:", span.get_span_context().trace_id)
        main()