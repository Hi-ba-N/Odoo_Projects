/* @odoo-module */
const {Component, onMounted, useState, useEffect} = owl
import { useService } from "@web/core/utils/hooks";


import {registry} from "@web/core/registry";

export class SampleService extends Component {
    static template = 'workshop.SampleService'

    setup(){
        this.rpc = useService('rpc') //this.env.services.rpc
        this.orm = useService('orm') //this.env.services.orm
        this.action = useService('action') //this.env.services.action
        this.notification = useService("notification"); //this.env.services.notification

        this.state = useState({
            data:{}
        })

        onMounted(async()=> {
            await this.fetchData()
        })
    }



    clientAction(){
          this.action.doAction(
            {
                type: "ir.actions.client",
                tag: "counter",
                name: "Counter Component",
            })
    }

    windowAction(){
        this.action.doAction({
            type: "ir.actions.act_window",
            res_model: 'sale.order',
            views: [[false, "list"], [false, "form"]],
            view_mode: "list",
            target: "new",
        });
    }


    addNotification(){
         this.notification.add(
                "This is Notification!",
                { title:"Notification title", type: "success" }
            );
    }

    async fetchData(){
        //this.orm.call
        this.state.data = await this.orm.searchRead(
            "res.partner",
            [],
            ["id", "name"],
            { limit: 10 }
        );
    }

 async archive_action(id){
console.log('function work')
 await this.orm.call('res.partner', "action_archive", [id])
            await this.fetchData()

    }

}


registry.category('actions').add('sample_service', SampleService);