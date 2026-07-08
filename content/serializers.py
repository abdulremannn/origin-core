from rest_framework import serializers

from .models import JobPosting, ProjectInquiry, SiteStat, Testimonial


class JobPostingSerializer(serializers.ModelSerializer):
    responsibilities = serializers.SerializerMethodField()
    requirements = serializers.SerializerMethodField()
    type = serializers.CharField(source="job_type")

    class Meta:
        model = JobPosting
        fields = [
            "id",
            "title",
            "department",
            "location",
            "type",
            "blurb",
            "responsibilities",
            "requirements",
            "apply_url",
        ]

    def get_responsibilities(self, obj):
        return obj.responsibilities_list()

    def get_requirements(self, obj):
        return obj.requirements_list()


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["quote", "name", "detail"]


class SiteStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteStat
        fields = ["value", "suffix", "label"]


class ProjectInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInquiry
        fields = [
            "id",
            "name",
            "email",
            "company",
            "phone",
            "project_type",
            "industry",
            "timeline",
            "budget_range",
            "summary",
            "business_problem",
            "desired_outcome",
            "current_tools",
            "conversation",
            "source",
            "page_url",
            "created_at",
        ]
        read_only_fields = ["id", "created_at", "source"]

    def validate_email(self, value):
        return value.strip().lower()

    def validate_name(self, value):
        return value.strip()

    def validate_company(self, value):
        return value.strip()

    def validate_phone(self, value):
        return value.strip()

    def validate_project_type(self, value):
        return value.strip()

    def validate_industry(self, value):
        return value.strip()

    def validate_timeline(self, value):
        return value.strip()

    def validate_budget_range(self, value):
        return value.strip()

    def validate_summary(self, value):
        value = value.strip()
        if len(value) < 20:
            raise serializers.ValidationError("Project summary must be at least 20 characters.")
        return value

    def validate_business_problem(self, value):
        return value.strip()

    def validate_desired_outcome(self, value):
        return value.strip()

    def validate_current_tools(self, value):
        return value.strip()

    def validate_conversation(self, value):
        return value.strip()

    def validate_page_url(self, value):
        return value.strip()

    def validate(self, attrs):
        email = attrs.get("email", "").strip()
        phone = attrs.get("phone", "").strip()

        if not email and not phone:
            raise serializers.ValidationError("Please provide at least an email or phone number.")

        return attrs
