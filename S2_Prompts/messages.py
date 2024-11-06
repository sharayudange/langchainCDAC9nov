# import os
# import configparser
# from langchain_cohere import ChatCohere
# from langchain_core.messages import HumanMessage, SystemMessage

# # set up config parser
# config = configparser.ConfigParser()
# config.read("config.ini")  # holds secrets and keys

# # load the Default section.
# default = config["DEFAULT"]

# # set the environment variables needed by LangSmith
# os.environ["LANGCHAIN_TRACING_V2"] = default.get("LANGCHAIN_TRACING_V2")
# os.environ["LANGCHAIN_API_KEY"] = default.get("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_ENDPOINT"] = default.get("LANGCHAIN_ENDPOINT")
# os.environ["LANGCHAIN_PROJECT"] = default.get("LANGCHAIN_PROJECT")

# # load Cohere config
# cohereConfig = config["cohere"]

# os.environ["COHERE_API_KEY"] = cohereConfig.get("COHERE_API_KEY")

# # select the model.
# model = ChatCohere(model="command-r-plus")


# # ~! Message classes
# messageForModel = [
#     SystemMessage(content="You are a chat bot who is an expert in political science"),
#     HumanMessage(content="What is the capital of India"),
# ]

# sysMessage = SystemMessage("You are a chat bot who is an expert in political science")
# humanMessage = HumanMessage(content="What is the capital of India")

# # Models such as Cohere, OpenAI extend BaseChatModel from LangChainCore
# # They are runnable and hence have an invoke method.
# # The invoke takes in a List and returns object of BaseMessage

# # ~# Both of the following product the same results.
# response = model.invoke(messageForModel)
# response = model.invoke([sysMessage, humanMessage])

# print(response.__repr__())


from langchain_core.prompts.chat import ChatMessagePromptTemplate

# This is the typical factory method
# Best is to check source code: https://github.com/langchain-ai/langchain/blob/master/libs/core/langchain_core/prompts/chat.py#L299
chatMessagePrompt = ChatMessagePromptTemplate.from_template(
    template= "Please give me flight options for {from_city} to {to_city}"
)

# In the above role is required. Why?
# ChatMessagePromptTemplate <- BaseStringMessagePromptTemplate: https://github.com/langchain-ai/langchain/blob/master/libs/core/langchain_core/prompts/chat.py#L300
# BaseStringMessagePromptTemplate has the class method from_template: https://github.com/langchain-ai/langchain/blob/master/libs/core/langchain_core/prompts/chat.py#L285
# It passes 
# It has an optional parameter cls: type[MessagePromptTemplateT] That is used to create prompt on line 327
# MessagePromptTemplateT is bound to class BaseStringMessagePromptTemplate: https://github.com/langchain-ai/langchain/blob/master/libs/core/langchain_core/prompts/chat.py#L279
# 

# print(f"The type of Prompt Message Template is \n\t{type(chatMessagePrompt)}")

# Use the prompt message template to generate the message by providing values for all the replacement variables.
# baseMessage = chatMessagePrompt.format(from_city="New Delhi", to_city="Mumbai", role="travel agent")

# print(
#     f"The type of message is: \n\t{type(baseMessage)}, \n\tand its __repr__ value is:  {baseMessage.__repr__()}"
# )  