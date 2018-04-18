import { get } from 'lodash';
import { RiskEntities } from '../../enums/risk-entities';

export interface GeneralObject {
	projectName: string,
	simulationTime: number,
	numberOfSimulations: number,
	indoorTemperature: number,
	elevation: number,
	indoorPressure: number,
	humidity: number,
}

export class General {

	private _projectName: string;
	private _simulationTime: number;
	private _numberOfSimulations: number;
	private _indoorTemperature: number;
	private _elevation: number;
	private _indoorPressure: number;
	private _humidity: number;

	private _heatReleaseRate: any;
	private _originOfFire: any;

	constructor(jsonString: string) {

		let base: GeneralObject;
		base = <GeneralObject>JSON.parse(jsonString);

		let GENERAL = RiskEntities.general;

		this.projectName = get(base, 'projectName', GENERAL.projectName.default) as string;
		this.simulationTime = get(base, 'simulationTime', GENERAL.simulationTime.default) as number;
		this.numberOfSimulations = get(base, 'numberOfSimulations', GENERAL.numberOfSimulations.default) as number;
		this.indoorTemperature = get(base, 'indoorTemperature', GENERAL.indoorTemperature.default) as number;
		this.elevation = get(base, 'elevation', GENERAL.elevation.default) as number;
		this.indoorPressure = get(base, 'indoorPressure', GENERAL.indoorPressure.default) as number;
		this.humidity = get(base, 'humidity', GENERAL.humidity.default) as number;

	}

    /**
     * Getter projectName
     * @return {string}
     */
	public get projectName(): string {
		return this._projectName;
	}

    /**
     * Setter projectName
     * @param {string} value
     */
	public set projectName(value: string) {
		this._projectName = value;
	}

    /**
     * Getter simulationTime
     * @return {number}
     */
	public get simulationTime(): number {
		return this._simulationTime;
	}

    /**
     * Setter simulationTime
     * @param {number} value
     */
	public set simulationTime(value: number) {
		this._simulationTime = value;
	}

    /**
     * Getter numberOfSimulations
     * @return {number}
     */
	public get numberOfSimulations(): number {
		return this._numberOfSimulations;
	}

    /**
     * Setter numberOfSimulations
     * @param {number} value
     */
	public set numberOfSimulations(value: number) {
		this._numberOfSimulations = value;
	}

    /**
     * Getter indoorTemperature
     * @return {number}
     */
	public get indoorTemperature(): number {
		return this._indoorTemperature;
	}

    /**
     * Setter indoorTemperature
     * @param {number} value
     */
	public set indoorTemperature(value: number) {
		this._indoorTemperature = value;
	}

    /**
     * Getter elevation
     * @return {number}
     */
	public get elevation(): number {
		return this._elevation;
	}

    /**
     * Setter elevation
     * @param {number} value
     */
	public set elevation(value: number) {
		this._elevation = value;
	}

    /**
     * Getter indoorPressure
     * @return {number}
     */
	public get indoorPressure(): number {
		return this._indoorPressure;
	}

    /**
     * Setter indoorPressure
     * @param {number} value
     */
	public set indoorPressure(value: number) {
		this._indoorPressure = value;
	}

    /**
     * Getter humidity
     * @return {number}
     */
	public get humidity(): number {
		return this._humidity;
	}

    /**
     * Setter humidity
     * @param {number} value
     */
	public set humidity(value: number) {
		this._humidity = value;
	}

	public toJSON(): object {
		let general = {
			projectName: this.projectName,
			simulationTime: this.simulationTime,
			numberOfSimulations: this.numberOfSimulations,
			indoorTemperature: this.indoorTemperature,
			elevation: this.elevation,
			indoorPressure: this.indoorPressure,
			humidity: this.humidity
		}
		return general;
	}


}
