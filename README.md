# Gmail-Agent

A Gmail agent integrated with LangChain and powered by OpenAI's GPT-40-mini, offering AI-driven interactions and task execution, including drafting, sending, and summarizing emails, all within a user-friendly Streamlit interface.

## Features
- **LangChain Model Integration**: Utilizes the ChatOpenAI model for AI-powered interactions.
- **Gmail API Integration**: Employs the GmailToolkit to access Gmail tools and execute tasks.
- **Conversation History**: Maintains and displays chat history using MemorySaver.
- **Streamlit UI**: Provides a real-time, user-friendly chat
  
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
