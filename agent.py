# Lang chain integration of OpenAI
from langchain_openai import ChatOpenAI
# To execute tasks
from langgraph.prebuilt import chat_agent_executor
# Access gmail tools
from gmail import tools
# Maintain conversation history
from langgraph.checkpoint.memory import MemorySaver
# Access AIMessage
from langchain_core.messages import HumanMessage, AIMessage
# Streamlit for UI
import streamlit as st

# Streamlit Title
st.title("Gmail Agent")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("How can I help you today?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Importing tools from gmail.py
    tools = [*tools]

    # LLM being used
    model = ChatOpenAI(model="gpt-4o-mini")

    # Creating instance of memory saver
    memory = MemorySaver()

    # Initializing agent
    agent_executor = chat_agent_executor.create_tool_calling_executor(
        model,
        tools,
        checkpointer=memory
    )

    # Define conversation thread
    config = {"configurable": {"thread_id": "gmail_agent"}}

    # Initialize conversation history with existing messages
    conversation_history = [HumanMessage(content=msg["content"]) if msg["role"] == "user" else AIMessage(content=msg["content"]) for msg in st.session_state.messages]

    # Add the user message to the conversation history
    conversation_history.append(HumanMessage(content=prompt))

    # Invoke agent to perform actions and respond
    response = agent_executor.invoke({
        "messages": conversation_history
    }, config)

    # Pull out response content from response dict
    ai_response_content = ""
    for message in response['messages']:
        if isinstance(message, AIMessage):
            ai_response_content = message.content
            conversation_history.append(message)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.write(ai_response_content)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": ai_response_content})
