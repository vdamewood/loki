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

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from . import models as m

def Index(request):
    return redirect(reverse('tuli-swcat-project-list'))

def ProjectList(request):
    return render(request,
        "tuli/swcat/project_list.html",
        {
            "projects": m.Project.objects.order_by('name')
        }
    )

def Project(request, project):
    return render(request,
        "tuli/swcat/project.html",
        {
            "project": get_object_or_404(m.Project, slug=project)
        }
    )
