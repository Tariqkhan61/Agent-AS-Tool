from agents import Agent, Runner
from connection import config

# Ab hum different agents banaen gay 
italian_agent = Agent(
    name="Italian Translator", 
    instructions="Translate any English text into Italian.",
)

french_agent = Agent(
    name="French Translator", 
    instructions="Translate any English text into French.",
)

spanish_agent = Agent(
    name="Spanish Translator", 
    instructions="Translate any English text into Spanish.",
)

# Main agent that routes to the right translator
translation_router = Agent(
    name="Translation Router",
    instructions="""
    You are a translation assistant.Route the translation requset to the corret language agent.
    Use the appropriate tool to convert English text into either Italian, French, Spanish, Urdu, or Japanese
    based on the user's request.
    """,
    tools=[
        italian_agent.as_tool(
            tool_name="Translate_to_Italian",
            tool_description="Translates the user's message to Italian.",

        ),

        french_agent.as_tool(
            tool_name="Translate_to_French",
            tool_description="Translates the user's message to French.",

        ),

        spanish_agent.as_tool(
            tool_name="Translate_to_Spanish",
            tool_description="Translates the user's message to Spanish.",

        ),
        spanish_agent.as_tool(
            tool_name="Translate_to_Spanish",
            tool_description="Translates the user's message to Spanish.",

        ),

      


        
        
    ]

)

# Example input
result = Runner.run_sync(spanish_agent, "Translate 'I love programming and I am a student' into Italian.", run_config=config)
print(result.final_output)

