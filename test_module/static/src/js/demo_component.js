
/* @odoo-module */

export class DemoComponent extends owl.Component {

  static template = "test_module.demo"
  static props = ['test','test2']



setup(){
console.log(this.props)
}


}


