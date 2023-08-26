import os
import openai

openai.api_key = "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"

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": prompt
        },
        {
        "role": "user",
        "content": ""
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response["choices"][0]["message"]["content"]



########################## test #############################

test_ingredient = ["milk", "bread", "fried egg", "steak"]

######################## end test ###########################



food_list = test_ingredient
food_list_string = ', '.join(food_list)
prompt_string = "Give me a recipe of what I can make with a list of food: "
prompt_format = "Give the answer in markdown format"
prompt_full = prompt_string + food_list_string + ". " + prompt_format

print(prompt_full)
response_md = ask_gpt(prompt_full)

with open("test.md", 'w') as f:
    f.write(response_md)