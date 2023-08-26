import os
import openai


class Chat:
    def __init__(self, ingredients, dietary, allergies):
        openai.api_key = "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"
        self.ingredients = ingredients
        self.dietary = dietary
        self.allergies = allergies 

    def ask_gpt(self, prompt):
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
        answer = response["choices"][0]["message"]["content"]
        with open("test.md", 'w') as f:
            f.write(answer)
        print(answer)
        return answer



    ########################## test #############################

    # test_ingredient = ["milk", "bread", "fried egg", "steak"]
    # test_dietry = ["vegan", "lactose-free"]
    # test_allergies = ["wheat", "nut"]

    ######################## end test ###########################


    def prompt_creation(self):
        # food_list = test_ingredient
        # food_list_string = ', '.join(food_list)

        dietry_list = self.dietary
        dietry_list_string = '. '.join(dietry_list)

        allergies_list = self.allergies
        allergies_list_string = '. '.join(allergies_list)

        # prompt_string = "Give me a recipe with this list of food: " + self.ingredients + ". "
        # prompt_dietry = "Here is the dietry requirements: " + dietry_list_string + ". "
        # prompt_allergies = "Here is the allergies list: " + allergies_list_string + ". "
        # prompt_format = "Give the answer in markdown format and using the metric system."
        # prompt_full = prompt_string + prompt_dietry + prompt_dietry + prompt_allergies + prompt_format

        prompt_string = "I have some leftovers. Give me a recipe with this list of ingridient: " + self.ingredients + ". "
        prompt_dietry = "Here is the dietry requirements: " + dietry_list_string + ". "
        prompt_allergies = "Here is the allergies list: " + allergies_list_string + ". "
        prompt_format = "Give the answer in markdown format using the metric system. "
        prompt_sanitizing = "If there are any food you don't recognize or does not match the dietary or allergies requirements, ignore them and display them at the very start. "
        prompt_extra = "If there is not enough ingredient to create recipes, then show recipes with some extra ingredients and highlight them."
        prompt_full = prompt_string + prompt_dietry + prompt_dietry + prompt_allergies + prompt_format + prompt_sanitizing + prompt_extra

        return prompt_full



    ########################## test #############################

    
        
    ######################## end test ###########################rn chatbot_response