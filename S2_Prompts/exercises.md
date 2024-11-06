#### Exercise 1: Creating Basic Message Templates
Objective: Understand the purpose of MessagePromptTemplate and ChatMessagePromptTemplate.

Task: Create a message prompt template for a chatbot. Use a template string, e.g., "Find me hotels in {city}", and specify a role for the chatbot, such as "travel agent". Format the prompt with sample data.
Challenge: Write a function that accepts any city name and generates a formatted message template.

#### Exercise 2: Using Multiple Message Types
Objective: Explore different message classes like SystemMessage, HumanMessage, and AIMessage.

Task: Write a function that sets up a chat between a user and an AI bot. Include:
A SystemMessage that defines the bot's role.
A HumanMessage with a user’s question.
An AIMessage with a response.
Hint: Look at how SystemMessage and HumanMessage can set different contexts for AI responses.

#### Exercise 3: Creating a Few-Shot Prompt Template
Objective: Learn how few-shot prompts work by providing examples.

Task: Define a few examples (e.g., questions and answers on different topics). Write a function to generate a prompt with these examples as context, where the model is expected to answer a new question.
Hint: Use the FewShotPromptTemplate and ensure it formats the question and answer in a structured way.

#### Exercise 4: Implementing Custom Example Selection
Objective: Implement and use a custom example selector based on criteria.

Task: Define a list of examples and implement a function that selects examples based on a topic. Write your logic so that only examples matching the specified topic are chosen.
Challenge: Modify the function to handle multiple selection criteria, like matching based on question type and difficulty.