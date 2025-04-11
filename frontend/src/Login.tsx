import React, { useState } from "react";
import axios from "axios";
import "./login.css";

interface User {
  username: string;
  email: string;
}

const Login: React.FC = () => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [message, setMessage] = useState<string>("");
  const [user, setUser] = useState<User | null>(null);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/api/login", {
        username: username,
        password: password,
      });
      const userDetails = response.data.user; // Assuming the API returns user details
      setUser(userDetails);
      setMessage("");
    } catch (error) {
      setMessage("Login failed. Please check your credentials.");
    }
  };

  const handleLogout = () => {
    setUser(null);
    setUsername("");
    setPassword("");
    setMessage("You have been logged out.");
  };

  if (user) {
    return (
      <div className="dashboard">
        <h1>Welcome, {user.username}!</h1>
        <p>Email: {user.email}</p>
        <button onClick={handleLogout} className="button">
          Logout
        </button>
      </div>
    );
  }

  return (
    <div className="container">
      <div className="form-container">
        <h1>Login</h1>
        <form onSubmit={handleLogin} className="form">
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="input"
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="input"
          />
          <button type="submit" className="button">
            Login
          </button>
        </form>
        <p>{message}</p>
      </div>
    </div>
  );
};

export default Login;