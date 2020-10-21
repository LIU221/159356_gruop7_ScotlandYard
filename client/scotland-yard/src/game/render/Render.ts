import { Point } from '../common/point';
import { PortraitType } from '../common/PortraitType';

export class Render {
    private __canvasElement: HTMLCanvasElement;
    private __ctx: CanvasRenderingContext2D;
    private __height: number;
    private __width: number;


    constructor(domElement: Element, height: number, width: number) {
        this.__canvasElement = this._createCanvasElement(height, width);
        const ctx =  this.__canvasElement.getContext('2d') as CanvasRenderingContext2D;
        this.__ctx = ctx;
        this.__height = height;
        this.__width = width;
        domElement.appendChild(this.__canvasElement);
    }

    private _createCanvasElement(height: number, width: number): HTMLCanvasElement {
        const result = document.createElement('canvas');
        result.setAttribute('height', height.toString());
        result.setAttribute('width', width.toString());
        return result;
    }

    public drawMap(img: HTMLImageElement) {
        this.__ctx.drawImage(img, 0, 0, this.__width, this.__height);
    }

    public drawPortrait(img: HTMLImageElement, x: number, y: number, height: number, width: number): void {
        this.__ctx.drawImage(img, x * this.__width - width/2, y * this.__height - height/2, height, width);
        // this.__ctx.fillStyle = "red";
        // this.__ctx.rect(x * this.__width, y * this.__height, height, width);
        // this.__ctx.fill();
        console.log('dont work');
    }

}