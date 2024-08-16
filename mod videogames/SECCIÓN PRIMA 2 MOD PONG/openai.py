#OpenAI Key: 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
import os
import openai
from openai import OpenAI

openai.api_key = "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"

def chat_with_gpt(prompt):
	response = openai.chat.completions.create(
		model="gpt-3.5=turbo",
		messages=[{"role":"user", "content":prompt}]
	)
	
	return response.choices[0].message.content.strip()
	
if __name__ == "__main__":
	while True: 
		user_input = input("You: ")
		if user_input.lower() in ["quit", "exit", "bye"]:
			break
		
		response= chat_with_gpt(user_input)
		print("Chatbot: ", response)
