from rest_framework import serializers
from .models import JobPosting, Testimonial, SiteStat


class JobPostingSerializer(serializers.ModelSerializer):
    responsibilities = serializers.SerializerMethodField()
    requirements = serializers.SerializerMethodField()
    type = serializers.CharField(source="job_type")

    class Meta:
        model = JobPosting
        fields = [
            "id", "title", "department", "location", "type",
            "blurb", "responsibilities", "requirements", "apply_url",
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
