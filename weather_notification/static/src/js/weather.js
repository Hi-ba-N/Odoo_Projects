/** @odoo-module **/
console.log('weather')
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
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
            date: new Date().toLocaleDateString(),
            error:null,
            time : new Date().toLocaleTimeString(),
            is_weather:false
           });
            onWillStart(async () => {
                await this.fetchWeather();
            });
       }

    reload(){
         this.fetchWeather();
    }
    async fetchWeather() {
       console.log(this.state.is_weather)
        try{
         const api_values = await this.orm.searchRead("res.users", [["is_weather_api", "=", true]],['api_key','city','is_weather_api'])
         const city= (api_values[0].city)
         const api = (api_values[0].api_key)
         this.state.is_weather=(api_values[0].is_weather_api)
         if (city && api ) {
                    const response = await fetch("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api+"&units=metric");
                    const data = await response.json();
                    console.log(data)
                    if (response.ok) {
                    this.state.weather = {
                        temp: data.main.temp,
                        main: data.weather[0].main,
                        description: data.weather[0].description,
                        city : data.name,
                        icon : `http://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`,
                    };
                    }
                    else{
                       this.state.error = data.message
                    }
         }
         else{
         this.state.error = "Api key or City not found"
         }
        }catch (error) {
            this.state.error = 'Failed to fetch weather information';

        }


    }

}

   WeatherNotification.template = "weather_notification.Weather";
   WeatherNotification.components = {Dropdown, DropdownItem };
   export const systrayItem = { Component: WeatherNotification,};
   registry.category("systray").add("WeatherNotification", systrayItem, { sequence: 100 });





