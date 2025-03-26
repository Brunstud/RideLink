import axios from 'axios';

const API_URL = 'http://localhost:5000/rides';

export const getRides = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching rides:', error);
    return [];
  }
};

export const addRide = async (ride) => {
  try {
    await axios.post(API_URL, ride);
  } catch (error) {
    console.error('Error adding ride:', error);
  }
};
