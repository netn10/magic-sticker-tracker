from flask import Flask, render_template, url_for, request, redirect
import os
from random import sample
from flask_cors import CORS

all_stickers_images = os.listdir("./static/all_stickers_images")
all_stickers_info = os.listdir("./static/all_stickers_info")
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('home.html', all_stickers_images=all_stickers_images)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/step_2/<selected_stickers_array>', methods=['GET'])
def step_2(selected_stickers_array):
    selected_stickers_array = selected_stickers_array.replace("selected_stickers_array=", "")
    selected_stickers_array = selected_stickers_array.split(",")
    # Randomly choose 3
    selected_stickers_array = sample(selected_stickers_array, 3)
    # Read data of sticker
    sticker_images_and_data = {}
    for sticker in selected_stickers_array:
        sticker = sticker.replace("jpg", "json")
        with open(f"./static/all_stickers_info/{sticker}") as f:
            sticker_data = f.read()
            sticker_images_and_data[sticker.replace("json", "jpg")] = sticker_data

    return render_template('step_2.html', sticker_images_and_data=sticker_images_and_data)

if __name__ == '__main__':
    app.run(debug=True)
