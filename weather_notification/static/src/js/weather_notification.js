/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { Dropdown } from '@web/core/dropdown/dropdown';
import { DropdownItem } from '@web/core/dropdown/dropdown_item';
import { ajax } from '@web/core/ajax'; // To make AJAX requests to the backend

class WeatherNotification extends Component {
    setup() {
        super.setup(...arguments);

        // Initialize the state to hold weather data
        this.state = useState({
            weather: null,
            error: null,
        });

        // Fetch the weather info when the component starts
        onWillStart(async () => {
            await this.fetchWeather();
        });
    }

    async fetchWeather() {
        try {
            // Make a call to the Odoo server to get the user's city and API key
            const userInfo = await ajax.rpc('/get_weather_info', {});
            const { city, apiKey } = userInfo;

            if (city && apiKey) {
                // Fetch weather information using the OpenWeatherMap API (or any other API)
                const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`);
                const data = await response.json();

                if (response.ok) {
                    // Update the state with the fetched weather data
                    this.state.weather = {
                        temp: data.main.temp,
                        description: data.weather[0].description,
                    };
                } else {
                    this.state.error = data.message || 'Error fetching weather data';
                }
            } else {
                this.state.error = 'City or API Key not found';
            }
        } catch (error) {
            this.state.error = 'Failed to fetch weather information';
        }
    }
}

WeatherNotification.template = "weather_notification.Weather";
WeatherNotification.components = { Dropdown, DropdownItem };

export const systrayItem = { Component: WeatherNotification };
registry.category("systray").add("WeatherNotification", systrayItem, { sequence: 100 });
