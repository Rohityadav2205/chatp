from flask import Flask, render_template, request
import openai


def process_question(question):
    try:
        openai.api_key = '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'

        response = openai.Completion.create(
            engine='text-davinci-003',
            # prompt='What is the capital of France?',
            prompt=question,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
            top_p=None,
            frequency_penalty=0.6,
            presence_penalty=0.6

        )

        answer = response['choices'][0]['text']
        return answer,"green"
    except Exception as e:
        return "error" + str(e),"red"


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/answer', methods=['POST'])
def answer():
    question = request.form['question']
    print(question)
    # Process the question and get the answer
    answer,color = process_question(question)
    return render_template('answer.html', question=question, answer=answer,color=color)


if __name__ == '__main__':
    app.run()