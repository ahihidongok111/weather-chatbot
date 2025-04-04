# Weather Chatbot Application

## Overview
This is a weather chatbot application that provides users with real-time weather forecasts using an AI-powered assistant. The chatbot understands natural language queries and retrieves weather information based on user input. It is built using **JavaFX** for the frontend, **Python (FastAPI)** for the backend, and an **open-source model from HuggingFace** for the chatbot's core. Weather data is fetched using the **Open-Meteo API**.

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

### **Frontend Setup**
1. Navigate to the frontend folder:
   ```sh
   cd ../frontend
   ```
2. Compile and run the JavaFX application:
   ```sh
   mvn clean javafx:run
   ```

## Usage
1. Launch the JavaFX application.
2. Enter a city name or country to get the weather forecast.
3. Ask follow-up questions (e.g., "What about tomorrow?").
4. The chatbot will respond based on the latest weather data.