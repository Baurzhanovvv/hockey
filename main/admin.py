from django.contrib import admin
from django import forms
from django.utils.html import format_html

from .models import Player, Teams, Tournament, Competition, Calendar, Match, Stage,Structure,Connect

# admin.site.register(Player)
admin.site.register(Teams)
admin.site.register(Competition)
admin.site.register(Calendar)
admin.site.register(Match)
admin.site.register(Stage)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('img_preview2', 'second_name', 'first_name', 'surname', 'birth_date', 'identificator')
    readonly_fields = ('img_preview',)

    def img_preview2(self, obj):
        return obj.img_preview2

    img_preview2.short_description = 'Фото'
    img_preview2.allow_tags = True

admin.site.register(Player, PlayerAdmin)

admin.site.register(Tournament)
admin.site.register(Structure)
admin.site.register(Connect)
