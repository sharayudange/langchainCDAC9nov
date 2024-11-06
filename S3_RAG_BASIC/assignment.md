# **Assignment: Build a Mini Q&A Assistant for Story Summarization**

### **Objective**
Create a Q&A assistant that helps summarize short stories by answering user queries based on the context of the story. Your goal is to implement a full workflow that involves embedding, vector storage, similarity search, and chatbot interaction, while ensuring that each component is customized to your unique design.

### **Scenario**
Imagine you are developing a tool for children's literature enthusiasts. This assistant will help summarize short stories by answering questions about them. For this assignment, you’ll work with provided short story texts, embed them, and set up a Q&A flow to make the assistant truly helpful.

---

### **Requirements**

#### 1. **Select a Story and Create Embeddings**
- Pick 2-3 short stories of your own choice (at least one story should be original—feel free to get creative).
- Use an embedding model (like AI21Embeddings) to create embeddings for each story.

  **Task:** Write your own short story of 200-300 words and use an embedding model to generate embeddings for it.
  - **Hint:** The story should have multiple elements (characters, events, places) to make question-answering more interesting.

#### 2. **Implement Vector Store for Storage**
- Store these embeddings in a vector store of your choice (e.g., InMemoryVectorStore or another like FAISS).

  **Task:** Implement a function that can store your story’s embedding and later retrieve it based on similarity.
  - **Challenge:** Compare the retrieval times between two vector stores and justify your choice.

#### 3. **User Query Integration**
- Allow the user to ask questions about the stories, like "Who was the protagonist?" or "What happened at the end?"

  **Task:** Implement a function that allows a user to ask questions and retrieves relevant story parts using similarity search.
  - **Hint:** Focus on understanding the user query and connecting it with the relevant part of the story.

#### 4. **Building the Response System**
- Set up a response generation mechanism using system and human messages. 
- Your assistant should be concise and friendly in answering questions about the stories.

  **Task:** Create a system message to guide your assistant's behavior (e.g., "Provide answers in simple language suitable for children")

#### 5. Adding Value: Story Summary

As an additional feature, let the user ask for a summary of the story.

Task: Write code that generates a summary of the story when the user asks for it.

Challenge: Include an option to summarize the story in 3 sentences, or in 2-3 bullet points.