# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-28 17:57
from __future__ import unicode_literals

import core.models.xosbase_header
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0012_backupoperation_decl_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text=b'Time this model was created')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, help_text=b'Time this model was changed by a non-synchronizer')),
                ('enacted', models.DateTimeField(blank=True, default=None, help_text=b'When synced, set to the timestamp of the data that was synced', null=True)),
                ('policed', models.DateTimeField(blank=True, default=None, help_text=b'When policed, set to the timestamp of the data that was policed', null=True)),
                ('backend_register', models.CharField(blank=True, default=b'{}', max_length=1024, null=True)),
                ('backend_need_delete', models.BooleanField(default=False)),
                ('backend_need_reap', models.BooleanField(default=False)),
                ('backend_status', models.CharField(default=b'Provisioning in progress', max_length=1024)),
                ('backend_code', models.IntegerField(default=0)),
                ('deleted', models.BooleanField(default=False)),
                ('write_protect', models.BooleanField(default=False)),
                ('lazy_blocked', models.BooleanField(default=False)),
                ('no_sync', models.BooleanField(default=False)),
                ('no_policy', models.BooleanField(default=False)),
                ('policy_status', models.CharField(blank=True, default=b'Policy in process', max_length=1024, null=True)),
                ('policy_code', models.IntegerField(blank=True, default=0, null=True)),
                ('leaf_model_name', models.CharField(help_text=b'The most specialized model in this chain of inheritance, often defined by a service developer', max_length=1024)),
                ('backend_need_delete_policy', models.BooleanField(default=False, help_text=b'True if delete model_policy must be run before object can be reaped')),
                ('xos_managed', models.BooleanField(default=True, help_text=b'True if xos is responsible for creating/deleting this object')),
                ('backend_handle', models.CharField(blank=True, help_text=b'Handle used by the backend to track this object', max_length=1024, null=True)),
                ('changed_by_step', models.DateTimeField(blank=True, default=None, help_text=b'Time this model was changed by a sync step', null=True)),
                ('changed_by_policy', models.DateTimeField(blank=True, default=None, help_text=b'Time this model was changed by a model policy', null=True)),
                ('name', models.CharField(help_text=b'Name for this color', max_length=256)),
                ('html_code', models.CharField(help_text=b'HTML Code for this color', max_length=256)),
            ],
            options={
                'verbose_name': 'Color',
            },
            bases=(models.Model, core.models.xosbase_header.PlModelMixIn),
        ),
        migrations.CreateModel(
            name='EmbeddedImageNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text=b'Time this model was created')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, help_text=b'Time this model was changed by a non-synchronizer')),
                ('enacted', models.DateTimeField(blank=True, default=None, help_text=b'When synced, set to the timestamp of the data that was synced', null=True)),
                ('policed', models.DateTimeField(blank=True, default=None, help_text=b'When policed, set to the timestamp of the data that was policed', null=True)),
                ('backend_register', models.CharField(blank=True, default=b'{}', max_length=1024, null=True)),
                ('backend_need_delete', models.BooleanField(default=False)),
                ('backend_need_reap', models.BooleanField(default=False)),
                ('backend_status', models.CharField(default=b'Provisioning in progress', max_length=1024)),
                ('backend_code', models.IntegerField(default=0)),
                ('deleted', models.BooleanField(default=False)),
                ('write_protect', models.BooleanField(default=False)),
                ('lazy_blocked', models.BooleanField(default=False)),
                ('no_sync', models.BooleanField(default=False)),
                ('no_policy', models.BooleanField(default=False)),
                ('policy_status', models.CharField(blank=True, default=b'Policy in process', max_length=1024, null=True)),
                ('policy_code', models.IntegerField(blank=True, default=0, null=True)),
                ('leaf_model_name', models.CharField(help_text=b'The most specialized model in this chain of inheritance, often defined by a service developer', max_length=1024)),
                ('backend_need_delete_policy', models.BooleanField(default=False, help_text=b'True if delete model_policy must be run before object can be reaped')),
                ('xos_managed', models.BooleanField(default=True, help_text=b'True if xos is responsible for creating/deleting this object')),
                ('backend_handle', models.CharField(blank=True, help_text=b'Handle used by the backend to track this object', max_length=1024, null=True)),
                ('changed_by_step', models.DateTimeField(blank=True, default=None, help_text=b'Time this model was changed by a sync step', null=True)),
                ('changed_by_policy', models.DateTimeField(blank=True, default=None, help_text=b'Time this model was changed by a model policy', null=True)),
                ('name', models.CharField(help_text=b'Name for this image', max_length=256)),
                ('url', models.CharField(help_text=b'URL for this image', max_length=256)),
            ],
            options={
                'verbose_name': 'Embedded Image',
            },
            bases=(models.Model, core.models.xosbase_header.PlModelMixIn),
        ),
        migrations.CreateModel(
            name='ServiceInstanceWithCompute2',
            fields=[
                ('serviceinstance_decl_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.ServiceInstance_decl')),
            ],
            options={
                'verbose_name': 'ServiceInstanceWithCompute2',
            },
            bases=('core.serviceinstance',),
        ),
        migrations.CreateModel(
            name='SimpleExampleService',
            fields=[
                ('service_decl_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Service_decl')),
                ('service_message', models.CharField(help_text=b'Service Message to display in web page', max_length=256)),
                ('service_secret', models.TextField(blank=True, help_text=b'Service Secret to place in a file', null=True)),
            ],
            options={
                'verbose_name': 'Simple Example Service',
            },
            bases=('core.service',),
        ),
        migrations.CreateModel(
            name='SimpleExampleServiceInstance',
            fields=[
                ('serviceinstancewithcompute2_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='simpleexampleservice.ServiceInstanceWithCompute2')),
                ('tenant_message', models.CharField(help_text=b'Tenant Message to Display', max_length=256)),
                ('tenant_image', models.CharField(help_text=b'Tenant image in web page', max_length=256)),
                ('tenant_secret', models.TextField(blank=True, help_text=b'Tenant Secret to place in a file', null=True)),
                ('background_color', models.ForeignKey(blank=True, help_text=b'Background color to use in web page', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serviceinstance_background_colors', to='simpleexampleservice.ColorNew')),
                ('foreground_color', models.ForeignKey(blank=True, help_text=b'Foreground color to use in web page', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serviceinstance_foreground_colors', to='simpleexampleservice.ColorNew')),
            ],
            options={
                'verbose_name': 'Example Service Instance',
            },
            bases=('simpleexampleservice.serviceinstancewithcompute2',),
        ),
        migrations.AddField(
            model_name='serviceinstancewithcompute2',
            name='compute_instance',
            field=models.ForeignKey(blank=True, help_text=b'ComputeServiceInstance that holds compute resources for this ServiceInstance', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_instance_with_computes', to='core.ComputeServiceInstance'),
        ),
        migrations.AddField(
            model_name='embeddedimagenew',
            name='serviceinstance',
            field=models.ForeignKey(blank=True, help_text=b'ServiceInstance that represents the web page where this embedded image should be placed', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='embedded_images', to='simpleexampleservice.SimpleExampleServiceInstance'),
        ),
    ]
