#pip install geopy
#pip install timezonefinder
#pip install pytz
#pip install Pillow
#pip install requests


# Import necessary libraries for GUI and other functionality
from tkinter import *  # Import all components from tkinter (GUI library)
import tkinter as tk  # Import tkinter with an alias 'tk'
from geopy.geocoders import Nominatim  # Import geocoder to convert city name into coordinates
from tkinter import ttk, Toplevel  # ttk for styling, Toplevel for creating pop-up windows
from timezonefinder import TimezoneFinder  # Import timezone finder to get timezone by coordinates
from datetime import datetime  # For handling date and time
import requests  # To make HTTP requests to the weather API
import pytz  # To handle time zone conversion
from PIL import Image, ImageTk, ImageSequence  # For handling images and GIF animations
from io import BytesIO  # To handle byte data from the internet

# Create the main window of the app
root = Tk()
root.title("Weather App")  # Set title of the window
root.geometry("900x500+300+200")  # Set window size and initial position
root.resizable(False, False)  # Disable resizing the window


# Function to display animated GIF in case of an error
def show_gif_error():
    # Create a new pop-up window for showing the error
    error_window = Toplevel()
    error_window.title("Weather App Error")  # Set title of error window
    error_window.geometry("700x700")  # Set size of error window

    # Load the GIF from URL
    url = "https://media1.tenor.com/m/BNrHF8JgiU8AAAAd/homelander-haha-no.gif"
    response = requests.get(url)  # Send a request to get the GIF from the URL
    img_data = response.content  # Get image data (GIF in bytes)

    # Use BytesIO to create a file-like object and open it using PIL
    gif = Image.open(BytesIO(img_data))

    # Function to animate the GIF frame by frame
    def animate_gif(frame_idx):
        # Try to loop through the sequence of frames in the GIF
        try:
            gif.seek(frame_idx)  # Go to the next frame
            gif_frame = ImageTk.PhotoImage(gif)  # Convert frame to a format tkinter can use
            gif_label.config(image=gif_frame)  # Update the label with the new frame
            gif_label.image = gif_frame  # Keep a reference to avoid garbage collection
            # Schedule next frame update (delay between frames)
            error_window.after(100, animate_gif, frame_idx + 1)  # Adjust delay if necessary
        except EOFError:
            # If the end of the sequence is reached, loop back to the first frame
            error_window.after(100, animate_gif, 0)

    # Create a label to display the GIF
    gif_label = Label(error_window)
    gif_label.pack(pady=10)

    # Start the animation with the first frame
    animate_gif(0)

    # Add error message text below the GIF
    error_label = Label(error_window, text="There was an error fetching the weather data.", font=("Arial", 14))
    error_label.pack(pady=10)


# Function to fetch weather details based on the city entered by the user
def getWeather():
    try:
        city = textfield.get()  # Get the text (city name) entered by the user in the input field

        geolocator = Nominatim(
            user_agent="geopiExercises")  # Create a geolocator object for converting city names into coordinates
        location = geolocator.geocode(city)  # Get location details (coordinates) of the city
        obj = TimezoneFinder()  # Create a TimezoneFinder object to find the timezone by coordinates
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)  # Get the timezone of the city

        home = pytz.timezone(result)  # Convert the timezone string into a pytz timezone object
        local_time = datetime.now(home)  # Get the current time in the selected timezone
        current_time = local_time.strftime("%I:%M %p")  # Format the time into a 12-hour format
        clock.config(text=current_time)  # Update the clock label with the current time
        name.config(text="CURRENT WEATHER")  # Update the label to show that it's displaying current weather

        # Define the API URL with the city name and your API key
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=7225d8238e0c6e09a7caeebc73599c23"
        json_data = requests.get(api).json()  # Make a request to the weather API and get the response in JSON format

        # Parse the JSON data to extract useful information
        condition = json_data['weather'][0]['main']  # Get the main weather condition (e.g., Clear, Rain)
        description = json_data['weather'][0]['description']  # Get the detailed weather description
        temp = int(json_data['main']['temp'] - 273.25)  # Convert temperature from Kelvin to Celsius
        pressure = json_data['main']['pressure']  # Get the atmospheric pressure
        humidity = json_data['main']['humidity']  # Get the humidity percentage
        wind = json_data['wind']['speed']  # Get the wind speed

        # Update the UI labels with the fetched weather data
        t.config(text=(temp, "°"))  # Update temperature label
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))  # Update condition and temperature label

        w.config(text=wind)  # Update wind speed label
        h.config(text=humidity)  # Update humidity label
        d.config(text=description)  # Update description label
        p.config(text=pressure)  # Update pressure label

    except Exception as e:
        show_gif_error()  # If there's an error (e.g., invalid city), show the GIF error window


# Create and place the search box (input field) for entering city names
Search_image = PhotoImage(file="search.png")  # Load an image for the search box background
myimage = Label(image=Search_image)  # Create a label with the search box image
myimage.place(x=20, y=20)  # Place the search box on the window

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"))  # Create the text entry field
textfield.place(x=50, y=40)  # Place the text field at the desired location
textfield.focus()  # Set focus on the text field so the user can start typing

# Create and place the search button with an icon
Search_icon = PhotoImage(file="search_icon.png")  # Load an image for the search button
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040",
                      command=getWeather)  # Create the button and link it to the getWeather function
myimage_icon.place(x=400, y=34)  # Place the button on the window

# Create and place the logo
Logo_image = PhotoImage(file="logo.png")  # Load an image for the app logo
logo = Label(image=Logo_image)  # Create a label with the logo
logo.place(x=150, y=100)  # Place the logo at the desired location

# Create and place the bottom box (for displaying weather info)
Frame_image = PhotoImage(file="box.png")  # Load an image for the bottom box background
frame_myimage = Label(image=Frame_image)  # Create a label with the bottom box image
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)  # Pack the box at the bottom of the window

# Create and place labels for the current time and weather conditions
name = Label(root, font=("arial", 15, "bold"))  # Label for displaying the text 'CURRENT WEATHER'
name.place(x=30, y=100)  # Place the label

clock = Label(root, font=("Helvatica", 20))  # Label for displaying the current time
clock.place(x=20, y=130)  # Place the label

# Create and place labels for weather details (wind, humidity, etc.)
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")  # Wind label
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")  # Humidity label
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")  # Description label
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")  # Pressure label
label4.place(x=650, y=400)  # Place the pressure label on the window

# Create and place labels that will be updated with the weather data (these start with '...')
t = Label(font=("arial", 70, "bold"), fg="#ee666d")  # Label for temperature
t.place(x=400, y=150)  # Place the temperature label

c = Label(font=("arial", 15, 'bold'))  # Label for weather condition and "feels like" temperature
c.place(x=400, y=250)  # Place the condition label

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")  # Label for wind speed
w.place(x=120, y=430)  # Place the wind speed label

h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")  # Label for humidity
h.place(x=250, y=430)  # Place the humidity label

d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")  # Label for weather description
d.place(x=450, y=430)  # Place the description label

p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")  # Label for pressure
p.place(x=670, y=430)  # Place the pressure label

# Start the main loop of the tkinter application
root.mainloop()
