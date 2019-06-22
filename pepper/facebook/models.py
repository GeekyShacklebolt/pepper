# Third party stuff
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class FacebookPage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Facebook Page Owner'))
    page_name = models.TextField(verbose_name=_('Facebook Page Name'), null=False, blank=False)
    access_token = models.TextField(verbose_name=_('Facebook Page Access Token'), null=False, blank=False)
    page_id = models.TextField(verbose_name=_('Facebook Page ID'), null=False, blank=False)

    class Meta:
        verbose_name = _('Facebook Page')
        verbose_name_plural = _('Facebook Pages')
        db_table = "facebookpages"

    def __str__(self):
        return self.page_name


class MessengerLabel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Messenger Label Owner'))
    page = models.ForeignKey(FacebookPage, on_delete=models.CASCADE, verbose_name=_('Facebook Page'))
    label_name = models.TextField(verbose_name=_('Messenger Label Name'), null=False, blank=False)
    label_id = models.TextField(verbose_name=_('Messenger Label Id'), null=False, blank=False)

    class Meta:
        verbose_name = _('Messenger Label')
        verbose_name_plural = _('Messenger Labels')
        db_table = "messengerlabels"

    def __str__(self):
        return self.label_name


class PSIDList(models.Model):
    page = models.ForeignKey(FacebookPage, on_delete=models.CASCADE, verbose_name=_('Facebook Page'))
    label = models.ForeignKey(MessengerLabel, on_delete=models.CASCADE, verbose_name=_('Messenger Label'))
    psid_list = models.TextField(verbose_name=_('PSID List'), null=False, blank=False)
    valid_psid = models.TextField(verbose_name=_('Valid PSID List'), null=True, blank=True, default=None)
    invalid_psid = models.TextField(verbose_name=_('Invalid PSID List'), null=True, blank=True, default=None)
    label_associated_to = models.TextField(verbose_name=_('Label Associated To'), null=True, blank=True, default=None)

    class Meta:
        verbose_name = _('PSID List')
        verbose_name_plural = _('PSID Lists')
        db_table = "psidlists"
