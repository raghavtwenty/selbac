/*
Filename: _j0_home.js
Title: Selbac - Home page
Author: Raghava | GitHub: @raghavtwenty
Date Created: May 20, 2023 | Last Updated: May 20, 2024
Language: JavaScript | Version: Safari
*/

let jTotalNodes;

function hHomeSubmit() {
	jTotalNodes = document.getElementById("hTotalNodes").value;

	// Console show
	//console.log("HOME JS : " + jTotalNodes);

	// Set the value to the local storage
	localStorage.setItem("Total Houses", jTotalNodes);

	// Go to the input page
	window.location.href = "input";
}
