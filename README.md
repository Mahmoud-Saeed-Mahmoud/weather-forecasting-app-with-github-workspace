# Weather Forecasting App

## Description

This project is a weather forecasting application that provides current weather conditions and forecasts. It integrates with the OpenWeatherMap API to fetch real-time data and displays weather information in a user-friendly interface. The app also includes features like location-based weather updates and weather alerts.

## Features

- Current weather conditions
- Weather forecasts
- Location-based weather updates
- Weather alerts

## Setup and Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd <project-directory>
   ```
3. Create a virtual environment:
   ```
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the App

1. Set the OpenWeatherMap API key as an environment variable:
   ```
   export OPENWEATHERMAP_API_KEY=<your-api-key>
   ```
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open your web browser and go to `http://127.0.0.1:5000` to access the weather app.

## Usage

- Enter a location in the input form to get the current weather conditions and forecasts for that location.
- The app will display the weather information in a user-friendly interface.

## License

This project is licensed under the MIT License.
