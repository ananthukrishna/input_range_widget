
# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#
#    Copyright (c) All rights reserved:
#        (c) 2015  TM_FULLNAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
###############################################################################
{
    'name': 'Input Range Widget',
    'summary': 'Display range input sliders for number selection in form view',
    'version': '1.0',
    'description': """
        Web Slider Widget
        =================
        Add slider to int fields.
        
        Usage
        --------------
        widget="input_range" in Form View

        Options
        --------------
        * min: The minimum acceptable value for the slider. 0 by default
        * max: The maximum acceptable value for the slider. 100 by default

        Examples
        --------------

        <group>
            <field name="fieldname" widget="input_range" options="{'min':0,'max':100}"/>
        </group>
            
    """,
    'author': 'Ananthu Krishna',
    'maintainer': 'Ananthu Krishna',
    'website': 'http://codersfort.com',
    'license': 'AGPL-3',
    'category': 'hr',
    "images": ["images/input_range.png"],
    'depends': ['base','hr','web'],
    'data': [
        # 'views/hr_employee_view.xml',
        'views/assets.xml'
    ],
    'qweb': ['static/src/xml/input_range.xml'],
    'installable': True,
    'application': True,    
}