import { EventArgs } from "../utils/event"

export class NetEventArgs extends EventArgs {
    public type: string;
    public msg: string;

    constructor(type: string, msg: string) {
        super();
        this.type = type;
        this.msg = msg;
    }
}
