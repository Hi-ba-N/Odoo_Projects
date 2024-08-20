/* @odoo-module */
const {Component, useState} = owl


import {registry} from "@web/core/registry";

export class Counter extends Component {
    static template = 'workshop.Counter'

    setup(){
        this.state = useState({
            value:0
        })
    }

    increment(){
        this.state.value = parseInt(this.state.value) + 1
    }

    decrement(){
        this.state.value = parseInt(this.state.value) - 1
    }

}


c