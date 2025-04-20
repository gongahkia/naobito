import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [panels, setPanels] = useState([]);
  const [isProcessing, setIsProcessing] = useState(false);

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    setIsProcessing(true);
    const formData = new FormData();
    formData.append('file', file);
    try {
      const response = await axios.post('http://localhost:5000/api/process', formData);
      setPanels(response.data.panels);
    } catch (error) {
      console.error('Error processing image:', error);
    }
    setIsProcessing(false);
  };

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <header className="mb-12 text-center">
        <h1 className="text-4xl font-bold text-gray-800 mb-2">Naobito</h1>
        <p className="text-gray-600">A Small Manga Panel Extractor</p>
      </header>
      <div className="max-w-2xl mx-auto mb-12">
        <label className="block bg-white rounded-lg shadow-md p-8 text-center cursor-pointer hover:bg-gray-50 transition-colors">
          <input 
            type="file" 
            className="hidden" 
            accept="image/*"
            onChange={handleFileUpload}
            disabled={isProcessing}
          />
          <span className="text-lg text-gray-700">
            {isProcessing ? 'Processing...' : 'Upload Manga Image'}
          </span>
        </label>
      </div>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-6 max-w-6xl mx-auto">
        {panels.map((panel, index) => (
          <div key={index} className="bg-white rounded-lg shadow-md overflow-hidden">
            <img 
              src={`http://localhost:5000/panels/${panel}`} 
              alt={`Panel ${index + 1}`}
              className="w-full h-64 object-contain"
            />
            <div className="p-4 text-center">
              <span className="text-gray-600">Panel {index + 1}</span>
            </div>
          </div>
        ))}
      </div>
      <footer className="mt-12 text-center text-gray-600">
        <p>Made with ❤️ by Gabriel Ong</p>
      </footer>
    </div>
  );
}

export default App;