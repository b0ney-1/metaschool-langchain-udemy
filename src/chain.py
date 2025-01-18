from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

#Todo : Create a basic chain

def main():
    qa_chain = create_basic_chain()
    
    print("Welcome to the Basic Q&A System!")
    print("Type 'quit' to exit\n")
    
    while True:
        user_question = input("\nWhat would you like to know? ")
        
        if user_question.lower() == 'quit':
            break
        
        try:
            #Todo : Run the chain
            
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please make sure your OpenAI API key is set correctly.")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set your OPENAI_API_KEY environment variable")
    else:
        main()