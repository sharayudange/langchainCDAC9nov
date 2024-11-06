import os
import configparser
import puzzles

# set up config parser
config = configparser.ConfigParser()
config.read("config.ini")

# load the Default section.
default = config["DEFAULT"]


# set the environment variables needed by LangSmith
os.environ["LANGCHAIN_TRACING_V2"] = default.get("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_API_KEY"] = default.get("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_ENDPOINT"] = default.get("LANGCHAIN_ENDPOINT")
os.environ["LANGCHAIN_PROJECT"] = default.get("LANGCHAIN_PROJECT")

# load Groq config
groqConfig = config["groq"]

os.environ["GROQ_API_KEY"] = groqConfig.get("GROQ_API_KEY")


from langchain_groq import ChatGroq

#  We use the llama3 8b model
groqmodel = ChatGroq(model="llama3-8b-8192")

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

parser = StrOutputParser()
puzzle = puzzles.puzzles("tallBuilding")  # Based on user input pick a puzzle.
system_template = (
    "solve the following puzzle. Please provide a {responseType} response."
)

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", puzzle)]
)


# prompt Template also implements runnable and can be easily chained.
chain = prompt_template | groqmodel | parser

str = chain.invoke({"responseType": "detailed"})

print(str)
