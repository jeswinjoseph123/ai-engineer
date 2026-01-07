from openai import OpenAI  # import openAi from installed openai

# The API key is read automatically from the OPENAI_API_KEY environment variable
client = OpenAI()  # connect to openai


# function that take 2 argument system and user prompt which is in string
def get_response_ai(system_prompt: str, user_prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0,
        max_tokens=300
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    system_prompt = (
        "You are a beginner-friendly Python tutor."

    )
    user_prompt = ("I am learning Python and struggling to understand functions."
                   "Explain how Python functions work, including parameters and return values."
                   "Provide a simple example and explain each line.")
    ai_reply = get_response_ai(system_prompt, user_prompt)

    print("AI response:")
    print("-"*40)
    print(ai_reply)
