import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
    <div className="bg-gray-800 shadow-2xl rounded-2xl">
      <div className="container mx-auto p-8">
        <div className="grid grid-cols-2 gap-4">
          <div className="space-y-8">
            <div className="flex flex-col">
              <h1 className="text-2xl text-red-500">Project 3 - Pathfinders</h1>
              <p className="text-gray-300 mb-8">By: <span className="font-bold">Nolan MacLear, Kevin Dao, and Ian Cook</span></p>
              <label htmlFor="origin" className="font-bold">
                Origin:
              </label>
              <input
                type="text"
                id="origin"
                className="border border-gray-300 rounded p-2"
              />
            </div>
            <div className="flex flex-col">
              <label htmlFor="destination" className="font-bold">
                Destination:
              </label>
              <input
                type="text"
                id="destination"
                className="border border-gray-300 rounded p-2"
              />
            </div>
            <div className="flex flex-col">
              <label htmlFor="algorithm" className="font-bold">
                Algorithm:
              </label>
              <select id="algorithm" className="border border-gray-300 rounded p-2">
                <option value="dijkstra">Dijkstra</option>
                <option value="aStar">A*</option>
              </select>

              <div className="mt-8 text-2xl">
                <p className="font-bold">Execution time: 46ms</p>
                <p className="font-bold">Path length: 28</p>
              </div>
            </div>
          </div>
          
          <div className="border-2 border-green-900 p-4 flex flex-col items-center">
            <h2 className="mb-4 font-bold text-gray-300 text-2xl">Calculated Route:</h2>
            <img src="/path/to/your/image" alt="Route" className="w-96 h-96 border border-green-800 rounded" />
          </div>
        </div>
      </div>
      </div>
    </>
  );
}

export default App;
