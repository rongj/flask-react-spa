webpackJsonp([7],{795:function(e,t,n){"use strict";function a(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function o(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!==typeof t&&"function"!==typeof t?e:t}function r(e,t){if("function"!==typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0}),n.d(t,"default",function(){return E});var l,i,c=(n(348),n(349)),u=(n(350),n(351)),s=(n(273),n(274)),d=(n(305),n(306)),m=(n(100),n(99)),f=(n(352),n(353)),p=(n(295),n(296)),h=n(0),b=n.n(h),g=n(43),y=n(298),v=function(){function e(e,t){for(var n=0;n<t.length;n++){var a=t[n];a.enumerable=a.enumerable||!1,a.configurable=!0,"value"in a&&(a.writable=!0),Object.defineProperty(e,a.key,a)}}return function(t,n,a){return n&&e(t.prototype,n),a&&e(t,a),t}}(),E=(l=Object(g.b)(function(e){return{inStore:e.categoryStore}}))(i=Object(g.c)(i=function(e){function t(){var e,n,r,l;a(this,t);for(var i=arguments.length,c=Array(i),u=0;u<i;u++)c[u]=arguments[u];return n=r=o(this,(e=t.__proto__||Object.getPrototypeOf(t)).call.apply(e,[this].concat(c))),r.state={showModal:!1,modalType:"create"},r.onModelToggle=function(e,t){var n=r.props.inStore;r.setState({showModal:!0,modalType:e}),n.formData="update"===e?t:{status:!0}},r.onFormChange=function(e,t){r.props.inStore.formData[e]=t},r.onModelChange=function(e){if("ok"===e){var t=r.props.inStore,n=r.state.modalType;t.putItem(n).then(function(e){e&&r.setState({showModal:!1})})}else r.setState({showModal:!1})},l=n,o(r,l)}return r(t,e),v(t,[{key:"componentDidMount",value:function(){this.props.inStore.getData()}},{key:"render",value:function(){var e=this,t=this.props.inStore,n=t.listData,a=t.listLoading,o=t.formData,r=t.submitLoding,l=t.deleteItem,i=this.state,g=i.showModal,v=i.modalType,E=[{title:"id",dataIndex:"id"},{title:"\u5206\u7c7b",dataIndex:"name"},{title:"\u6587\u7ae0\u6570",dataIndex:"article_num"},{title:"\u5206\u7c7b\u72b6\u6001",dataIndex:"status",render:function(e){return e?"\u542f\u7528":"\u7981\u7528"}},{title:"\u64cd\u4f5c",dataIndex:"action",render:function(t,n){return b.a.createElement("span",null,b.a.createElement("a",{onClick:e.onModelToggle.bind(null,"update",n)},"\u7f16\u8f91"),b.a.createElement(p.a,{type:"vertical"}),b.a.createElement(f.a,{title:"\u786e\u5b9a\u5220\u9664\u8fd9\u6761\u5206\u7c7b?",onConfirm:function(){return l(n.id)}},b.a.createElement("a",null,"\u5220\u9664")))}}];return b.a.createElement(h.Fragment,null,b.a.createElement("div",{className:"mb10"},b.a.createElement(m.a,{type:"primary",onClick:this.onModelToggle.bind(null,"create")},"\u65b0\u589e\u5206\u7c7b")),b.a.createElement(y.a,{loading:a,columns:E,dataSource:n}),b.a.createElement(c.a,{visible:g,title:"update"===v?"\u7f16\u8f91\u5206\u7c7b":"\u65b0\u589e\u5206\u7c7b",centered:!0,confirmLoading:r,onOk:this.onModelChange.bind(null,"ok"),onCancel:this.onModelChange.bind(null,"cancel")},b.a.createElement(s.a,{className:"form-flex"},b.a.createElement(s.a.Item,{label:"\u5206\u7c7b\u540d\u79f0",required:!0},b.a.createElement(d.a,{value:o.name,onChange:function(t){return e.onFormChange("name",t.target.value)},placeholder:"\u8f93\u5165\u5206\u7c7b\u540d"})),b.a.createElement(s.a.Item,{label:"\u5206\u7c7b\u72b6\u6001"},b.a.createElement(u.a,{checkedChildren:"ON",unCheckedChildren:"OFF",checked:o.status,onChange:function(t){return e.onFormChange("status",t)}})),b.a.createElement(s.a.Item,{label:"\u5206\u7c7b\u6392\u5e8f"},b.a.createElement(d.a,{value:o.order_num,onChange:function(t){return e.onFormChange("order_num",t.target.value)},type:"number"})))))}}]),t}(h.Component))||i)||i}});