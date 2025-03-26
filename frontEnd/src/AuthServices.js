import axios from 'axios';

const API_URL = window.location.hostname.includes("localhost")
  ? "http://127.0.0.1:8000/api/"
  : "https://9vtnjg7h-8000.use2.devtunnels.ms/api/";

export const register = async (username, password) => {
    try {
        const response = await axios.post(API_URL + "registro/", { username, password });
        return response.data; 
    } catch (error) {
        console.error("Error en el registro:", error.response?.data || error.message);
        throw error; 
    }
};

export const login = async (username, password) => {
    try {
        const response = await axios.post(API_URL + "ingreso/", { username, password });
        return response.data;
    } catch (error) {
        console.error("Error en el login:", error.response?.data || error.message);
        throw error;
    }
};


