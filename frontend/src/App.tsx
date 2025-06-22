import React from 'react';
import './App.css';

function App() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-200 to-purple-300">
      <h1 className="text-4xl font-bold text-blue-800 mb-4">Hello, Tailwind CSS!</h1>
      <p className="text-lg text-gray-700">
        Your React + Tailwind setup is working 🎉
      </p>
      <button className="mt-6 px-6 py-2 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transition">
        Test Button
      </button>
    </div>
  );
}

export default App;
