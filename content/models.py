from django.db import models


class JobPosting(models.Model):
    DEPARTMENT_CHOICES = [
        ("Engineering", "Engineering"),
        ("Design", "Design"),
        ("Product", "Product"),
        ("Sales", "Sales & Ops"),
    ]

    title = models.CharField(max_length=200)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    location = models.CharField(max_length=100, default="Remote")
    job_type = models.CharField(max_length=50, default="Full-time")
    blurb = models.TextField(help_text="One-line summary shown on the role card.")
    responsibilities = models.TextField(help_text="One item per line.")
    requirements = models.TextField(help_text="One item per line.")
    is_active = models.BooleanField(default=True, help_text="Untick to hide from the careers page.")
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first.")
    created_at = models.DateTimeField(auto_now_add=True)
    apply_url = models.URLField(max_length=300, blank=True, help_text="Tally or other application form URL for this role.")

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title

    def responsibilities_list(self):
        return [line.strip() for line in self.responsibilities.splitlines() if line.strip()]

    def requirements_list(self):
        return [line.strip() for line in self.requirements.splitlines() if line.strip()]


class Testimonial(models.Model):
    quote = models.TextField()
    name = models.CharField(max_length=100, help_text='e.g. "Director of Operations"')
    detail = models.CharField(max_length=100, blank=True, help_text='e.g. "Logistics & freight"')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} — {self.detail}"


class SiteStat(models.Model):
    PAGE_CHOICES = [
        ("home", "Homepage"),
        ("careers", "Careers page"),
    ]

    page = models.CharField(max_length=20, choices=PAGE_CHOICES, default="home")
    value = models.CharField(max_length=20, help_text='e.g. "40", "99.9", "24"')
    suffix = models.CharField(max_length=10, blank=True, help_text='e.g. "+", "%", "/7"')
    label = models.CharField(max_length=100, help_text='e.g. "Agents in production"')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["page", "order"]

    def __str__(self):
        return f"{self.value}{self.suffix} — {self.label}"


class SiteSetting(models.Model):
    """Simple key/value store for small bits of editable text
    (contact email, availability line, response time, etc.)"""

    key = models.SlugField(max_length=100, unique=True)
    value = models.CharField(max_length=300)
    note = models.CharField(max_length=200, blank=True, help_text="Reminder of where this is used.")

    class Meta:
        ordering = ["key"]

    def __str__(self):
        return self.key
