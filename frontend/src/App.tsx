import React from 'react';
import { ThemeProvider, CssBaseline } from '@material-ui/core';
import { createTheme } from '@material-ui/core/styles';
import { MaritimeProvider } from './contexts/MaritimeContext';
import { MainLayout } from './layouts/MainLayout';
import { AlertProvider } from './contexts/AlertContext';
import { WebSocketProvider } from './contexts/WebSocketContext';
import './styles/global.css';

const theme = createTheme({
    palette: {
        primary: {
            main: '#1976d2',
        },
        secondary: {
            main: '#dc004e',
        },
    },
});

const App: React.FC = () => {
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <WebSocketProvider>
                <MaritimeProvider>
                    <AlertProvider>
                        <MainLayout />
                    </AlertProvider>
                </MaritimeProvider>
            </WebSocketProvider>
        </ThemeProvider>
    );
};

export default App;