/** @odoo-module **/
console.log('weather')
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
//import { Component } from "@odoo/owl";
import {Dropdown} from '@web/core/dropdown/dropdown';
import {DropdownItem} from '@web/core/dropdown/dropdown_item';
import { onWillStart,useState,Component } from "@odoo/owl";


class WeatherNotification extends Component {
    setup() {
           super.setup(...arguments);
           console.log(this)
            this.orm = useService("orm");
            this.state = useState({
            weather: null,
            error: null,
            date: new Date().toLocaleDateString(),
            time : new Date().getHours()

           });
            onWillStart(async () => {
                await this.fetchWeather();
            });
       }
    async fetchWeather() {
        console.log('fetch weather')
         const api_values = await this.orm.searchRead("res.users", ["&", ["api_key", "!=", false], ["city", "!=", false]],['api_key','city']);
         console.log(api_values)
         const city= (api_values[0].city)
         const api = (api_values[0].api_key)
         console.log(api)
         if (city && api) {

                    const response = await fetch("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api+"&units=metric");
                    console.log('res',response)
                    const data = await response.json();
                    console.log(data)
                    if (response.ok) {
                      console.log('response')
                    this.state.weather = {
                        temp: data.main.temp,
                        main: data.weather[0].main,
                        description: data.weather[0].description,
                        city : data.name,
                        icon : data.weather[0].icon
                    };
                    }
                    else {
                         console.log('errror')
                    }
         }
         else {
                  console.log('else error')
         }


    }



}
   WeatherNotification.template = "weather_notification.Weather";
    WeatherNotification.components = {Dropdown, DropdownItem };
   export const systrayItem = { Component: WeatherNotification,};
   registry.category("systray").add("WeatherNotification", systrayItem, { sequence: 100 });




