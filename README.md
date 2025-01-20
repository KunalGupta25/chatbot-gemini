# Chatbot Application

## Description
This is a chatbot application that utilizes the Google Generative AI model to respond to user queries. The application provides an interactive interface for users to engage with the chatbot and receive intelligent responses.

## Features
- Chatbot interface for user interaction.
- Session management to keep track of user messages and bot responses.
- An "About" page providing information about the application.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables in a `.env` file:
   ```
   API_KEY=your_google_api_key
   ```

## Usage
To run the application, execute the following command:
```bash
python app.py
```
Then, open your web browser and navigate to `http://127.0.0.1:5000` to interact with the chatbot.

## Dependencies
- Flask
- python-dotenv
- google-generativeai

## License
This project is licensed under the MIT License. See the LICENSE file for details.
