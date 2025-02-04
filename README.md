# Weather App - Django Framework

A simple weather application built with **Python** and **Django Framework** that allows users to fetch real-time weather information based on either a city name or their current geolocation. The app utilizes the **OpenWeatherMap API** to display data like temperature, humidity, pressure, weather conditions, and more.

## 🚀 Features
- 🌍 Fetch weather data by entering a city name.
- 📍 Automatically detect the user's current location using Geolocation API.
- 🌡️ Display temperature, humidity, pressure, weather descriptions, and icons.
- 🌗 Dark mode toggle for an enhanced UI experience.
- 🌐 Responsive design built with **Bootstrap 5**.

## 🛠️ Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **API:** OpenWeatherMap API

## 📦 Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/weather-app-django.git
   cd weather-app-django
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the app:**  
   Visit [http://127.0.0.1:8000/weather](http://127.0.0.1:8000/weather)

## 🔑 API Configuration
- Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your API key.
- Replace the placeholder `api_key` in `views.py` with your API key:
  ```python
  api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
  ```

## 📋 Project Structure
```
weather-app-django/
├── main/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── main/index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── requirements.txt
```

## 💡 Usage
- **Search by City:** Enter the city name and click **Search** to get the weather details.
- **Current Location:** Allow location access when prompted to automatically display your current weather.
- **Dark Mode:** Toggle between light and dark themes using the moon/sun button.

## ❗ Troubleshooting
- **404 Error:** Ensure you've defined the `/weather` route in `urls.py`.
- **API Errors:** Verify your OpenWeatherMap API key is valid and active.
- **Geolocation Issues:** Make sure the browser allows location access.

## 📜 License
This project is licensed under the [MIT License](LICENSE).

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## 📧 Contact
**Author:** Evans Kirimi  
**Email:** [kirimievansgitonga@gmail.com](mailto:kirimievansgitonga@gmail.com)  
**LinkedIn:** [EVANS KIRIMI](https://www.linkedin.com/in/evans-kirimi)  
**GitHub:** [krymoevanag](https://github.com/krymoevanag)

---
*Built with ❤️ using Django and OpenWeatherMap API*

