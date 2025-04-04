# Weather Chatbot Application

## Overview
This is a weather chatbot application that provides users with real-time weather forecasts using an AI-powered assistant. The chatbot understands natural language queries and retrieves weather information based on user input. It is built using **JavaFX** for the frontend, **Python (FastAPI)** for the backend, and an **open-source LLM from HuggingFace** for the chatbot's core. Weather data is fetched using the **Open-Meteo API**.

## Features
- Conversational AI chatbot for weather-related queries
- Real-time weather forecasts for any location
- Supports follow-up questions and maintains chat history
- JavaFX-based graphical user interface
- Python backend powered by FastAPI for efficient communication
- Weather data retrieval using Open-Meteo API

## Tech Stack
### **Frontend** (User Interface)
- JavaFX (Java-based GUI framework)
- HTTP client for API communication with the backend

### **Backend**
- Python with FastAPI (REST API server)
- LangChain for chatbot logic
- HuggingFace open-source model for natural language processing
- Open-Meteo API for weather data retrieval

## Installation & Setup
### **Prerequisites**
- Java Development Kit (JDK) 11+
- Python 3.11+
- FastAPI and required Python dependencies
- Maven or Gradle for JavaFX project management

### **Backend Setup**
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/weather-chatbot.git
   cd weather-chatbot/backend
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the FastAPI backend:
   ```sh
   python src/main/backend/app.py
   ```

## Usage
Launch the JavaFX application and enjoy!

<p align="center">
  <img src="https://github.com/user-attachments/assets/8c1559bd-ed05-458f-927c-055bac2a542a" width="500">
</p>



