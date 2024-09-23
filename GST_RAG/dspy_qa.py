import dspy
from retriever import load_faiss_indices

turbo = dspy.HFModel(model='google/flan-t5-small')
dspy.configure(lm=turbo)

class BasicQA(dspy.Signature):
    ''' Answer questions with short factoid answers. '''

    question = dspy.InputField()
    context = dspy.InputField()
    answer = dspy.OutputField()

predictor = dspy.ChainOfThought(BasicQA)

query = "Whether software is regarded as goods or services in GST?"
context = load_faiss_indices(query)
pred = predictor(question=query, context=context)

print(f"Predicted Answer: {pred.answer}")
