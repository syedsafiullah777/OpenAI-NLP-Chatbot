
# Chatbot using NLP

## Overview
This project implements a chatbot using Natural Language Processing (NLP) techniques. The chatbot is designed to understand user intents and provide appropriate responses based on predefined patterns and responses. It utilizes the `nltk` library for natural language processing, `scikit-learn` for machine learning, and `streamlit` for creating an interactive web interface.

---

## Features
- Understands various user intents such as greetings, farewells, gratitude, and more.
- Provides relevant responses based on user input.
- Maintains a conversation history that can be viewed by the user.
- Built using Python and leverages popular libraries for NLP and machine learning.

---

## Technologies Used
- **Python**
- **NLTK** (Natural Language Toolkit)
- **Scikit-learn** (Machine Learning)
- **Streamlit** (Web Interface)
- **JSON** (for intents data)

---

## Installation

### 1. Clone the Repository
Clone the repository to your local machine using the following command:
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment (Optional but Recommended)
It's recommended to create a virtual environment for managing dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Required Packages
Install all necessary packages using the following command:
```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data
Ensure you have the required NLTK data for text processing by running:
```python
import nltk
nltk.download('punkt')
```

---

## Usage

To run the chatbot application, execute the following command:
```bash
streamlit run app.py
```

Once the application is running, you can interact with the chatbot through the web interface. Type your message in the input box and press Enter to see the chatbot's response.

---

## Intents Data

The chatbot's behavior is defined by the `intents.json` file, which contains various tags, patterns, and responses. You can modify this file to add new intents or change existing ones.

---

## Conversation History

The chatbot saves the conversation history in a CSV file (`chat_log.csv`). You can view past interactions by selecting the "Conversation History" option in the sidebar.

---

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- **NLTK** for natural language processing.
- **Scikit-learn** for machine learning algorithms.
- **Streamlit** for building the web interface.
- **OpenAI** for integrating dynamic query handling through GPT.

**Project by:** SYED SAFI ULLAH
