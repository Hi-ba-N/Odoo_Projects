/* @odoo-module */

export class Child extends owl.Component {
    static template = 'workshop.Child'
    static props = { sampleProps: { type: String, optional: true} }
    static defaultProps = {
        sampleProps: "Hi guys",
    };
    setup(){
        console.log("props:-", this.props)
    }

}