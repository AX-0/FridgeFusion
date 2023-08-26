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

test_ingredient = ["milk", "bread", "fried egg", "steak", "shoe"]
test_dietry = ["lactose-free"]
test_allergies = ["wheat", "nut"]

######################## end test ###########################



food_list = test_ingredient
food_list_string = ', '.join(food_list)

dietry_list = test_dietry
dietry_list_string = '. '.join(dietry_list)

allergies_list = test_allergies
allergies_list_string = '. '.join(allergies_list)

prompt_string = "I have some leftovers. Give me a recipe with this list of ingridient: " + food_list_string + ". "
prompt_dietry = "Here is the dietry requirements: " + dietry_list_string + ". "
prompt_allergies = "Here is the allergies list: " + allergies_list_string + ". "
prompt_format = "Give the answer in markdown format. "
prompt_sanitizing = "If there are any food you don't recognize or does not match the dietry or allergies requirements, ignore them and display them at the very start. "
prompt_extra = "If there is not enough ingredient to create recipes, then show recipes with some extra ingredients and highlight them."
prompt_full = prompt_string + prompt_dietry + prompt_dietry + prompt_allergies + prompt_format + prompt_sanitizing + prompt_extra

print(prompt_full)
response_md = ask_gpt(prompt_full)



########################## test #############################

with open("test.md", 'w') as f:
    f.write(response_md)
    
######################## end test ###########################