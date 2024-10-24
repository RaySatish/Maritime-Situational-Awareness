import { Box, Container } from '@mui/material';
import React, { useState } from 'react';
import Map from './components/Map';
import ReportUpload from './components/ReportUpload';
import AlertPanel from './components/src/components/AlertPanel';

function App() {
  const [contacts, setContacts] = useState([]);
  const [alerts, setAlerts] = useState([]);

  const handleContactDetected = (data) => {
    setContacts([...contacts, data.contact]);
    if (data.alert) {
      setAlerts([...alerts, data.alert]);
    }
  };

  return (
    <Container>
      <Box sx={{ my: 4 }}>
        <ReportUpload onContactDetected={handleContactDetected} />
        <Map contacts={contacts} />
        <AlertPanel alerts={alerts} />
      </Box>
    </Container>
  );
}

export default App;
