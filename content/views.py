from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import JobPosting, Testimonial, SiteStat, SiteSetting
from .serializers import JobPostingSerializer, TestimonialSerializer, SiteStatSerializer


@api_view(["GET"])
def jobs_list(request):
    jobs = JobPosting.objects.filter(is_active=True)
    return Response(JobPostingSerializer(jobs, many=True).data)


@api_view(["GET"])
def testimonials_list(request):
    items = Testimonial.objects.filter(is_active=True)
    return Response(TestimonialSerializer(items, many=True).data)


@api_view(["GET"])
def stats_list(request):
    page = request.GET.get("page", "home")
    items = SiteStat.objects.filter(page=page)
    return Response(SiteStatSerializer(items, many=True).data)


@api_view(["GET"])
def settings_dict(request):
    items = SiteSetting.objects.all()
    return Response({s.key: s.value for s in items})
