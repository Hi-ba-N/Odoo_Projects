/** @odoo-module **/
console.log('weather')
import { registry } from "@web/core/registry";
//import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import {Dropdown} from '@web/core/dropdown/dropdown';
import {DropdownItem} from '@web/core/dropdown/dropdown_item';


class WeatherNotification extends Component {
setup() {
       super.setup(...arguments);
       console.log(this)
//       this.action = useService("action");
   }
//
//   displayWeather(){
//   console.log('button clickk')
//
//   }
}
   WeatherNotification.template = "weather_notification.Weather";
    WeatherNotification.components = {Dropdown, DropdownItem };
   export const systrayItem = { Component: WeatherNotification,};
   registry.category("systray").add("WeatherNotification", systrayItem, { sequence: 100 });




