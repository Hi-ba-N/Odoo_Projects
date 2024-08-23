/** @odoo-module */
console.log('snippet')
import PublicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToElement } from "@web/core/utils/render";

var latest_events = PublicWidget.Widget.extend({
 selector: '.latest_event',
// willStart: async function() {
// console.log('lllkk')
////const data = await rpc('/latest_events', {})
//
//}
////        	var self = this;
////        	await jsonrpc.query({
////            	route: '/latest_events',
////        	}).then((data) => {
////            	this.data = data;
////
////        	});
////
////    	},
////    	start: function() {
////        	var chunks = _.chunk(this.data, 4)
////        	chunks[0].is_active = true
////        	this.$el.find('#courosel').html(
////            	qweb.render('elearning_course_snippet.event_latest_snippet', {
////                	chunks
////            	})
////        	)
////    	},
	});
//	PublicWidget.registry.dynamic_snippet_blog = Dynamic;
//	return Dynamic;
//













