import os
import warnings
warnings.filterwarnings("ignore")
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
RESET = "\033[0m"

def main():
    llm = ChatOpenAI(
        temperature=0.7,
        model_name="gpt-3.5-turbo",
        openai_api_key=os.getenv("OPENAI_KEY")
    )
    
    conversation = ConversationChain(llm=llm)
    
    print("=== LangChain Conversation Demo ===")
    
    print("1. Simple question:")
    input = "What is your favorite programming language?"
    print(f"{CYAN}{input}{RESET}")
    response1 = conversation.predict(input=input)
    print(f"Response: {GREEN}{response1}{RESET}\n")

    print("2. Follow-up question:")
    input = "What are its disadvantages?"
    print(f"{CYAN}{input}{RESET}")
    response2 = conversation.predict(input=input)
    print(f"Response: {GREEN}{response2}{RESET}\n")

    print("3. Separate question:")
    input = "What is a programming language that you struggle with?"
    print(f"{CYAN}{input}{RESET}")
    response3 = conversation.predict(input=input)
    print(f"Response: {GREEN}{response3}{RESET}\n")

    print("4. Completely unrelated:")
    input = "Who shot Abraham Lincoln? Give your response in JSON format."
    print(f"{CYAN}{input}{RESET}")
    response4 = conversation.predict(input=input)
    print(f"Response: {GREEN}{response4}{RESET}\n")

if __name__ == "__main__":
    with tracer.start_as_current_span("main") as span:
        print("Trace ID:", span.get_span_context().trace_id)
        main()