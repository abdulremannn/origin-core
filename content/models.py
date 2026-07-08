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
    apply_url = models.URLField(
        max_length=300,
        blank=True,
        help_text="Tally or other application form URL for this role.",
    )

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Job Posting"
        verbose_name_plural = "Job Postings"

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
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.name} — {self.detail}" if self.detail else self.name


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
        verbose_name = "Site Stat"
        verbose_name_plural = "Site Stats"

    def __str__(self):
        return f"{self.value}{self.suffix} — {self.label}"


class SiteSetting(models.Model):
    """Simple key/value store for small editable website text."""

    key = models.SlugField(max_length=100, unique=True)
    value = models.CharField(max_length=300)
    note = models.CharField(max_length=200, blank=True, help_text="Reminder of where this is used.")

    class Meta:
        ordering = ["key"]
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.key


class ProjectInquiry(models.Model):
    STATUS_NEW = "new"
    STATUS_REVIEWED = "reviewed"
    STATUS_CONTACTED = "contacted"
    STATUS_QUALIFIED = "qualified"
    STATUS_CLOSED = "closed"

    STATUS_CHOICES = [
        (STATUS_NEW, "New"),
        (STATUS_REVIEWED, "Reviewed"),
        (STATUS_CONTACTED, "Contacted"),
        (STATUS_QUALIFIED, "Qualified"),
        (STATUS_CLOSED, "Closed"),
    ]

    SOURCE_CHATBOT = "chatbot"
    SOURCE_CONTACT_FORM = "contact_form"
    SOURCE_MANUAL = "manual"

    SOURCE_CHOICES = [
        (SOURCE_CHATBOT, "Chatbot"),
        (SOURCE_CONTACT_FORM, "Contact Form"),
        (SOURCE_MANUAL, "Manual"),
    ]

    name = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)
    company = models.CharField(max_length=160, blank=True)
    phone = models.CharField(max_length=60, blank=True)

    project_type = models.CharField(
        max_length=160,
        blank=True,
        help_text="e.g. AI agent, enterprise platform, workflow automation, integration.",
    )
    industry = models.CharField(max_length=160, blank=True)
    timeline = models.CharField(max_length=120, blank=True)
    budget_range = models.CharField(max_length=120, blank=True)

    summary = models.TextField(help_text="AI-generated or user-submitted project summary.")
    business_problem = models.TextField(blank=True)
    desired_outcome = models.TextField(blank=True)
    current_tools = models.TextField(blank=True, help_text="Current software, systems, APIs, databases, or workflows.")
    conversation = models.TextField(blank=True, help_text="Full chatbot conversation/context submitted by the user.")

    source = models.CharField(max_length=30, choices=SOURCE_CHOICES, default=SOURCE_CHATBOT)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=STATUS_NEW)
    admin_notes = models.TextField(blank=True)

    user_agent = models.TextField(blank=True)
    page_url = models.URLField(max_length=500, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Project Inquiry"
        verbose_name_plural = "Project Inquiries"

    def __str__(self):
        label = self.company or self.name or self.email or "New project inquiry"
        return f"{label} — {self.get_status_display()}"

    @property
    def has_contact_details(self):
        return bool(self.email or self.phone)
