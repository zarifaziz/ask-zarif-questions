from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
tokenizer = AutoTokenizer.from_pretrained('mrm8488/bert-small-finetuned-squadv2')
model = AutoModelForQuestionAnswering.from_pretrained('mrm8488/bert-small-finetuned-squadv2')
question_answerer = pipeline("question-answering", model=model, tokenizer=tokenizer)

context=r"""
Hello, my name is Zarif. I am 26 years old. I'm a software engineer and data scientist based in Sydney, 
Australia focused on building AI-enabled software solutions for a wide range of problems. Currently working at Faethm.ai.
"""

while True:
    try:
        question = input("Ask me a question: ")
        result = question_answerer(question=question, context=context)
        print(
            f"Answer: '{result['answer']}'"
        )
    except Exception as e:
        print(e)
