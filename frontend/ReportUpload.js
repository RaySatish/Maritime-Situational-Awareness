import React, { useState } from 'react';
import { Button, Box } from '@mui/material';
import axios from 'axios';

const ReportUpload = ({ onContactDetected }) => {
  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await axios.post('http://localhost:8000/api/reports/upload', formData);
    onContactDetected(response.data);
  };

  return (
    <Box>
      <Button variant="contained" component="label">
        Upload Report
        <input type="file" hidden onChange={handleFileUpload} />
      </Button>
    </Box>
  );
};

export default ReportUpload;
