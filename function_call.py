import streamlit as st
from openai import OpenAI
import json
import instructor

def app():
    # Set up the Streamlit app
    st.title("NER")
    
    
    client = OpenAI(api_key="asdf", base_url="http://localhost:8000/v1")
        
    # Create a patched client
    client = instructor.patch(client=client)
    
    ticket_custom_functions = [
    {
        'name': 'extract_passenger_info',
        'description': 'Get the passenger information from the body of the input text',
        'parameters': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person'
                },
                'orderID': {
                    'type': 'string',
                    'description': 'The order or booking ID.'
                },
                'bookedOn': {
                    'type': 'string',
                    'description': 'The date and time when the booking was made.'
                },
                'flightSupport': {
                    'type': 'integer',
                    'description': 'The customer support number for flight-related queries.'
                }
            }
        }
    }
]
    
    # Get the student description from the user
    ticket_description = st.text_area("Enter the ticket description")
    
    if ticket_description:
        if st.button('Extract'):

            response = client.chat.completions.create(
                model='stable-3b-function-calling',
                messages=[{'role': 'user', 'content': ticket_description}],
                functions= ticket_custom_functions,
                function_call='auto'
            )
            
            # Loading the response as a JSON object
            json_response = json.loads(response.choices[0].message.function_call.arguments)
            
            # Display the extracted student information
            st.write("Extracted Ticket Information:")
            st.json(json_response)

if __name__ == "__main__":
    app()
