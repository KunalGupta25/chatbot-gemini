from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime
from google import genai
from google.genai import types

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Genai initialization
client = genai.Client(api_key='AIzaSyDrSVoJnOEZclbciDf5hyor665iHG1nQsQ')
# response = model.generate_content("Explain how AI works")
# print(response.text)
PERSON_IMG = "https://img.icons8.com/bubbles/100/user.png";
BOT_IMG = "https://img.icons8.com/dusk/64/bot--v1.png";

def formatDate(date):
    return date.strftime("%H:%M")  # Adjust the format as needed

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    # Clear the session only on GET request (when the page is loaded)
    if request.method == 'GET':
        session.clear()  # This will reset the session data

    if request.method == 'POST':
        query = request.form['query']
        print("User Query:", query)  # Debugging line to check the query

        # Call the model to get a response
        try:
            response = client.models.generate_content(model='gemini-1.5-flash', contents=query)
            print("API Response:", response.text)  # Debugging line to check the response
            answer = response.text if response else "No response from the model."
        except Exception as e:
            print("Error calling the model:", e)
            answer = "There was an error processing your request."

        # Initialize messages in session if not already done
        if 'messages' not in session:
            session['messages'] = []  

        # Append user message and bot response to messages list in session
        session['messages'].append({'side': 'right', 'img': PERSON_IMG, 'name': 'You', 'time': formatDate(datetime.now()), 'text': query})
        session['messages'].append({'side': 'left', 'img': BOT_IMG, 'name': 'Chatbot', 'time': formatDate(datetime.now()), 'text': answer})

        # Save the session
        session.modified = True

    return render_template('index.html', messages=session.get('messages', []))

@app.route('/about')
def about():
    return render_template('about.html')  # Create an about.html template

if __name__ == "__main__":
    app.run(debug=True)