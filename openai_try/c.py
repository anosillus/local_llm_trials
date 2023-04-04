import openai
import os
from datetime import datetime

start_time = datetime.now()

openai.api_key = os.getenv("OPENAI_API_KEY")
# model_name = "gpt-4"
model_name = "gpt-4"

question = """
以下の文章を日本語に翻訳して

ただし以下の特徴を反映した翻訳にしてください。
The style of The Great Gatsby is wry, sophisticated, and elegiac, employing extended metaphors, figurative imagery, and poetic language to create a sense of nostalgia and loss. The book can be read as an extended elegy, or poetic lament, for Gatsby – “the man who gives his name to this book… who represented everything for which I have an unaffected scorn.” Throughout the novel Nick references the fact that he is creating a written account of a time past – one he remembers with nostalgia and fondness. One of the most frequently occurring words in the book is ‘time,’ and the word ‘past’ appears often, as well, suggesting the act of remembrance and recollection. Fitzgerald describes Gatsby as an exceptionally graceful, stylish, and elegant character, and the novel’s flowing, musical sentences underscore this impression. When talking about other characters, however, the elevated, metaphoric language often creates ironic contrast with the crude nature of the characters themselves. Many of his descriptions contain an undertone of ridicule, with the most sympathetic, wistful passages reserved for the character of Gatsby and for Nick’s lost innocence.

ここからが翻訳する内容です
In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.

"Whenever you feel like criticizing any one," he told me, "just remember that all the people in this world haven't had the advantages that you've had."

He didn't say any more but we've always been unusually communicative in a reserved way, and I understood that he meant a great deal more than that. In consequence I'm inclined to reserve all judgments, a habit that has opened up many curious natures to me and also made me the victim of not a few veteran bores. The abnormal mind is quick to detect and attach itself to this quality when it appears in a normal person, and so it came about that in college I was unjustly accused of being a politician, because I was privy to the secret griefs of wild, unknown men. Most of the confidences were unsought—frequently I have feigned sleep, preoccupation, or a hostile levity when I realized by some unmistakable sign that an intimate revelation was quivering on the horizon—for the intimate revelations of young men or at least the terms in which they express them are usually plagiaristic and marred by obvious suppressions. Reserving judgments is a matter of infinite hope. I am still a little afraid of missing something if I forget that, as my father snobbishly suggested, and I snobbishly repeat, a sense of the fundamental decencies is parcelled out unequally at birth."""

response = openai.ChatCompletion.create(
    model=model_name,
    messages=[
        {"role": "user", "content": question},
    ],
)

end_time = datetime.now()

print(response.choices[0]["message"]["content"].strip())
print(f"elapsed time: {end_time - start_time}")

# write to output-${yyyymmddthhmmss}.txt
with open(f"output-{model_name}-{datetime.now().strftime('%Y%m%dT%H%M%S')}-{question}.txt", "w") as f:
    f.write(f"model: {model_name}\n")
    f.write("time: " + str(end_time - start_time) + "\n")
    f.write("question: " + question + "\n")
    f.write("answer: " + response.choices[0]["message"]["content"].strip() + "\n")
