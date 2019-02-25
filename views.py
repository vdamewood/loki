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

from django.shortcuts import get_object_or_404, render
from .models import Post, Tag

def show_index(request):
    posts = Post.objects.order_by('created')
    tags = Tag.objects.order_by('name')
    return render(request, 'loki/index.html', {
        'posts': posts,
        'tags': tags,
    })

def show_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "loki/post.html", {"post": post})

def show_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = None
    return render(request, "loki/tag.html", {
        'tag': tag,
        'posts': posts,
    })