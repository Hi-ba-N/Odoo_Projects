/* @odoo-module */
import { Component } from "@odoo/owl";
//const {Component} = owl
//owl.Component

import { Child } from "./child"
//import { Child } from "@workshop/js/child_parent/child"


import {registry} from "@web/core/registry";

export class Parent extends Component {
    static template = 'workshop.Parent'
    static components = { Child }

    setup(){
        this.name = "Sample text"
    }

}


registry.category('actions').add('parent', Parent);