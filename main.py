import requests

API_KEY = "AIzaSyD5m64cIJR4FZe6ibpLVAbAVXxsN2GymIM"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def call_google_ai(prompt):
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        try:
            text = result['candidates'][0]['content']['parts'][0]['text']
            return text
        except (KeyError, IndexError):
            return "Error: Unexpected response format"
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    while True:
        prompt = input("Enter question (type 'exit' to leave ): ")
        if prompt.lower() == "exit":
            break
        print("Generating...")
        result = call_google_ai(prompt)
        print("AI:\n", result)
        print("-" * 50)