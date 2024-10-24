import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

const MaritimeMap = ({ vessels }) => {
    return (
        <MapContainer center={[0, 0]} zoom={3}>
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            {vessels.map(vessel => (
                <Marker 
                    position={[vessel.latitude, vessel.longitude]}
                    key={vessel.vessel_id}
                >
                    <Popup>
                        {`Type: ${vessel.vessel_type}\nSpeed: ${vessel.speed} knots`}
                    </Popup>
                </Marker>
            ))}
        </MapContainer>
    );
};
