# Integrating ChatGPT with python.
# Starting with installing required package:- pip install openai
from openai import OpenAI

gpt = OpenAI(api_key
              = "YOUR_API_KEY_HERE")

r = gpt.chat.completions.create(
    model = 'gpt-4',
    messages=[
        {"role": "user",
         "content": "Top 10 tech companies"}
    ]
)

print(r.choices[0].message.content)