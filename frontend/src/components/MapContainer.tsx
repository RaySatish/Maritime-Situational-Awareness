import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import { useWebSocket } from '../hooks/useWebSocket';

const MaritimeMap: React.FC = () => {
  const [markers, setMarkers] = useState<Array<{ coordinates: [number, number]; info: string }>>([]);
  const { data: wsData } = useWebSocket('ws://localhost:8000/ws');

  useEffect(() => {
    if (wsData) {
      const updateMarkers = (data: any) => {
        // Assuming wsData is an array of marker objects
        setMarkers(data.map((item: any) => ({
          coordinates: [item.latitude, item.longitude],
          info: item.vesselName || 'Unknown Vessel'
        })));
      };

      updateMarkers(wsData);
    }
  }, [wsData]);

  return (
    <MapContainer center={[0, 0]} zoom={3}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      {markers.map((marker, index) => (
        <Marker key={index} position={marker.coordinates}>
          <Popup>{marker.info}</Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default MaritimeMap;