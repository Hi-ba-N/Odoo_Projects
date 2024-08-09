/* @odoo-module */
//import { Component } from "@odoo/owl";
//const {Component} = owl
import { DemoComponent } from "@test_module/js/demo_component";

import {registry} from "@web/core/registry";

import {
    Component,
    useState,
    mount,
    useComponent,
    onWillStart,
    onMounted,
    onWillUnmount,
    onWillUpdateProps,
    onPatched,
    onWillPatch,
    onWillRender,
    onRendered,
    onWillDestroy,
} from "@odoo/owl";



export class Workshop extends owl.Component {
static components = {  DemoComponent };

static template = "workshop"
    setup() {
        console.log('hello')
        this.sample='first'
        this.sample2='second'

        const component = useComponent();
    const name = component.constructor.name;
    onWillStart(() => console.log(`${name}:willStart`));
    onMounted(() => console.log(`${name}:mounted`));
    onWillUpdateProps(() => console.log(`${name}:willUpdateProps`));
    onWillRender(() => console.log(`${name}:willRender`));
    onRendered(() => console.log(`${name}:rendered`));
    onWillPatch(() => console.log(`${name}:willPatch`));
    onPatched(() => console.log(`${name}:patched`));
    onWillUnmount(() => console.log(`${name}:willUnmount`));
    onWillDestroy(() => console.log(`${name}:willDestroy`));

    this.state = useState({ value: 0,toggle:true });
//this.value=0

}
 add(){
this.state.value = parseInt(this.state.value) +1
console.log(this.value)
    }
    decrement(){
this.state.value = parseInt(this.state.value) -1
console.log(this.value)


    }

    }




registry.category('actions').add('workshop', Workshop);
