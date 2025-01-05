import openai

try:
    openai.api_key = "your-openai-api-key"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, how are you?"}
        ],
        max_tokens=50
    )

    print(response["choices"][0]["message"]["content"].strip())

except Exception as e:
    print(f"Error occurred: {e}")