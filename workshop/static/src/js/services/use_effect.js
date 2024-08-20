/* @odoo-module */
const {Component, useState} = owl


import {registry} from "@web/core/registry";

export class UseEffect extends Component {
    static template = 'workshop.Counter'

    setup(){


   this.state = useState({
       age: 0,
       data: data = [
               { id: 1, name: 'John Doe', age: 25 },
               { id: 2, name: 'Jane Smith', age: 17 },
               { id: 3, name: 'Alice Johnson', age: 30 },
               { id: 4, name: 'Bob Brown', age: 16 },
               { id: 5, name: 'Charlie Davis', age: 22 },
             ]
   })


//   useEffect(()=> {
//       this.FilterData()
//   }, ()=>[this.state.age,])
}






//FilterData(){
//   return this.state.data.filter(user => user.age <= this.state.age);
//}


//registry.category('actions').add('use_effect', UseEffect);