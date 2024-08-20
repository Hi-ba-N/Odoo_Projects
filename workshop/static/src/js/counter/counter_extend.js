/* @odoo-module */


import {Counter} from "@workshop/js/counter/counter";
import {registry} from "@web/core/registry";

export class CounterExtend extends Counter {

 static template = 'workshop.CounterExtend'

    increment(){
        super.increment()
        this.state.value = parseInt(this.state.value) + 1
    }

     decrement(){
        this.state.value = parseInt(this.state.value) - 1
    }
    }

    registry.category('actions').add('counter_extend', CounterExtend);
