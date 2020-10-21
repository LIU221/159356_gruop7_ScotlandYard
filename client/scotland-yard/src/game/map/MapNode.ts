// import { Point } from "../common/point";

export class MapNode {
    public id: number;
    // public location: Point;
    public x: number;
    public y: number;
    public taxiDestination: number[];
    public busDestination: number[];
    public undergroundDestination: number[];

    /**
     *
     * @param location
     * @param busDestination
     * @param taxiDestination
     * @param undergroundDestination
     */
    constructor(id: number, x: number, y: number, busDestination: number[], taxiDestination: number[], undergroundDestination: number[]) {
        this.id = id;
        this.x = x;
        this.y = y;
        // this.location = location;
        this.taxiDestination = taxiDestination;
        this.busDestination = busDestination;
        this.undergroundDestination = undergroundDestination;
    }
}
