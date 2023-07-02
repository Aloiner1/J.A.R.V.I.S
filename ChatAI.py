import openai

openai.api_key = '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'

models = openai.Model.list()
#print(models)

def handle_input(user_input):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role':'user',
                   'content':user_input}]

    )
    return completion

