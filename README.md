# Lab: API Deployment
## Overview
It’s time to deploy!

First steps are to make sure your Application is able to run well in a remote environment.

Once you are confident that your Application is *deployable` then time to research deployment options.

## Feature Tasks and Requirements
### Use API Quick Start Template
- Create a new public repo cookie-stand-api that uses API Quick Start as a template.
- Modify your application using instructions in README.md found in root of repo.
  - Install from requirements.txt.
  - Add black and flake8 dependencies.
  - Export (aka freeze) requirements.
  - Change things app folder to be cookie_stands
  - Go through code base looking for Thing,thing and things change to cookie-stand related names.
  - E.g. Thing model becomes CookieStand
  - E.g. ThingList becomes CookieStandList
- Pro Tip: Do a global text search looking for thing
  - Search should be case insensitive.
  - WARNING: Do NOT just cut and paste. Think through each change.
- Create/rename .env using .env.sample as starting point.
  - Here’s a handy way to generate a secret key
    - ```python -c “import secrets; print(secrets.token_urlsafe())”```

### Deeper CookieStand Changes
The `CookieStand` model must contain:
```
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(blank=True)
    hourly_sales = models.JSONField(default=list, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)
```

- Notice the use of JSONField which is a newer feature introduced in Django 3.1.
- Update str method to return the stand’s location.
- Once changes are complete make migrations, migrate, and test locally.
### Database Deployment Requirements
- Host your Database at ElephantSQL
### Site Deployment Requirements
- Deploy Docker container to Heroku

### Implementation Notes
- Site must use environment variables.
### Useful Terminal Commands
- docker compose up --build
- docker compose down
- docker compose restart
- docker compose run web python manage.py migrate
- docker compose run web python manage.py collectstatic
### User Acceptance Tests
- Add Unit Tests to cookie_stands/tests.py
- Manually confirm API using API Tester, Postman or HTTPie.
  - Remember to use deployed url, not localhost
