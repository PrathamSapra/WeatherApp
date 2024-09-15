
# ☁️ Weather App ⛅

Welcome to **Weather App**—where Python meets the skies to fetch you live weather updates! 🌤️ Whether you're planning a beach day or just want to check if it's sweater weather, this app has you covered. And if things go wrong... well, you'll get an entertaining GIF! 😜

---

## 🌟 Features

- **Live Weather Updates**: Enter any city, and boom 💥, you get the current temperature, humidity, wind speed, and more!
- **Cool UI**: A slick, easy-to-use interface designed using **Tkinter**.
- **Error Handling**: If something goes wrong, don't worry, you'll get a *fancy* animated GIF to cheer you up! 🎉
- **Real-Time Clock**: Know the local time of your city along with the weather updates ⏰.

---

## 🚀 How to Run

1. **Clone the repo**:
   ```bash
   git clone https://github.com/PrathamSapra/WeatherApp.git
   cd WeatherApp
   ```

2. **Install the dependencies**:
   - You'll need a few Python packages to run the app. Just install them with:
     ```bash
     #pip install geopy
      #pip install timezonefinder
      #pip install pytz
      #pip install Pillow
      #pip install requests

     ```
   
   You’ll need the following:
   - `geopy`
   - `timezonefinder`
   - `pytz`
   - `requests`
   - `Pillow` (for GIF animation!)

3. **Run the app**:
   ```bash
   python weather_app.py
   ```

---

## 🛠️ How It Works

- **Tkinter GUI**: The app interface is built using **Tkinter**, Python’s standard GUI toolkit. You’ll see search boxes, buttons, and results all laid out in a visually clean and modern way. 🔲
  
- **Geolocation & Timezone**: The magic starts when you enter a city name. It uses `geopy` and `timezonefinder` to get the exact timezone, and then we fetch the current local time. 🕰️

- **OpenWeatherMap API**: Weather data comes from the **OpenWeatherMap** API. It gives us the latest temperature, wind speed, humidity, and pressure for your city. ☁️

- **Error Handling**: If the API call fails, or if there’s any other issue, we show a fun little animated GIF using `Pillow` to make your error experience a bit more... enjoyable. 😉

---

## 📦 Files

- **weather_app.py**: The main code file where all the fun happens! 🎯
- **search.png, logo.png, box.png**: Images used for the UI.
- **requirements.txt**: Python dependencies to install.
  
---

## 🎉 Fun Fact

- Ever seen an error message make you smile? Well, now you will! If you misspell a city or there's no internet connection, you'll be greeted by an adorable error GIF. 😂 Who knew debugging could be fun?

---

## 🤖 Tech Used

- **Python** 🐍
- **Tkinter** for the GUI 🖥️
- **Geopy** for location tracking 🌍
- **TimezoneFinder** for timezone fetching 🕓
- **OpenWeatherMap API** for real-time weather data 🌡️
- **Pillow** for GIF handling 🖼️

---

## 🧠 Ideas for Future Updates

- 🌎 Add a world map showing weather in multiple cities.
- 📱 Convert this app into a mobile-friendly version.
- 🎨 Add themes and customize the look and feel.
  
---

## ✨ Show Your Support

If you like this project, give it a ⭐ on GitHub and feel free to fork or contribute! Let’s make weather apps fun again! 🙌

---

Made with 💻 and a dash of fun by Pratham Sapra 👨‍💻
