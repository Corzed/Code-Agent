from orchestrai import Agent, AgentManager
from coding_tools import FILE_TOOLS

# Initialize the agent manager
manager = AgentManager()

# Create the coding agent
coding_agent = Agent(
    name="CodingAssistant",
    role="""You are a coding assistant that can help with file operations and code management.
You can read, write, edit, create, rename, and delete files, as well as execute terminal commands.
Always confirm before making destructive changes (delete, overwrite).
When editing files, provide clear explanations of the changes being made.""",
    description="An AI agent specialized in code and file manipulation",
    manager=manager,
    verbose=True,
    tools=FILE_TOOLS,
    model="gpt-4",  # Make sure to use a capable model
)