# Financial Advisor Chatbot

An intelligent financial advisor chatbot built with Streamlit and Large Language Models. This application provides personalized financial guidance, answers questions about investments, savings, and helps with financial planning decisions.

## Features

- 💬 Interactive chat interface
- 💰 Financial advice and guidance
- 📊 Investment strategies discussion
- 💵 Budgeting and savings recommendations
- 🤖 Powered by LLM (supports both OpenAI and Llama)

## Prerequisites

- Python 3.8+
- Ollama (for local LLM) or OpenAI API key
- Git

## Installation

1. Clone the repository

`git clone https://github.com/prashantmane92/financial-advisor-chatbot.git`

`cd financial-advisor-bot`

2. Create and activate virtual environment

`python -m venv venv`

Windows

`.\venv\Scripts\activate`


3. Install dependencies

`pip install -r requirements.txt`


4. Set up environment variables

Create a .env file and add your API key (if using OpenAI)

`OPENAI_API_KEY=your_api_key_here`


## Usage

1. Start the Streamlit app:

`streamlit run main.py`


2. Open your browser and navigate to `http://localhost:8501`

3. Start chatting with your financial advisor!

## Project Structure

financial-advisor-chatbot/
├── main.py # Main Streamlit application
├── utils/
│ ├── advisor.py # Financial advisor logic
│ └── tools.py # Helper functions and tools
├── requirements.txt # Project dependencies
└── README.md # Project documentation


## Configuration

- For OpenAI: Add your API key to `.env` file
- For Llama: Install Ollama and download the model locally

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by Large Language Models
- Financial advice templates and prompts

## Contact

Prashant Mane - [@prashantmane92](https://github.com/prashantmane92)

Project Link: [https://github.com/prashantmane92/financial-advisor-chatbot](https://github.com/prashantmane92/financial-advisor-chatbot)
