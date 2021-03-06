# Copyright 2019 Vincent Damewood
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import date
from django.db import models

from tuli.models import ContentField

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return format(self.name)


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    created = models.DateField(default=date.today)
    edited = models.DateField(auto_now=True)
    content = ContentField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return format(self.title)
