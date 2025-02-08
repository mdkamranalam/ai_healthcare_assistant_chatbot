# AI Healthcare Assistant Chatbot

## AI Healthcare Assistant Chatbot
This project is an AI-powered healthcare assistant that provides personalized health advice, symptom monitoring, fitness tracking, and preventive care tips. It leverages a fine-tuned healthcare-specific NLP model to improve user experience and deliver accurate recommendations

## Features
List the key features of your chatbot, such as:\
✅ Symptom checker\
✅ Personalized health advice\
✅ Fitness tracking\
✅ Preventive care recommendations\
✅ User-friendly chat interface

## Installation and Setup
Provide step-by-step instructions on how to set up and run the project.

**Clone the repository**
```bash
git clone https://github.com/mdkamranalam/ai_healthcare_assistant_chatbot.git
```
**Open project directory**
```bash
cd ./ai_healthcare_assistant_chatbot
```
**Create virtual environment**
```bash
conda create -n myenv python==3.10 -y
```
**Activate virtual environment**
```bash
conda activate myenv
```
**Install all requirements**
```bash
pip install -r requirements.txt
```

If you want to deactivate environment:\
**Deactivate virtual environment**
```bash
conda deactivate
```

## How to use huggingface tokens?
There are 2 methods:

**METHOD 1: By making <mark>.toml</mark> file for streamlit**
- Step 1: Create folder name <mark>.streamlit</mark> in the project directory.
- Step 2: Then create file name <mark>secrets.toml</mark> in the <mark>.streamlit</mark> directory.
- Step 3: Now, add your Huggingface token
```toml
HUGGINGFACE_TOKEN="YOUR HUGGINGFACE TOKEN HERE"
```

or,
**METHOD 2: By using <mark>.env</mark> file**
- Step 1: Create file name <mark>.env</mark> in the project directory.
- Step 2: Then make sure you comment out code that is necessary to access <mark>.env</mark> in <mark>app.py</mark>.
- Step 3: Now, add your Huggingface token
```env
HUGGINGFACE_TOKEN="YOUR HUGGINGFACE TOKEN HERE"
```

## Usage
Explain how to use the chatbot. Provide an example command or usage instructions.\
**Run streamlit app**
```bash
streamlit run app.py
```

## Model & Dataset
Since you're integrating a Hugging Face healthcare-specific model, include:
- The model used Mistral-7B-Instruct-v0.3
- Finetune on custom template

## For Future
Implementing some new features as well as updating the project for better use case scenarios.

## Contact & Support
LinkedIn - https://www.linkedin.com/in/muhammad-kamran-alam-47b6ab230/