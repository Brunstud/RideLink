<template>
  <div id="app">
    <h1>Carpool System</h1>
    <div>
      <h2>Available Rides</h2>
      <ul>
        <li v-for="ride in rides" :key="ride.driver">
          {{ ride.driver }} offers a ride to {{ ride.destination }} for {{ ride.passenger }}
        </li>
      </ul>
    </div>
    <div>
      <h2>Add a New Ride</h2>
      <input v-model="driver" placeholder="Driver Name" />
      <input v-model="passenger" placeholder="Passenger Name" />
      <input v-model="destination" placeholder="Destination" />
      <button @click="addNewRide">Add Ride</button>
    </div>
  </div>
</template>

<script>
import { getRides, addRide } from './services/rideService';

export default {
  data() {
    return {
      rides: [],
      driver: '',
      passenger: '',
      destination: ''
    };
  },
  async created() {
    this.rides = await getRides();
  },
  methods: {
    async addNewRide() {
      const ride = {
        driver: this.driver,
        passenger: this.passenger,
        destination: this.destination
      };
      await addRide(ride);
      this.rides = await getRides(); // Refresh rides list
    }
  }
};
</script>
