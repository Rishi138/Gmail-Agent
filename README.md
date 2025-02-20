# Gmail-Agent

A Gmail agent integrated with LangChain and powered by OpenAI's gpt-4o-mini, offering AI-driven interactions and task execution, including drafting, sending, and summarizing emails, all within a user-friendly Streamlit interface.

Here is a sample prompt for this application to generate a very basic email draft.
![image](https://github.com/user-attachments/assets/8140ac06-233b-42ae-919b-4a90b10abacb)
In Gmail, a new draft was created with the following.
![image](https://github.com/user-attachments/assets/f299a436-f415-482c-a6dc-8d5a7940a455)


## Table of Contents
1. [Introduction](#Gmail-Agent)
2. [Features](#features)
3. [Google Developer Setup](#google-developer-setup)
4. [Installation](#installation)
5. [Sample Prompts](#sample-prompts)

## Features
  - **OpenAI Model Integration**: Discuss and look over emails with powerful LLMs from OpenAI such as gpt-4o and gpt4o-mini.
  - **Gmail API Integration**: Employs Gmail tools to ask an LLM to draft, send, and reply to emails from an application hosted locally. 
  - **Conversation History**: Maintains and displays chat history to create more in-depth and context-aware conversations.
  - **Streamlit UI**: Provides a real-time, user-friendly chat hosted on a local machine.

## Google Developer Setup
1. **Create New Project**
   - Navigate to [Google Console](https://console.cloud.google.com/) and create a new project titled Gmail Agent

3. **Enable Gmail API**
   - Select [APIs & Services](https://console.cloud.google.com/apis/dashboard?) from the Quick access menu
   - Search Gmail API in the toolbar above and select the first option
   - Press Enable

3. **Credentials**
   - Select [Credentials](https://console.cloud.google.com/apis/dashboard?) from the left hand menu
   - Configure OAuth consent screen if not done already
   - Navigate back to credential screen and create new set of credentials for desktop application
   - Download JSON file and upload to folder containing agent.py
    
4. **Permissions**
   - Navigate to [Audience](https://console.cloud.google.com/auth/audience?) screen
   - Scroll to bottom and add your email as a test user
  
## Installation
1. **Clone Repository**
```sh
git clone https://github.com/Rishi138/gmail-agent.git
cd gmail-agent
```

2. **Install Dependencies**
```sh
pip3 install -r requirements.txt
```

3. **Run Streamlit App**
```sh
python -m streamlit run agent.py 
```

## Sample Prompts
```
Summarize the email thread with the client from the past week, including key points discussed, decisions made, and any action items or follow-ups required.
```

```
Draft a professional email to my manager, summarizing the progress we've made on the recent marketing project, highlighting key milestones achieved, and outlining the next steps. Mention any challenges we faced and how we overcame them.
```

```
Set up an automated email response to acknowledge receipt of incoming support requests and provide initial troubleshooting steps. Include contact information for further assistance. Make sure to ask me for any unknown information before sending the email.
```
