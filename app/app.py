# app.py
# Author: Stefan Elmgren
# Date: 2025-03-21 - 2025-04-04

# from flask import Flask
# from flask import render_template
# import json
# import stalarm

# app = Flask(__name__)
# app.config["DEBUG"] = True  # Enable debug mode

# @app.route('/')
# @app.route('/index')
# def index():
#     # Convert DataFrame to dictionary for Jinja
#     df_data = stalarm.df_stock_data.to_dict(orient='records')

#     return render_template('index.html', df=df_data, columns=stalarm.df_stock_data.columns)

# if __name__ == "__main__":
#     app.run()

import os
import sys
from flask import Flask, render_template
import stalarm

def resource_path(relative_path):
    """ Get absolute path to resource (for dev and PyInstaller) """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# 🔥 FIX: Set correct folders here
app = Flask(
    __name__,
    template_folder=resource_path("templates"),
    static_folder=resource_path("static")
)


app.config["DEBUG"] = True

@app.route('/')
@app.route('/index')
def index():
    df_data = stalarm.df_stock_data.to_dict(orient='records')
    return render_template('index.html', df=df_data, columns=stalarm.df_stock_data.columns)

if __name__ == "__main__":
    import threading, webbrowser
    threading.Timer(1.0, lambda: webbrowser.open("http://127.0.0.1:5000/")).start()
    app.run()
