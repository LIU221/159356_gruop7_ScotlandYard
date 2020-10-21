import { MapNode } from './map/MapNode';

export class Game {
    private __datas: Object;
    private __startLocations: number[];
    private __nodes: MapNode[];

    constructor() {
        this.__datas = this.loadData();
        this.__startLocations = this.__datas['startLocations'] as number[];
        this.__nodes = this._createNodes(this.__datas);
  
    }

    private _createNodes(data: Object): MapNode[] {
        const nodeLocations = data['nodeLocations'];
        const trafficNetwork = data['trafficNetwork'];
        const result: MapNode[] = [];

        for (const iterator of nodeLocations) {
            const id = iterator['id'] as number;
            const x = iterator['x'] as number;
            const y = iterator['y'] as number;
            // const pt = new Point(x, y);
            const trafficNode = trafficNetwork[id-1];
            let taxi: number[] = [];
            let bus: number[] = [];
            let underground: number[] = [];
            if (trafficNode != null) {
                taxi = trafficNode['taxi'] as number[];
                bus = trafficNode['bus'] as number[];
                underground = trafficNode['underground'] as number[];
            }
            
            
            result.push(new MapNode(id, x, y, bus, taxi, underground));
        }
        return result;
    }


    /**
     * 
     */
    private loadData(): Object {
        const data = require('./config/map.config.json');
        // console.log(data);
        return data;
    }

    public getNodeWithIndex(index: number): MapNode {
        return this.__nodes[index - 1];
    }

    public getStartLocation(): number {
        const num = Math.floor(Math.random()*10)
        return this.__startLocations[num];
    }

    
}