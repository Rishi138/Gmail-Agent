# Gmail API integration with langchain
from langchain_community.agent_toolkits import GmailToolkit

# Loading in tools
toolkit = GmailToolkit()
tools = toolkit.get_tools()
