import { useState } from 'react';

function App() {
  const [movie, setMovie] = useState('');
  const [recommendations, setRecommendations] = useState([]);

  const handleSearch = async () => {
    if (!movie) return;
    
    try {
      const res = await fetch(`http://127.0.0.1:5000/recommend?movie=${encodeURIComponent(movie)}`);
      const data = await res.json();
      setRecommendations(data.recommendations);
    } catch (err) {
      alert("Error fetching recommendations");
      console.error(err);
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center p-10">
      <h1 className="text-3xl font-bold mb-6">🎥 Movie Recommender</h1>
      
      <div className="flex space-x-2 mb-6">
        <input
          type="text"
          value={movie}
          onChange={(e) => setMovie(e.target.value)}
          placeholder="Enter a movie name"
          className="px-4 py-2 w-80 rounded-md text-black"
        />
        <button
          onClick={handleSearch}
          className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-md font-semibold"
        >
          Recommend
        </button>
      </div>

      {recommendations.length > 0 && (
        <div className="mt-4 w-full max-w-md bg-white text-black rounded-lg shadow-md p-4">
          <h2 className="text-xl font-bold mb-3">Recommended Movies:</h2>
          <ul className="list-disc list-inside space-y-1">
            {recommendations.map((rec, idx) => (
              <li key={idx}>{rec}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
