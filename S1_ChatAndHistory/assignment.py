import random
import os
import asyncio
import configparser
from langchain_groq import ChatGroq
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.chat_history import InMemoryChatMessageHistory

config = configparser.ConfigParser()
config.read('/workspaces/langchainCDAC9nov/config.ini') 
# load the Default section.
default = config["DEFAULT"]

groq = config['groq']
cohere = config['cohere']


os.environ['GROQ_API_KEY'] = groq.get('GROQ_API_KEY')
os.environ['COHERE_API_KEY'] = cohere.get('COHERE_API_KEY')


def actor_picker():
    actors = ["Amitabh Bacchan", "Sharukh Khan", "Priyanka Chopra", "Deepika Padukone", "Alia Bhatt","Rohit Saraf"]
    return random.choice(actors)

def location_picker():
    locations = ["Paris", "Mumbai", "Pune", "Nainital", "Kashmir"," "]
    return random.choice(locations)

def theme_picker():
    themes = ["adventure", "romance", "mystery", "horror", "sci-fi", "funny", "motivational"]
    return random.choice(themes)

def generate_story(actor, location, theme):
    prompt = f"Write a short {theme} story featuring {actor} in {location}. Keep story in 100 words and meaningful."

    # System message for both models
    system_message = SystemMessage(content="You are a creative storyteller.")
    human_message = HumanMessage(content=prompt)

    # Cohere model
    cohere_model = ChatCohere(model="command-r-plus")
    cohere_response = cohere_model.invoke([system_message, human_message])

    # Groq model
    groq_model = ChatGroq(model="llama3-8b-8192")
    groq_response = groq_model.invoke([system_message, human_message])

    return cohere_response.content, groq_response.content

# Main function to create and modify stories
async def create_and_modify_story():
    # Pick random elements
    actor = actor_picker()
    location = location_picker()
    theme = theme_picker()
    
    # Generate initial story using Cohere model
    print("Generating story with Cohere model...")
    cohere_story = generate_story(actor, location, theme)
    print("Initial Cohere Story:")
    print(cohere_story)
    
    # Generate Initial story using
    #  Groq model
    print("Generating story with Groq model...")
    groq_story = generate_story(actor, location, theme)
    print("Groq Story:")
    print(groq_story)
    
    
    store = InMemoryChatMessageHistory()
    
    
    # user feedback to modify the story
    print("Would you like to modify the story? Please provide feedback.")
    user_feedback = input("Enter feedback to change the story: ")
    
    # Store feedback and modify the story
    store.add_message(HumanMessage(content=f"User feedback: {user_feedback}"))
    
    # Modify the story based on user feedback
    modified_story = f"User Feedback: {user_feedback}\nModified Story: {cohere_story} "
    print(modified_story)

    


asyncio.run(create_and_modify_story())
