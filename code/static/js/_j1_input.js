/*
Filename: _j1_input.js
Title: Selbac - Get the input from the user
Author: Raghava | GitHub: @raghavtwenty
Date Created: May 20, 2023 | Last Updated: May 20, 2024
Language: JavaScript | Version: Safari
*/

// Show the value in the console
//console.log("INPUT JS : " + jTotalNodes);

// Variables
let jTotalNodes;
let jConnHouses;
let jConnDis;
var jCurrNode = 1;
var jTempCurrNode = 2;

// House content
let jHouses = {};
let jHousesLocalStorage;

// Total houses top show
window.onload = function () {
    // Get the total nodes from the local storage of the home page
    jTotalNodes = localStorage.getItem("Total Houses");

    document.getElementById("hTotalNodesOp").textContent =
        "Total Number of Houses : " + jTotalNodes;

    document.getElementById("hCurrentNode").innerText =
        "Current House Number : " + 1;
};

// Input loop
async function jNextNodeInput() {
    // Current house number less than total house number
    if (jCurrNode <= jTotalNodes) {
        document.getElementById("hCurrentNode").innerText =
            "Current House Number : " + jTempCurrNode;

        // Retrieve the values
        jConnHouses = document.getElementById("hConnNodes").value;
        jConnDis = document.getElementById("hConnDis").value;

        // After parsing the input, set to empty for next iteration
        document.getElementById("hConnNodes").value = "";
        document.getElementById("hConnDis").value = "";

        // Temp show in console
        // console.log("CONNECTING NODES : " + jConnHouses);
        // console.log("CONNECTING DISTANCES : " + jConnDis);

        // Append to the json
        jHouses[jCurrNode] = [jConnHouses, jConnDis];

        // Temp show of json
        // console.log(jHouses);

        // JSON to string for local storage
        jHousesLocalStorage = JSON.stringify(jHouses);

        // Set local storage
        localStorage.setItem("Houses Data", jHousesLocalStorage);

        // Calculate distance when the current house number equal the last house number
        if (jCurrNode == jTotalNodes) {
            document.getElementById("hCurrentNode").innerText = "CLICK NEXT";
            $.ajax({
                url: "/output",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify(jHousesLocalStorage),
                success: function (response) {
                    window.location.href = "final";
                    localStorage.removeItem("Houses Data");
                },
                error: function (error) {
                    console.log("Error:", error);
                }
            });
        }

        // Update the current house number
        jCurrNode += 1;
        jTempCurrNode += 1;
    }
}
