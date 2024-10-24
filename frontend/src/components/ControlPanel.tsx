import React from 'react';
import { LayerControl } from './LayerControl';
import { TimelineControl } from './TimelineControl';
import { FormControl, Select, MenuItem } from '@material-ui/core';

export const ControlPanel: React.FC = () => {
  return (
    <div className="control-panel">
      <LayerControl />
      <TimelineControl />
      <div className="filter-controls">
        <FormControl>
          <Select defaultValue="all">
            <MenuItem value="all">All Vessels</MenuItem>
            <MenuItem value="threats">Potential Threats</MenuItem>
            <MenuItem value="commercial">Commercial Vessels</MenuItem>
          </Select>
        </FormControl>
      </div>
    </div>
  );
};