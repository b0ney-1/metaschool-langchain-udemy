from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_basic_chain():
    # Initialize the language model
    llm = OpenAI(temperature=0.7)
    
    # Create a prompt template
    template = """
    Question: {question}

    Please provide a clear and concise answer. If you're not sure about something,
    feel free to say so. End your response with a relevant follow-up question.

    Answer:"""
    
    prompt = PromptTemplate(
        input_variables=["question"],
        template=template
    ) 
    # Create the chain using the new LCEL syntax
    chain = prompt | llm
    return chain

def main():
    # Initialize the chain
    qa_chain = create_basic_chain()
    
    print("Welcome to the Basic Q&A System!")
    print("Type 'quit' to exit\n")
    
    while True:
        user_question = input("\nWhat would you like to know? ")
        
        if user_question.lower() == 'quit':
            break
        
        try:
            # Use invoke instead of run
            response = qa_chain.invoke({"question": user_question})
            print("\nResponse:", response)
            
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please make sure your OpenAI API key is set correctly.")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set your OPENAI_API_KEY environment variable")
    else:
        main()