# Exercise: MuseoBot - A Versatile Virtual Museum Guide

## Overview
MuseoBot is a single, multi-functional virtual museum guide that assists visitors by answering questions about famous artworks, describing historical artifacts, providing details about artifact images, and answering historical trivia. The bot intelligently identifies the type of query based on user input and routes it to the appropriate response handler.

In this project, you will implement several functions, including a main `handle_query` function, to make MuseoBot seamlessly responsive to different kinds of questions, creating an interactive, cohesive experience for virtual museum visitors.

---

## Project Steps

### Step 1: MuseoBot’s Introduction

1. **Objective**: Set up MuseoBot to introduce itself and explain its capabilities to visitors.
   
2. **Instructions**: 
   - Create a `start_tour` function where MuseoBot welcomes visitors and explains that it can provide information about artworks, historical artifacts, images, and trivia.
   - Use a system message to set MuseoBot’s role as a knowledgeable and friendly guide.

3. **Expected Output**:
   - MuseoBot should greet users with a message like: *"Welcome to the virtual museum! I’m MuseoBot, here to help you explore artworks, historical artifacts, and more. Just enter the details about an artwork, artifact, image, or trivia question, and I’ll provide insights."*

---

### Step 2: Create Individual Query Handlers

Create separate functions for each type of query MuseoBot can handle. These functions will be integrated into the main `handle_query` function in Step 3.

1. **Artwork Query Handler**:
   - **Objective**: Enable MuseoBot to answer questions about specific artworks.
   - **Instructions**: Define a function `handle_artwork_query` that takes `artwork_name` and `artist` as parameters. This function should use a prompt template to generate a response with interesting details about the artwork.

2. **Artifact Query Handler**:
   - **Objective**: Let MuseoBot describe historical artifacts.
   - **Instructions**: Create `handle_artifact_query` that takes `artifact` as a parameter. The function should use a prompt template to generate a brief description of the artifact’s significance.

3. **Image Query Handler**:
   - **Objective**: Allow MuseoBot to describe uploaded images of artifacts.
   - **Instructions**: Define `handle_image_query`, which takes `image_url` as a parameter. The function should use an image prompt template to generate a detailed description of the artifact depicted in the image.

4. **Trivia Query Handler**:
   - **Objective**: Program MuseoBot to answer historical trivia questions using example-based responses.
   - **Instructions**: Create `handle_trivia_query` that takes `trivia_question` as a parameter. This function should use a few-shot prompt template with example Q&A pairs to generate a response for common trivia questions.

Each of these handler functions should return MuseoBot’s response to be displayed to the user.

---

### Step 3: Implementing the `handle_query` Function

**Objective**: Develop a unified `handle_query` function that routes each query to the appropriate handler based on the provided inputs. This function will make MuseoBot adaptive to different types of questions without requiring users to specify the query type directly.

**Instructions**:

1. **Define Flexible Input Parameters**:
   - `handle_query` should take multiple parameters, including `artwork_name`, `artist`, `artifact`, `image_url`, `trivia_question`, and a generic `user_input`.
   - Only one or two of these parameters will typically be provided at a time, which will help MuseoBot determine the query type.

2. **Distinguish Query Types Using Input Patterns**:
   - If specific parameters are filled (e.g., `artwork_name` and `artist`), the function can directly route to the corresponding handler.
   - If `user_input` is provided instead, MuseoBot will use patterns to identify the type:
     - **Image URL**: Check if `user_input` contains a URL pattern (e.g., starts with “http”).
     - **Trivia Question**: Check if `user_input` is a question (e.g., starts with “Who,” “What,” “When,” “Where,” or ends with a question mark).
     - **Artifact or Artwork Name**: If it’s a short string without other patterns, assume it’s either an artifact or artwork name.

3. **Route to the Correct Handler**:
   - Based on the filled parameters or detected patterns, `handle_query` should call the correct handler:
     - `handle_artwork_query` for artworks.
     - `handle_artifact_query` for artifacts.
     - `handle_image_query` for image descriptions.
     - `handle_trivia_query` for trivia questions.

4. **Return the Response**:
   - Capture and return the response from the chosen handler function, making `handle_query` the single point of contact for all MuseoBot queries.

---

### Step 4: Complete the `museum_tour` Function

1. **Objective**: Build the main `museum_tour` function that integrates all of MuseoBot’s capabilities.

2. **Instructions**:
   - Start the tour with `start_tour`.
   - Use the `handle_query` function to process any type of user query during the tour.
   - Conclude the tour with a summary of what the visitor explored, referencing their interests where applicable to make the wrap-up more engaging.

3. **Expected Outcome**:
   - MuseoBot should provide a seamless experience, dynamically adapting to each type of query and remembering user preferences, making the virtual museum tour interactive and personalized.

---

### Final Deliverable

A single, cohesive MuseoBot experience that can handle multiple types of queries (artworks, artifacts, images, and trivia), remember user interests, and provide a personalized summary at the end of the tour. Each function should work together to make MuseoBot a responsive and engaging digital museum guide.
