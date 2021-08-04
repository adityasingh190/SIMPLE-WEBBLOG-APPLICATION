from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin): #customizing admin
	list_display = ["title","updated","timestamp"]
	list_display_links = ["updated"] #it makes field as links which u can select
	list_filter = ["updated","timestamp"] #filter the fields
	search_fields = ["title","content"] #search the fields
	list_editable = ["title"] #we can edit the fields like here title
	class Meta:
		model = Post #adding post model to PostAdmin


admin.site.register(Post, PostModelAdmin)