#
#
#


from django.db import models
from django.contrib.auth.models import User


class LibraryModel(models.Model):
    """A single JS library"""

    name = models.CharField(max_length=1023, db_index=True)
    version = models.CharField(max_length=127)
    supported_browsers = models.ManyToManyField("BrowserModel", related_name="libraries", null=True, blank=True)
    supported_platforms = models.ManyToManyField("PlatformModel", related_name="libraries", null=True, blank=True)
    summary = models.CharField(max_length=2047)
    description = models.TextField(blank=True)
    keywords = models.ManyToManyField("KeywordModel", related_name="libraries", null=True, blank=True)
    homepage = models.CharField(max_length=2047, blank=True)
    download_url = models.ManyToManyField("URLModel", related_name="download_libraries")
    author = models.CharField(max_length=1023, blank=True)
    author_email = models.CharField(max_length=2047, blank=True)
    maintainer = models.CharField(max_length=1023, blank=True)
    maintainer_email = models.CharField(max_length=2047, blank=True)
    licenses = models.ManyToManyField("LicenseModel", related_name="libraries", null=True, blank=True)
    requires = models.ManyToManyField("LibraryModel", related_name="required_by", null=True, blank=True, symmetrical=False)
    recommends = models.ManyToManyField("LibraryModel", related_name="recommended_by", null=True, blank=True, symmetrical=False)
    obsoletes = models.ManyToManyField("LibraryModel", related_name="obsoleted_by", null=True, blank=True, symmetrical=False)
    project_url = models.ManyToManyField("URLModel", related_name="project_libraries")

    internal_owners = models.ManyToManyField(User, related_name="libraries")

    class Meta:
        unique_together = ("name", "version")


class BrowserModel(models.Model):
    """A browser"""

    id = models.CharField("browser ID", max_length=127, primary_key=True)
    full_name = models.CharField("full name", max_length=1023)


class PlatformModel(models.Model):
    """A JS engine"""

    id = models.CharField("engine ID", max_length=127, primary_key=True)
    full_name = models.CharField("full name", max_length=1023)


class KeywordModel(models.Model):
    """A keyword or tag"""

    name = models.CharField(max_length=1023, primary_key=True)
    description = models.TextField(blank=True)


class URLModel(models.Model):
    """An URL"""

    url = models.CharField(max_length=2047)
    type = models.TextField(max_length=127)

    class Meta:
        unique_together = ("url", "type")


class LicenseModel(models.Model):
    """A license of a library"""

    id = models.CharField("license", max_length=1023, primary_key=True)
    full_name = models.CharField("full name", max_length=1023, blank=True)
    url = models.CharField("URL", max_length=2047, blank=True)

