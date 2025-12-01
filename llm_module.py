import google.generativeai as genai
import os

# 1. Setup API Key
# PASTE YOUR KEY INSIDE THE QUOTES BELOW
API_KEY = "AIzaSyBDl96wjh34dgaEZRlKHaSoYBGt8tCaPIM"

genai.configure(api_key=API_KEY)

# 2. Function to Summarize & Draft Response
def process_ticket_with_llm(ticket_text):
    """
    Sends the ticket text to Gemini and returns a summary + draft response.
    """
    try:
        # We use 'gemini-pro' (good for text) or 'gemini-1.5-flash' (faster)
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Prompt Engineering: We tell the AI exactly how to behave
        prompt = f"""
        You are a helpful customer support assistant.
        Analyze the following customer ticket:
        
        Ticket: "{ticket_text}"
        
        Please provide the output in this EXACT format:
        
        SUMMARY:
        (Write a 1-sentence summary of the problem)
        
        SUGGESTED RESPONSE:
        (Write a polite, professional response to the customer addressing their issue)
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"Error connecting to AI: {str(e)}"

# --- Quick Test ---
if __name__ == "__main__":
    # Fake ticket to test the connection
    test_ticket = "My internet is not working and I am very angry! I pay too much for this."
    
    print("⏳ Asking Gemini (this might take a few seconds)...")
    result = process_ticket_with_llm(test_ticket)
    
    print("\n🤖 AI Response:\n")
    print(result)
