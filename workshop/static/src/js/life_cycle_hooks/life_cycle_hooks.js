/* @odoo-module */
const {  Component,
useComponent,
    useState,
    onWillStart,
    onMounted,
    onWillUnmount,
    onWillUpdateProps,
    onPatched,
    onWillPatch,
    onWillRender,
    onRendered,
    onWillDestroy,
    xml,} = owl


import {registry} from "@web/core/registry";


function useLogLifecycle(){
    const component = useComponent();
    const name = component.constructor.name;
    onWillStart(() => console.log(`${name}:willStart`));
    onMounted(() => console.log(`${name}:mounted`));
    onWillUpdateProps((nextProps) => console.log(`${name}:willUpdateProps:- `, nextProps));
    onWillRender(() => console.log(`${name}:willRender`));
    onRendered(() => console.log(`${name}:rendered`));
    onWillPatch(() => console.log(`${name}:willPatch`));
    onPatched(() => console.log(`${name}:patched`));
    onWillUnmount(() => console.log(`${name}:willUnmount`));
    onWillDestroy(() => console.log(`${name}:willDestroy`));
}


export class DemoSubComponent extends Component {
    static template = xml`<div class="container text-center">
        <h3>Props:--> <t t-esc="props.counter"/></h3>
    </div>`;

    setup() {
        useLogLifecycle();
    }
}


export class LifeCycleHooks extends Component {
    static template = 'workshop.LifeCycleHooks'
    static components = { DemoSubComponent };

    setup(){
//        const component = useComponent();
//        const name = component.constructor.name;
//        onWillStart(() => console.log(`${name}:willStart`));
//        onMounted(() => console.log(`${name}:mounted`));
//        onWillUpdateProps(() => console.log(`${name}:willUpdateProps`));
//        onWillRender(() => console.log(`${name}:willRender`));
//        onRendered(() => console.log(`${name}:rendered`));
//        onWillPatch(() => console.log(`${name}:willPatch`));
//        onPatched(() => console.log(`${name}:patched`));
//        onWillUnmount(() => console.log(`${name}:willUnmount`));
//        onWillDestroy(() => console.log(`${name}:willDestroy`));

        useLogLifecycle()
        this.state = useState({ n: 0 });
    }

    toggleSubComponent() {
        this.state.flag = !this.state.flag;
    }

}


registry.category('actions').add('life_cycle_hooks', LifeCycleHooks);