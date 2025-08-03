import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_

model = genai.GenerativeModel("gemini-pro")

user_prompt = input("Nhập nội dung bạn muốn hỏi AI: ")

response = model.generate_content(user_prompt)

print("\nPhản hồi từ AI:")
print(response.text)

# request ur API using goog api for dev to get personal API key