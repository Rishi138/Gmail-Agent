# Gmail-Agent

A Gmail agent integrated with LangChain and powered by OpenAI's gpt-4o-mini, offering AI-driven interactions and task execution, including drafting, sending, and summarizing emails, all within a user-friendly Streamlit interface.

## Features
  - **LangChain Model Integration**: Utilizes the ChatOpenAI model for AI-powered interactions.
  - **Gmail API Integration**: Employs the GmailToolkit to access Gmail tools and execute tasks.
  - **Conversation History**: Maintains and displays chat history using MemorySaver.
  - **Streamlit UI**: Provides a real-time, user-friendly chat

## Google Developer Setup
1. **Create New Project**
  - Navigate to [Google Console](https://console.cloud.google.com/) and create a new project tiled Gmail Agent

2. **Enable Gmail API**
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
