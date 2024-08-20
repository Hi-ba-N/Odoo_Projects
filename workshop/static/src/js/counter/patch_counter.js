/* @odoo-module */
import { patch } from "@web/core/utils/patch";
import {Counter} from "@workshop/js/counter/counter";

patch(Counter.prototype, {

clear(){

this.state.value=0
},
increment(){
super.increment()
        this.state.value = parseInt(this.state.value) + 1



}


})
