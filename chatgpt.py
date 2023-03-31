#%%
import openai
openai.organization = "org-GOqz10RWXV4QQqNRyYQn4PaY"
#%%
# openai.Model.list()


# %%
def load_txt(name):
    with open(name, encoding='utf-8') as f:
        a=f.read()
    return a

p = r"E:\Projects\hackdays-explore\data\input_text1.txt"
text = load_txt(p)
question = "Was waren die Investitionen?"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": text},
            {"role": "user", "content": question},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)


#%%
question = "[Uri Amtsblatt] Was sind die Bruttoinvestitionen in der Investitionsrechnung?"
response = openai.ChatCompletion.create(
    model="davinci:ft-personal-2023-03-31-14-37-19",
    # model="davinci",
    messages=[
            {"role": "user", "content": question},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)
#%%
# question = "Wie hoch sind die Nettoinvestitionen?"
question = "Was ist ein Hund?"
import openai
res = openai.Completion.create(
    model="davinci:ft-personal-2023-03-31-14-37-19",
    # model="davinci",
    prompt=question)

#%%
print(question)
print(res)
print(res["choices"][0]["text"])
# %%
