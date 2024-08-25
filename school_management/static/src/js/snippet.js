/** @odoo-module */
console.log('snippet')
import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToFragment } from "@web/core/utils/render";
import { registry } from "@web/core/registry";
import { renderToElement } from "@web/core/utils/render";

console.log('abc')
export function _chunk(array, size) {
    const result = [];
    for (let i = 0; i < array.length; i += size) {
        result.push(array.slice(i, i + size));
    }
    return result;
}

var LatestEvent = publicWidget.Widget.extend({
        selector: '.latest_event',

        willStart: async function () {
        const events = await jsonrpc('/latest_events', {});
        console.log('events',events)
        const chunks = _chunk(events, 4);
        console.log('chunks',chunks)
        Object.assign(this, {
            events,
            chunks
        });
    },
    start: function () {
        const refEl = this.$el.find("#event_latest");
        const { chunks } = this;
        console.log('chunksss',chunks)
        refEl.html(renderToFragment('school_management.event_latest_snippet', {
            chunks
        }));

    }
	});
publicWidget.registry.LatestEvent = LatestEvent;










