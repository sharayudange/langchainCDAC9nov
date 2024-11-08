#### Exercise 1: Query Processing and Response Generation
Objective: Use the vector store to answer questions about documents.

Instructions:

Notice the query: "What was john guided by?" and how the similarity search helps find the answer.

Question: How does similarity search determine the most relevant document to your query?

Task: Create a new query related to the stories and modify the search function to return the top 3 relevant documents. Analyze why these documents were chosen.

#### Exercise 2: Crafting System and Human Messages
Objective: Understand the usage of system and human messages in LangChain.

Instructions:

Look at the creation of SystemMessage and HumanMessage.

Question: Why is it important to separate system-level instructions from user questions?

Task: Write a new SystemMessage that instructs the bot to provide only numerical answers (if possible) to user queries. Use this to interact with the bot and test if it works.
