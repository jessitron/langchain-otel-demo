import os
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
    
    # This memory buffer automatically manages conversation history
    memory = ConversationBufferMemory()
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True  # Shows what LangChain is doing
    )
    
    print("=== LangChain Conversation Demo ===")
    
    # First exchange - looks innocent
    print("1. Simple question:")
    response1 = conversation.predict(input="What is your favorite programming language?")
    print(f"Response: {response1}\n")
    
    print("2. Follow-up question:")
    response2 = conversation.predict(input="What are its disadvantages?")
    print(f"Response: {response2}\n")
    
    print("3. Separate question:")
    response3 = conversation.predict(input="What is a programming language that you struggle with?")
    print(f"Response: {response3}\n")
    
    print("4. Completely unrelated:")
    response4 = conversation.predict(input="Who shot Abraham Lincoln? Give your response in JSON format.")
    print(f"Response: {response4}\n")
    
    # # Show what's actually stored in memory
    # print("=== What LangChain is Actually Tracking ===")
    # print("Memory buffer contents:")
    # print(memory.buffer)

    # print the number of tokens in the conversation
    print(f"\nTotal conversation tokens: {llm.get_num_tokens_from_messages(memory.chat_memory.messages)}")
    
    # print(f"\nTotal conversation turns: {len(memory.chat_memory.messages)}")

if __name__ == "__main__":
    with tracer.start_as_current_span("main") as span:
        print("Trace ID:", span.get_span_context().trace_id)
        main()