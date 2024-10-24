import { useState, useEffect } from 'react';

export const useWebSocket = (url: string) => {
  const [data, setData] = useState(null);
  const [socket, setSocket] = useState<WebSocket | null>(null);

  useEffect(() => {
    const ws = new WebSocket(url);
    
    ws.onmessage = (event) => {
      const newData = JSON.parse(event.data);
      setData(newData);
    };

    setSocket(ws);

    return () => {
      ws.close();
    };
  }, [url]);

  return { data, socket };
};
