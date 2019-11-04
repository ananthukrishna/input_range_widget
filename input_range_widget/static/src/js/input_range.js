odoo.define('input_range.input_range', function (require) {
    'use strict';
    
    var field_registry = require('web.field_registry');    
    var FieldInteger = field_registry.get('integer');

    var core = require('web.core');
    var QWeb = core.qweb;

    
    var InputRange = FieldInteger.extend({ 
        events: {
            'mousemove #myRange': '_onMoveProgress',
            'click #myRange': '_onMoveProgress',
        },
        template: 'InputRange',   

        init: function (options) {
            this._super.apply(this, arguments);
            var self = this; 
            if (this.nodeOptions['min']){ 
                this.min = this.nodeOptions['min'];
            }
            else{
                this.min = 0;
            }
            if (this.nodeOptions['max']) {
                this.max = this.nodeOptions['max'];
            }  
            else{
                this.max = 100;
            }                                 
            $('#rangeValue').text(this.value);
        },
        start: function() {                                 
            return this._super();  
        },
        _getValue: function () {
            var $input = this.$el.find('input');            
            return $input.val();
        },
        _renderEdit: function () {
            var self= this; 
            if (this.value != null && this.value >= 0){
                $('#rangeValue').text(this.value);             
            }            
        },
        _onMoveProgress: function(){   
            var self = this;  
            $('#rangeValue').text($('#myRange').val());
            this._setValue($('#myRange').val());
        },    
        

    })
    field_registry.add('input_range', InputRange);
    return InputRange;
});