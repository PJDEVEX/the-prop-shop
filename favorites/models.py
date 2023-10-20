from django.db import models
from accounts.models import Account
from listings.models import Listing


class Favorite(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("owner", "listing")

    def __str__(self):
        return f"{self.user} {self.listing}"
