import streamlit as st
from swarmauri.standard.llms.concrete.GroqModel import GroqModel
from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent
from swarmauri.standard.conversations.concrete.Conversation import Conversation

# Replace with your actual API key
API_KEY = "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"

# Initialize the GroqModel
llm = GroqModel(api_key=API_KEY)

# Create a SimpleConversationAgent with the GroqModel
conversation = Conversation()
agent = SimpleConversationAgent(llm=llm, conversation=conversation)

# Function to generate job application and skills
def generate_application_and_skills(job_role, company_name):
    try:
        # Create prompts for job application and must-have skills
        application_prompt = (
            f"Write a comprehensive, complete, and persuasive job application letter for the position of {job_role} at {company_name}. "
            "The letter should include the following sections: introduction, relevant experience, qualifications, and a concluding statement on why the applicant is an excellent fit for the role. "
            "Ensure the letter is well-structured and professionally written. End the letter with a proper closing, such as 'Thank you for considering my application. Regards,' followed by the applicant's name."
        )
        
        skills_prompt = (
            f"Provide a detailed list of essential skills for a {job_role} at {company_name}. "
            "Include descriptions of each skill and suggest courses or resources where one can learn these skills."
        )
        
        # Get responses from the model
        application_response = agent.exec(application_prompt)
        skills_response = agent.exec(skills_prompt)
        
        # Check if responses are empty and handle accordingly
        if not application_response:
            application_response = "No response generated for the application letter."
        
        if not skills_response:
            skills_response = "No response generated for the skills list."
        
        return application_response, skills_response

    except Exception as e:
        return f"An error occurred: {e}", "An error occurred while generating skills."

# Streamlit application layout
st.title("Job Application Assistant")

job_role = st.text_input("Job Role", placeholder="Enter the job role (e.g., Software Engineer)")
company_name = st.text_input("Company Name", placeholder="Enter the company name")

if st.button("Generate"):
    if job_role and company_name:
        application_response, skills_response = generate_application_and_skills(job_role, company_name)
        st.subheader("Job Application Letter")
        st.text_area("Application Letter", value=application_response, height=300)
        
        st.subheader("Must-Have Skills and Courses")
        st.text_area("Skills List", value=skills_response, height=300)
    else:
        st.error("Please enter both job role and company name.")
