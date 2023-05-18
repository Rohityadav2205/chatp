import openai

print(openai.__version__)

#
openai.api_key = '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'


response = openai.Completion.create(
    engine='text-davinci-003',
    # prompt='What is the capital of France?',
    prompt=input(),
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.7,
    top_p=None,
    frequency_penalty=0.6,
    presence_penalty=0.6

)

answer = response['choices'][0]['text']
print(answer)

