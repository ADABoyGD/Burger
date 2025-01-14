# C:\Users\gavin\OneDrive\Desktop\AI_agent2025clean\app.py

import os
import openai

# Read the OpenAI key from an environment variable, not hard-coded!
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_agent(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("AI Agent is running!")
    user_input = input("Ask the AI something: ")
    answer = chat_with_agent(user_input)
    print("\nAI says:", answer)
