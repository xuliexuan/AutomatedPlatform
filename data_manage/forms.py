#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django  import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit, HTML, MultiField, Div
from crispy_forms.bootstrap import FormActions
from .fields import RestrictedFileField

DATE_FORMAT = '%m/%d/%Y'
TIME_FORMAT = '%I:%M %p'

class GlucoseImportForm(forms.Form):
    # File size limited to 2MB
    file = RestrictedFileField(
        label='CSV File (Max Size 2MB)',
        content_types=[
            'application/binary',
            'application/csv',
            'application/octet-stream',
            'application/vnd.ms-excel',
            'text/csv',
            'text/plain',
        ],
        max_upload_size=2097152,
    )

    def __init__(self, *args, **kwargs):
        super(GlucoseImportForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self. helper.layout = Layout(
            MultiField(
                None,
                HTML(
                    '''
                    {% if messages %}
                    {% for message in messages %}
                    <p {% if message.tags %}
                    class="alert alert-{{ message.tags }}"
                    {% endif %}>{{ message }}</p>{% endfor %}{% endif %}
                    '''
                ),
                Div(
                    'file',
                    FormActions(
                        Submit('submit', 'Import'),
                        css_class='pull-right',
                    ),
                    css_class='well col-xs-10 col-sm-8 col-md-8',
                ),
            ),
        )