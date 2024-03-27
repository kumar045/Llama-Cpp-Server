from openai import OpenAI
import json
import instructor

# Create a client
client = OpenAI(api_key="password", base_url="http://localhost:8000/v1")
# Create a patched client
client = instructor.patch(client=client)

student_custom_functions = [
    {
        'name': 'extract_student_info',
        'description': 'Get the student information from the body of the input text',
        'parameters': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person'
                },
                'major': {
                    'type': 'string',
                    'description': 'Major subject.'
                },
                'school': {
                    'type': 'string',
                    'description': 'The university name.'
                },
                'grades': {
                    'type': 'integer',
                    'description': 'GPA of the student.'
                },
                'club': {
                    'type': 'string',
                    'description': 'School club for extracurricular activities. '
                }
                
            }
        }
    }
]
student_1_description = "David Nguyen is a sophomore majoring in computer science at Stanford University. He is Asian American and has a 3.8 GPA. David is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after graduating."
student_description = [student_1_description]
for i in student_description:
    response = client.chat.completions.create(
        model = 'mistral-function-calling',
        messages = [{'role': 'user', 'content': i}],
        functions = student_custom_functions,
        function_call = 'auto'
    )

    
# Loading the response as a JSON object
json_response = json.loads(response.choices[0].message.function_call.arguments)
print(json_response)
