import React from 'react';
import { useMaritimeContext } from '../contexts/MaritimeContext';
import { useAlerts } from '../hooks/useAlerts';

export const AlertPanel: React.FC = () => {
  const { alerts } = useAlerts();
  const { dispatch } = useMaritimeContext();

  const handleDismiss = (alertId: string) => {
    dispatch({ type: 'DISMISS_ALERT', payload: alertId });
  };

  return (
    <div className="alert-panel">
      <h2>Active Alerts</h2>
      {alerts.map(alert => (
        <div className="alert-item" key={alert.id}>
          <span className={`alert-level-${alert.level}`}>{alert.message}</span>
          <time>{alert.timestamp}</time>
          <button onClick={() => handleDismiss(alert.id)}>Dismiss</button>
        </div>
      ))}
    </div>
  );
};