// src/api.js
import axios from "axios";

const instance = axios.create({
	baseURL: "http://localhost:5000", // Replace with your FastAPI server URL
	timeout: 5000, // Timeout in milliseconds
	headers: {
		"Content-Type": "application/json",
	},
});

export default instance;
