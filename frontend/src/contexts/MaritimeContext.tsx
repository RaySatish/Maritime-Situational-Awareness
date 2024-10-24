import React, { createContext, useContext, useReducer, useCallback } from 'react';
import { MaritimeState, MaritimeAction } from '../types/maritime';

const initialState: MaritimeState = {
  vessels: [],
  alerts: [],
  loading: false,
  error: null
};

export const MaritimeContext = createContext<{
  state: MaritimeState;
  dispatch: React.Dispatch<MaritimeAction>;
}>({ state: initialState, dispatch: () => null });

export const maritimeReducer = (state: MaritimeState, action: MaritimeAction): MaritimeState => {
    switch (action.type) {
        case 'SET_VESSELS':
            return { ...state, vessels: action.payload };
        case 'ADD_ALERT':
            return { ...state, alerts: [...state.alerts, action.payload] };
        case 'DISMISS_ALERT':
            return { 
                ...state, 
                alerts: state.alerts.filter(alert => alert.id !== action.payload) 
            };
        case 'SET_LOADING':
            return { ...state, loading: action.payload };
        case 'SET_ERROR':
            return { ...state, error: action.payload };
        default:
            return state;
    }
};
export const MaritimeProvider: React.FC = ({ children }) => {
  const [state, dispatch] = useReducer(maritimeReducer, initialState);

  return (
      <MaritimeContext.Provider value={{ state, dispatch }}>
          {children}
      </MaritimeContext.Provider>
  );
};

export const useMaritimeContext = () => {
  const context = useContext(MaritimeContext);
  if (!context) {
      throw new Error('useMaritimeContext must be used within a MaritimeProvider');
  }
  return context;
};