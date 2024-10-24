import React from 'react';
import { Snackbar, Alert } from '@material-ui/core';
import { useMaritimeContext } from '../contexts/MaritimeContext';

export const AlertSystem: React.FC = () => {
  const { state, dispatch } = useMaritimeContext();

  const handleClose = (alertId: string) => {
    dispatch({ type: 'DISMISS_ALERT', payload: alertId });
  };

  return (
    <>
      {state.alerts.map(alert => (
        <Snackbar
          key={alert.id}
          open={true}
          autoHideDuration={6000}
          onClose={() => handleClose(alert.id)}
        >
          <Alert severity={alert.severity}>
            {alert.message}
          </Alert>
        </Snackbar>
      ))}
    </>
  );
};

interface Alert {
    id: string;
    message: string;
    severity: 'error' | 'warning' | 'info' | 'success';
}
