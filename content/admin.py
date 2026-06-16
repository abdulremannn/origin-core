from django.contrib import admin
from .models import JobPosting, Testimonial, SiteStat, SiteSetting


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "location", "job_type", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("department", "is_active")
    search_fields = ("title",)
    fieldsets = (
        (None, {
            "fields": ("title", "department", "location", "job_type", "is_active", "order")
        }),
        ("Description", {
            "fields": ("blurb", "responsibilities", "requirements", "apply_url")
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "detail", "is_active", "order")
    list_editable = ("is_active", "order")


@admin.register(SiteStat)
class SiteStatAdmin(admin.ModelAdmin):
    list_display = ("page", "value", "suffix", "label", "order")
    list_editable = ("value", "suffix", "label", "order")
    list_filter = ("page",)


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("key", "value", "note")
    list_editable = ("value",)
