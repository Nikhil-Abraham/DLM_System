// src/App.js
import React, { useState } from "react";
import GridBatteryBuildingSupply from "./components/GridBatteryBuildingSupply";
import StationAndVehicleData from "./components/StationAndVehicleData";
import "./App.css";

const App = () => {
	const [supplyData, setSupplyData] = useState({
		internal_capacity: 2000,
		battery_capacity: 2000,
		battery_capacity_diverted: 300,
		battery_capacity_available: 1700,
		building_load: 200,
		available_capacity: 2100,
		capacity_utilization: 0,
	});
	return (
		<div className="App bg-slate-100">
			<div className="flex">
				<GridBatteryBuildingSupply
					internal_capacity={supplyData.internal_capacity}
					battery_capacity={supplyData.battery_capacity}
					battery_capacity_diverted={
						supplyData.battery_capacity_diverted
					}
					battery_capacity_available={
						supplyData.battery_capacity_available
					}
					building_load={supplyData.building_load}
					available_capacity={supplyData.available_capacity}
					capacity_utilization={supplyData.capacity_utilization}
				/>
				<StationAndVehicleData />
			</div>
		</div>
	);
};

export default App;
