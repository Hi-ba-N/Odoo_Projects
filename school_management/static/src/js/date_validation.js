/** @odoo-module **/
import publicWidget from '@web/legacy/js/public/public_widget';
publicWidget.registry.ageCompute = publicWidget.registry.ageCompute.extend({
 selector: '#dob',
    events: {
        'change #dob': '_onChange'
})
