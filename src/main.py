from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
# tokenizer = AutoTokenizer.from_pretrained('ktrapeznikov/albert-xlarge-v2-squad-v2')
# model = AutoModelForQuestionAnswering.from_pretrained('ktrapeznikov/albert-xlarge-v2-squad-v2')
# question_answerer = pipeline("question-answering", model=model, tokenizer=tokenizer)

question_answerer = pipeline("question-answering")

context=r"""
Hello, my name is Zarif. I am 26 years old. I'm a software engineer and data scientist based in Sydney, 
Australia focused on building AI-enabled software solutions for a wide range of problems. Currently working at Faethm.ai.
"""
result = question_answerer(question="What is Zarif's name?", context=context)

print(
    f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}"
)

while True:
    try:
        question = input("Ask me a question: ")
        result = question_answerer(question=question, context=context)
        print(
            f"Answer: '{result['answer']}'"
        )
    except Exception as e:
        print(e)
