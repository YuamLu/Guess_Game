# Guess Game 🎭

Guess Game is an interactive web application where an AI Language Model (LLM) plays the role of a game host. Players must guess a secret item by asking questions and receiving indirect clues from the AI.

## Features 🚀

- AI-powered game host using a Large Language Model
- Web-based user interface built with Streamlit
- Dynamic question-answer gameplay
- Random selection of topics for each game
- Class and seat number input for player identification
- Multilingual support (primarily Chinese)

## How It Works 🧠

1. **Game Initialization**: The AI selects a random topic from a predefined list.
2. **Player Interaction**: Users ask questions through a chat interface.
3. **AI Responses**: The LLM provides indirect clues based on the secret item.
4. **Guessing**: Players attempt to guess the item using the provided clues.
5. **Win Condition**: The game ends when the player correctly guesses the item.

## Technical Stack 🛠️

- Web Framework: `streamlit`
- AI Model API: Together.ai (Qwen/Qwen1.5-72B-Chat)
- HTTP Requests: `requests`
- Language: Python

## Usage 🖥️

To run the application:

```bash
streamlit run main.py
```

1. Enter your class and seat number.
2. Start asking questions to guess the secret item.
3. Use the phrase "答案是XX嗎?" (Is the answer XX?) to confirm your guess.
4. The game ends when you guess correctly or choose to start a new game.

## Core Functionality 🧠

### Main Components

- `call_ai_model`: Function to interact with the AI model API
- Session state management for conversation tracking
- Dynamic conversation display using Streamlit's chat interface
- Webhook integration for game record submission

### Game Flow

1. Initialize game with a random topic
2. Display welcome message and game instructions
3. Accept user input for questions
4. Process AI responses and update the conversation
5. Check for correct guesses and end the game accordingly

## Notes 📝

- The AI is instructed to maintain a strict and challenging gameplay experience.
- Cheating attempts or off-topic conversations are discouraged by the AI.
- The game is primarily in Chinese, with some English instructions in the code comments.