import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
	faBolt,
	faBuilding,
	faBatteryFull,
	faBatteryEmpty,
	faArrowRight,
	faArrowLeft,
} from "@fortawesome/free-solid-svg-icons";

const GridBatteryBuildingSupply = ({
	internal_capacity,
	battery_capacity,
	battery_capacity_diverted,
	battery_capacity_available,
	building_load,
	available_capacity,
	capacity_utilization,
}) => {
	return (
		<div className="p-10 mt-5 ml-5 bg-slate-200 rounded-lg flex-col justify-around w-1/4">
			<div className="flex flex-col items-center justify-center p-10">
				<div className="mt-4 text-cente text-smr">
					<p className="text-lg text-gray-600">Grid</p>
				</div>
				<div className="flex flex-row justify-around items-center bg-slate-200 w-100 p-5">
					<div className="flex items-center justify-center shadow-sm rounded-full bg-slate-100 w-24 h-24">
						<FontAwesomeIcon
							icon={faBolt}
							className="text-slate-600 text-3xl"
						/>
					</div>
					<div className="px-3 ">
						<p className="text-sm text-slate-500">
							Capacity: {internal_capacity} KW
						</p>
						<p className="text-sm text-slate-500">
							Available: {available_capacity} KW
						</p>
						<p className="text-sm text-slate-500">
							Utilized: {capacity_utilization} KW
						</p>
					</div>
				</div>
			</div>
			<div className="flex flex-col items-center justify-center p-10">
				<div className="mt-4 text-cente text-smr">
					<p className="text-lg text-gray-600">Battery</p>
				</div>
				<div className="flex flex-row justify-center items-center p-5">
					<div className="flex items-center justify-center shadow-sm rounded-full bg-slate-100 w-24 h-24">
						<FontAwesomeIcon
							icon={faBatteryEmpty}
							className="text-slate-600 text-3xl"
						/>
					</div>
					<div className="px-3 ">
						<p className="text-sm text-slate-500">
							Capacity: {battery_capacity} KW
						</p>
						<p className="text-sm text-slate-500">
							Diverted: {battery_capacity_diverted} KW
						</p>
						<p className="text-sm text-slate-500">
							Available: {battery_capacity_available} KW
						</p>
					</div>
				</div>
			</div>
			<div className="flex flex-col items-center justify-center p-10">
				<div className="mt-4 text-cente text-smr">
					<p className="text-lg text-gray-600">Building</p>
				</div>
				<div className="flex flex-row justify-center items-center p-5">
					<div className="flex items-center justify-center shadow-sm rounded-full bg-slate-100 w-24 h-24">
						<FontAwesomeIcon
							icon={faBuilding}
							className="text-slate-600 text-3xl"
						/>
					</div>
					<div className="px-3 ">
						<p className="text-sm text-slate-500">
							Load: {building_load} KW
						</p>
					</div>
				</div>
			</div>
		</div>
	);
};

export default GridBatteryBuildingSupply;
