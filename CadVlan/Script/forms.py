# -*- coding:utf-8 -*-

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from django import forms
from CadVlan.messages import error_messages


class ScriptForm(forms.Form):

    def __init__(self, forms_aux, *args, **kwargs):
        super(ScriptForm, self).__init__(*args, **kwargs)

        self.fields['script_type'].choices = [(st['id'], st['tipo'] + " - " + st['descricao'])
                                              for st in forms_aux["tipo_roteiro"]["script_type"]]
        self.fields['model'].choices = ([(m['id'], m['nome']) for m in forms_aux["modelos"]])

    name = forms.CharField(label=u'Nome do Roteiro', min_length=3, max_length=40, required=True,
                           error_messages=error_messages, widget=forms.TextInput(attrs={'style': "width: 300px"}))
    script_type = forms.ChoiceField(label=u'Tipo de Roteiro', choices=[(0, 'Selecione')], required=True,
                                    error_messages=error_messages, widget=forms.Select(attrs={'style': "width: 310px"}))
    model = forms.MultipleChoiceField(label=u'Modelos', required=True, error_messages=error_messages,
                                       widget=forms.SelectMultiple(attrs={'style': "width: 250px"}))
    description = forms.CharField(label=u'Descrição', min_length=3, max_length=100, required=True,
                                  error_messages=error_messages, widget=forms.Textarea(
                                  attrs={'style': "width: 500px", 'rows': 3, 'data-maxlenght': 100}))