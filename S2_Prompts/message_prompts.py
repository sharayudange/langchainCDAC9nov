from langchain_core.prompts.chat import (
    ChatMessagePromptTemplate,
)

# template parameter is required by the base class BasseStringMessagePromptTemplate as a string for creating the prompt
# role is required by ChatMessagePromptTemplate
chatMessagePrompt = ChatMessagePromptTemplate.from_template(
    template="Please give me flight options for {from_city} to {to_city}",
    role="travel agent",
)

print(f"The type of Prompt Message Template is \n\t{type(chatMessagePrompt)}")

# Use the prompt message template to generate the message by providing values for all the replacement variables.
baseMessage = chatMessagePrompt.format(from_city="New Delhi", to_city="Mumbai")

print(
    f"The type of message is: \n\t{type(baseMessage)}, \n\tand its __repr__ value is:  {baseMessage.__repr__()}"
)
