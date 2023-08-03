import React, { useState, useRef } from 'react';
import { MapContainer, TileLayer, Polyline, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css'
import './App.css';

const App = () => {
  const [route, setRoute] = useState(null);
  const [executionTime, setExecutionTime] = useState(null);
  const [pathLength, setPathLength] = useState(null);
  const [start, setStart] = useState(null);
  const [end, setEnd] = useState(null);
  const [error, setError] = useState(null);
  const algorithm = useRef();

  const fetchRoute = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch(`http://localhost:3001/shortest_path/${algorithm.current.value}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ start: start, end: end }),
      });

      if (response.ok) {
        const data = await response.json();
        setRoute(data.path);
        setExecutionTime(data.executionTime);
        setPathLength(data.pathLength);
        setError(null);
      } else {
        setError(`Error: ${response.statusText}`);
      }
    } catch (err) {
      setError(`Error: ${err.message}`);
    }
  };

  const centerCoordinates = [29.6516, -82.3248];

  return (

    <div className="App text-3xl">
      <form onSubmit={fetchRoute} className=" flex flex-col items-center">
        <div className="w-3/4 m-16 p-16 bg-slate-800 space-y-4">
          <label className="block">
            Start:
            <input type="text" onChange={(e) => setStart(e.target.value)} className="border border-gray-300 px-3 py-2 w-full" />
          </label>
          <label className="block">
            End:
            <input type="text" onChange={(e) => setEnd(e.target.value)} className="border border-gray-300 px-3 py-2 w-full" />
          </label>
          <label className="block">
            Algorithm:
            <select ref={algorithm} className="border border-gray-300 px-3 py-2 w-full">
              <option value="dijkstra">Dijkstra</option>
              <option value="a_star">A*</option>
            </select>
          </label>
        </div>
        <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Calculate Route
        </button>
      </form>
      <div className="m-16">
      <MapContainer center={centerCoordinates} zoom={13} style={{ height: '400px', width: '100%' }}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          />
          {route && (
            <>
              <Polyline positions={route} color="blue" />
              <Marker position={route[0]} icon={L.divIcon({ className: 'icon', html: 'S' })} />
              <Marker position={route[route.length - 1]} icon={L.divIcon({ className: 'icon', html: 'E' })} />
            </>
          )}
        </MapContainer>
        <p>Execution time: {executionTime}</p>
        <p>Path length: {pathLength}</p>
        {error && <p>Error: {error}</p>}
      </div>


    </div>
  );
};

export default App;
