from django.contrib import admin

from .models import JobPosting, ProjectInquiry, SiteSetting, SiteStat, Testimonial


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "location", "job_type", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("department", "is_active")
    search_fields = ("title", "department", "location")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "department",
                    "location",
                    "job_type",
                    "is_active",
                    "order",
                )
            },
        ),
        (
            "Description",
            {
                "fields": (
                    "blurb",
                    "responsibilities",
                    "requirements",
                    "apply_url",
                )
            },
        ),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "detail", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("quote", "name", "detail")


@admin.register(SiteStat)
class SiteStatAdmin(admin.ModelAdmin):
    list_display = ("page", "value", "suffix", "label", "order")
    list_editable = ("value", "suffix", "label", "order")
    list_filter = ("page",)
    search_fields = ("label", "value")


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("key", "value", "note")
    list_editable = ("value",)
    search_fields = ("key", "value", "note")


@admin.register(ProjectInquiry)
class ProjectInquiryAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "company",
        "name",
        "email",
        "project_type",
        "timeline",
        "budget_range",
        "source",
        "status",
        "has_contact_details",
    )
    list_editable = ("status",)
    list_filter = (
        "status",
        "source",
        "project_type",
        "industry",
        "timeline",
        "budget_range",
        "created_at",
    )
    search_fields = (
        "name",
        "email",
        "company",
        "phone",
        "project_type",
        "industry",
        "summary",
        "business_problem",
        "desired_outcome",
        "current_tools",
        "conversation",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
        "ip_address",
        "user_agent",
        "page_url",
    )
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    fieldsets = (
        (
            "Lead status",
            {
                "fields": (
                    "status",
                    "source",
                    "admin_notes",
                )
            },
        ),
        (
            "Contact details",
            {
                "fields": (
                    "name",
                    "email",
                    "company",
                    "phone",
                )
            },
        ),
        (
            "Project details",
            {
                "fields": (
                    "project_type",
                    "industry",
                    "timeline",
                    "budget_range",
                    "summary",
                    "business_problem",
                    "desired_outcome",
                    "current_tools",
                )
            },
        ),
        (
            "Chatbot conversation",
            {
                "fields": ("conversation",),
            },
        ),
        (
            "Technical metadata",
            {
                "classes": ("collapse",),
                "fields": (
                    "page_url",
                    "ip_address",
                    "user_agent",
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )
