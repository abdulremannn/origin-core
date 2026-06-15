# Origin Core CMS — setup guide

This gives you a Django app ("content") with a model for jobs, testimonials,
and homepage/careers stats — managed through a styled admin dashboard, and
exposed as a small JSON API your existing `index.html` / `careers.html` can
fetch from.

---

## 1. Install packages

In your PyCharm terminal (venv active):

```powershell
pip install django djangorestframework django-cors-headers django-jazzmin
pip freeze > requirements.txt
```

## 2. Create the app

```powershell
python manage.py startapp content
```

Copy `models.py`, `admin.py`, `serializers.py`, `views.py`, `urls.py` from
this folder into the new `content/` folder (overwrite the empty ones it
creates).

## 3. Update your project's `settings.py`

Add to `INSTALLED_APPS` — **jazzmin must be listed before
`django.contrib.admin`**:

```python
INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "corsheaders",
    "content",
]
```

Add the CORS middleware (near the top of `MIDDLEWARE`, before
`CommonMiddleware`):

```python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    # ...rest of your middleware...
]
```

Allow your Vercel site to call the API:

```python
CORS_ALLOWED_ORIGINS = [
    "https://your-site.vercel.app",
    "http://localhost:3000",   # for local testing
]
```

Add the Jazzmin theme (paste anywhere in `settings.py`):

```python
JAZZMIN_SETTINGS = {
    "site_title": "Origin Core Admin",
    "site_header": "Origin Core",
    "site_brand": "Origin Core",
    "welcome_sign": "Manage your jobs, testimonials, and stats",
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": ["content"],
    "icons": {
        "content.JobPosting": "fas fa-briefcase",
        "content.Testimonial": "fas fa-quote-right",
        "content.SiteStat": "fas fa-chart-line",
        "content.SiteSetting": "fas fa-sliders-h",
    },
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "brand_colour": "navbar-dark",
    "accent": "accent-danger",
    "navbar": "navbar-dark",
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}
```

`"darkly"` gives you a dark sidebar + dashboard, which sits much closer to
your site's theme than the default light admin. You can swap `accent` to
`"accent-primary"` if you want it closer to the indigo accent instead of
magenta.

## 4. Wire up the URLs

In your project's main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("content.urls")),
]
```

## 5. Migrate and create an admin user

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` — log in, and you'll see **Job
Postings**, **Testimonials**, **Site Stats**, and **Site Settings** in the
sidebar. Add your real jobs there. The `is_active` and `order` columns are
editable right from the list view.

For **SiteStat**, add rows like:

| page    | value | suffix | label                  |
|---------|-------|--------|------------------------|
| home    | 40    | +      | Agents in production   |
| home    | 15    |        | Industries served      |
| home    | 99.9  | %      | Platform uptime        |
| home    | 24    | /7     | Operations support     |
| careers | 100   | %      | Remote-first           |
| careers | 8     | +      | Countries on the team  |
| careers | 2     | wk     | Avg. time to offer     |

(The "open roles" number on the careers page stays automatic — it's just a
count of active jobs.)

## 6. Check the API

With `runserver` running, visit:

- `http://127.0.0.1:8000/api/jobs/`
- `http://127.0.0.1:8000/api/testimonials/`
- `http://127.0.0.1:8000/api/stats/?page=home`
- `http://127.0.0.1:8000/api/stats/?page=careers`

Each should return JSON once you've added a row in the admin.

---

## 7. Deploying the Django side

Vercel isn't a good fit for Django (no persistent database). The easiest
beginner-friendly option is **PythonAnywhere** (free tier, supports Django +
SQLite, web-based setup, no extra CLI). Alternatives: **Render** or
**Railway** (free/low-cost, support Postgres, deploy from GitHub like
Vercel does).

Whichever you pick, once it's live you'll have a URL like
`https://yourname.pythonanywhere.com`. Update `CORS_ALLOWED_ORIGINS` with
your real Vercel domain, and update `API_BASE` in `careers.html` /
`index.html` (see `frontend_integration.md`) to point at that URL.

If you want, once you've got Django running locally, tell me which host
you'd like and I'll walk through that deploy step by step.
