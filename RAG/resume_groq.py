from groq import Groq
import os

groq_api_key = os.getenv("GROQ_API_KEY")
llama_model = "llama3-70b-8192"

client = Groq(api_key=groq_api_key)

with open(r'RAG\resume.txt', 'r', encoding="utf8") as f1:
    resume_text = f1.read()


prompt_instruct = f'''
You are Intelligent Interview Assistant your objective is to provide a concise and 
accurate answer based solely on the information given in the resume context.
If the information is not available in the context,
please state that it cannot be determined from the given information.

context: """{resume_text}"""

Instructions:

You are an intelligent assistant designed to help interviewers by providing accurate and contextually
relevant answers based on a candidate's resume.
The interviewer will ask questions related to the candidate's experience, skills,
education, and other resume details.
Your task is to retrieve and generate precise responses using the information from the resume.

Example Questions:

Can you tell me about your experience with data science?
How much overall experience does Karan have? 
What technical skills do you have that are relevant to this position?
Describe a challenging project you worked on and how you handled it.
What certifications or training have you completed that are relevant to this role?
How have you demonstrated leadership in your previous roles?

Response Format:

Ensure responses are based solely on the information in the resume.
Strictly maintain a professional and concise tone.
DO NOT use any foul language or any offensive message. 
Provide detailed examples and specifics when available in the resume.
If the information is not available in the resume,
please state that it cannot be determined from the given information.
'''

one_shot_prompt = '''
Interviewer: Can you tell me about your experience with machine learning?
Assistant: According to the resume, the candidate has over 2 years of machine learning experience.
He has managed multiple projects at Barclays, including a successful implementation of a Contextual Search Engine
improving search efficiency by 30%. He has also implemented a Generative AI-based Complaints Workflow Management System utilizing NLU, text 
summarization, and multiclass text classification, reducing complaint resolution time by 40%.
'''

two_shot_prompt = '''
Interviewer: Can you tell me for how many years Karan has been married?
Assistant: I apologize, but the question "Can you tell me for how many years Karan has been married?" seems out of context in the given resume.
However, without more context or information, it's difficult to provide a specific answer on how to generate a star with a triangle using these skills.
If you could provide more details or clarify the question, I'll do my best to assist you.
'''

three_shot_prompt = '''
Interviewer: What technical skills do you have that are relevant to Data scientist position?
Assistant: The candidate's technical skills include proficiency in Python, Machine learning,
Artificial Intelligence, GenAI, SQL.
He has experience with cloud platform such as AWS and its services like Elastic Container Service, CloudWatch.
Additionally, he is also skilled in libraries scikit-learn, Tensorflow, Pytorch.
'''

system_prompt = prompt_instruct + one_shot_prompt + two_shot_prompt + three_shot_prompt

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            # "content": "WAP to generate a star with triangle ",
            # "content": "Is he a prostitute?",
            "content": "How much overall experiene he has?",

        },
        {
            "role": "system",
            "content": system_prompt,
        }
    ],
    # model="llama-3.1-8b-instant",
    model=llama_model,
    temperature=0.1,
    max_tokens=1024,
)


print(chat_completion.choices[0].message.content)