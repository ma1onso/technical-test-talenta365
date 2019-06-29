from django.db import models


class Region(models.Model):
    code = models.PositiveIntegerField(

    )
    name = models.CharField(
        max_length=100,
    )
    municipalities = models.ManyToManyField(
        'places.Municipality', blank=True,
    )

    def __str__(self):
        return '{0}'.format(self.name)


class Municipality(models.Model):
    code = models.PositiveIntegerField(

    )
    name = models.CharField(
        max_length=100,
    )
    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name_plural = 'municipalities'

    def __str__(self):
        return '{0}'.format(self.name)

    def save(self, *args, **kwargs):
        super(Municipality, self).save(*args, **kwargs)

        if self.is_active is False:
            regions = Region.objects.filter(municipalities=self.pk)

            for region in regions:
                region.municipalities.remove(self.pk)
