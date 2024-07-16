import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { io } from 'socket.io-client';

const Dashboard = () => {
  const [dishes, setDishes] = useState([]);
  const socket = io('http://localhost:5000');
  
  useEffect(() => {
    fetchDishes();
    socket.on('update', () => {
      fetchDishes();
      })
      
      return () => socket.disconnect();
  }, []);

  const fetchDishes = async () => {
    const response = await axios.get('http://localhost:5000/dishes');
    setDishes(response.data);
  };

  const togglePublish = async (id) => {
    await axios.post(`http://localhost:5000/toggle-publish/${id}`);
  };

  return (
    <div>
      <h1>Dish Dashboard</h1>
      <ul>
        {dishes.map((dish) => (
          <li key={dish.dishId}>
            <h2>{dish.dishName}</h2>
            <img src={dish.imageUrl} alt={dish.dishName} />
            <p>{dish.isPublished ? 'Published' : 'Unpublished'}</p>
            <button onClick={() => togglePublish(dish.dishId)}>
              {dish.isPublished ? 'Unpublish' : 'Publish'}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
