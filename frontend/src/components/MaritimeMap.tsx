import React, { useEffect, useState, useCallback } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import { LatLngTuple, Icon } from 'leaflet';
import { useMaritimeContext } from '../contexts/MaritimeContext';
import { MaritimeVessel } from '../types/maritime';
import { VesselMarker } from './VesselMarker';
import { VesselDetails } from './VesselDetails';
import 'leaflet/dist/leaflet.css';

const DEFAULT_CENTER: LatLngTuple = [0, 0];
const DEFAULT_ZOOM = 3;

export const MaritimeMap: React.FC = () => {
    const { state } = useMaritimeContext();
    const [selectedVessel, setSelectedVessel] = useState<MaritimeVessel | null>(null);

    const handleVesselSelect = useCallback((vessel: MaritimeVessel) => {
        setSelectedVessel(vessel);
    }, []);

    return (
        <div className="maritime-map-container">
            <MapContainer 
                center={DEFAULT_CENTER} 
                zoom={DEFAULT_ZOOM}
                style={{ height: '100%', width: '100%' }}
            >
                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution='© OpenStreetMap contributors'
                />
                {state.vessels.map(vessel => (
                    <VesselMarker
                        key={vessel.id}
                        vessel={vessel}
                        onSelect={handleVesselSelect}
                        isSelected={selectedVessel?.id === vessel.id}
                    />
                ))}
                {selectedVessel && (
                    <VesselDetails
                        vessel={selectedVessel}
                        onClose={() => setSelectedVessel(null)}
                    />
                )}
            </MapContainer>
        </div>
    );
};