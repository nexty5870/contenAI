import openai
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
df = pd.read_csv("kub.csv")

# Set OpenAI API key
openai.api_key = os.getenv("API_KEY")

results = []

for index, row in df.iterrows():

    prompt = f"Please write a detailed article about {row['topic']}. Use this information to write the article: {row['context']}, I want the article to look modern and stylish"
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, temperature=0.7,max_tokens=2048,top_p=0.5)
    results.append([row['topic'], response.choices[0].text])
print('Content Generation using AI completed')

output_df = pd.DataFrame(results, columns = ['Topic', 'Generated Text'])

output_df.to_csv('output.csv', index=False)


# Adding readability on the excel sheet if needed with the below block
# output_df = pd.DataFrame(results, columns = ['Topic', 'Generated Text'])
# print(output_df)

# with open('output.csv', 'w') as f:
#     output_df.to_csv(f, index=False)