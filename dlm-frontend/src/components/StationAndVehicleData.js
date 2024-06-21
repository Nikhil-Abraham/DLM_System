import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlug, faCar } from "@fortawesome/free-solid-svg-icons";

const StationAndVehicleData = ({
	station_id,
	max_feasible_rate,
	charge_rate,
	charger_priority,
	vehicle_soc,
	vehicle_max_charging_rate,
	vehicle_scheduled_time,
	vehicle_desired_soc,
	estimated_charging_time,
}) => {
	return (
		<div className="m-5 p-10 bg-slate-200 rounded-lg w-3/4">
			<div className="felx justify-center rounded-lg items-center shadow-md w-1/4">
				<div className="rounded-lg flex flex-row justify-around items-center p-5">
					<FontAwesomeIcon
						icon={faPlug}
						className="text-slate-600 text-3xl"
					/>
					<div className="px-3 text-sm text-slate-600">
						<p>Station Name: {station_id}</p>
						<p>Charge Rate: {max_feasible_rate}</p>
						<p>Max Charge Rate: {charge_rate}</p>
						<p>Charger Priority: {charger_priority}</p>
					</div>
				</div>
				<div className="rounded-lg flex flex-row justify-around  items-center p-5">
					<FontAwesomeIcon
						icon={faCar}
						className="text-slate-600 text-3xl"
					/>
					<div className="px-3 text-sm text-slate-600">
						<p>SOC: {vehicle_soc}</p>
						<p>Max Charge Rate: {vehicle_max_charging_rate}</p>
						<p>Departure Time: {vehicle_scheduled_time}</p>
						<p>Desired SOC: {vehicle_desired_soc}</p>
						<p>
							Estimated Charging Time: {estimated_charging_time}
						</p>
					</div>
				</div>
			</div>
		</div>
	);
};

export default StationAndVehicleData;
