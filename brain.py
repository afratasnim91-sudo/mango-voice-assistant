from google import genai

# Make sure your key from the screenshot is in here
client = genai.Client(api_key="AIzaSyAw4nHRW6ueWGFqYZqXTzqBssXmDxL3edk")

def get_ai_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents=f"Respond in one short sentence: {prompt}"
        )
        return response.text
    except Exception as e:
        print(f"Brain Error: {e}") 
        return "Mango can't connect to his brain right now."