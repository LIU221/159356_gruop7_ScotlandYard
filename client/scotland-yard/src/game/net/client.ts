import WebSocket from 'isomorphic-ws';
import { NetEventArgs } from "./netevent"


export class Client {
    public static gClient: Client = null;
    public ws: WebSocket;
    public onmessage: WebSocket.MessageEvent;

    constructor(url: string) {
        this.ws = new WebSocket(url);
        this.ws.onopen = (evt: WebSocket.OpenEvent) => {
            this.onOpen(evt)
        };

        this.ws.onmessage = (evt: WebSocket.OpenEvent) => {
            console.log('WebSocket接收消息：');
            let data = JSON.parse(evt.data);
            console.log(data);
        }

        this.ws.onerror = (evt: WebSocket.ErrorEvent) => {
            this.onError(evt)
        };
    }

    public onOpen(evt: WebSocket.OpenEvent) {
    }


    public onError(evt: WebSocket.ErrorEvent) {
        this.ws.close();
    }

    public doSend(message: Object) {
        if (this.ws.readyState == 1) {
            this.ws.send(JSON.stringify(message));
        }
    }

}