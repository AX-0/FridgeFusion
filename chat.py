import openai

openai.api_key = "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"

def chat_with_chatgpt(prompt, model = "gpt-3.5-turbo"):
    response = openai.Completion.create(
        engine = model, 
        prompt = prompt, 
        max_tokens = 100, 
        n = 1, 
        steop = None, 
        temperature = 0.5
    )

    message = response.choices[0].text.strip()
    return message

def recipe_generate(user_prompt):
    chatbot_response = chat_with_chatgpt(user_prompt)
    return chatbot_response