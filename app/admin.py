from django.contrib import admin

from . import models


class StatsInline(admin.TabularInline):
    model = models.Stat


class PerformancesInline(admin.TabularInline):
    model = models.Performance


@admin.register(models.Channel)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Video)
class PostAdmin(admin.ModelAdmin):
    inlines = [StatsInline, PerformancesInline]


@admin.register(models.Stat)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Performance)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class PostAdmin(admin.ModelAdmin):
    pass
