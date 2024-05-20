"""
Project Name: SELBAC - Cable Cost Estimator using Boruvka Algorithm
Filename: main.py
Title: Main flask application
Designed & Developed by:
    Farhaan
    Naveen
    Raghava
Github: @raghavtwenty
Date Created: May 20, 2023 | Last Updated: May 20, 2024
Version Info: 1.20052024 | Stable Release
Language: Python  | Version: 3.10.14,  64-bit
"""

# Importing required libraries
from flask import Flask, render_template, request, jsonify
from requests import get
from datetime import datetime
import json
import _1_algorithm as ImpBoruvka
import _2_network_graph as NetworkDraw


# Flask App
app = Flask(__name__)


# Final output route
@app.route("/final")
def finalPage():

    # Show the network graph
    NetworkDraw.drawNetwork(filtered_data)

    starting_houses = [i[0] for i in final_path]
    connecting_houses = [j[1] for j in final_path]
    distances = [k[2] for k in final_path]

    return render_template(
        "_h3_j2_final.html",
        hStartingHouses=starting_houses,
        hConnectingHouses=connecting_houses,
        hDistances=distances,
        hFinalCost=final_cost,
    )


# Processing route
@app.route("/output", methods=["POST"])
def outputPage():
    global final_path, final_cost, filtered_data

    # Retrieve the output
    str_houses_data = request.get_json(force=True)
    # print(strHousesData)

    # Convert to dictionary
    dict_houses_data = json.loads(str_houses_data)
    # print(f"USER INPUT HOUSES DATA : {dict_houses_data}")

    # Remove empty input values
    filtered_data = {}
    for key, value in dict_houses_data.items():
        if not all(item == "" for item in value):
            filtered_data[key] = value

    # Pass the value to the boruvka
    final_path, final_cost = ImpBoruvka.callAlgo(filtered_data)

    # Temp show
    # print(f"\nSHORTEST PATH AS PER BORUVKA : {Final_Path}")
    # print(f"\nLEAST PATH COST : {Final_Cost}")

    # Return a JSON response
    return jsonify(
        status="success",
        final_path=final_path,
        final_cost=final_cost,
    )


# Input route
@app.route("/input")
def sec_page():
    return render_template("_h2_j1_input.html")


# Default route
@app.route("/")
def home():
    return render_template("_h1_j0_home.html")


# Home route
@app.route("/home")
def back_home():
    return render_template("_h1_j0_home.html")


# Main
if __name__ == "__main__":
    app.run()
