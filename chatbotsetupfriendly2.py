import openai

openai.api_key = ("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")
messages = [
    {"role": "user", "content": """Act as an Ai assistant"""}
]


def Chat_Ressponse(user_input):
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages

    )
    messages.append({"role": "user", "content": response.choices[0].message.content})
    return response.choices[0].message.content


