
export type IEventHandler = (sender: any, args: EventArgs) => void;

class EventHandler {
    handler: IEventHandler;
    self: any;
    constructor(handler: IEventHandler, self: any) {
        this.handler = handler;
        this.self = self;
    }
}
export class Event {
    private _handlers: EventHandler[] = [];

    addHandler(handler: IEventHandler, self?: any): void {
        this._handlers.push(new EventHandler(handler, self));
    }

    removeHandler(handler: IEventHandler, self?: any): void {
        for (let i: number = 0; i < this._handlers.length; i++) {
            var l: EventHandler = this._handlers[i];
            if (l.handler == handler || handler == null) {
                if (l.self == self || self == null) {
                    this._handlers.splice(i, 1);
                    if (handler && self) {
                        break;
                    }
                }
            }
        }
    }

    removeAllHandlers(): void {
        this._handlers.length = 0;
    }

    raise(sender: any, args: EventArgs = EventArgs.empty): void {
        for (let i: number = 0; i < this._handlers.length; i++) {
            var l: EventHandler = this._handlers[i];
            l.handler.call(l.self, sender, args);
        }
    }
    get hasHandlers(): boolean {
        return this._handlers.length > 0;
    }
}

export class EventArgs {
    /**
     * Provides a value to use with events that do not have event data.
     */
    static empty: EventArgs = new EventArgs();
}


export class NetEventArgs {
    /**
     * Provides a value to use with events that do not have event data.
     */
    static empty: EventArgs = new EventArgs();
}
