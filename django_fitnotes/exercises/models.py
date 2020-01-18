from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return "%s(name=%s)" % (self.__class__.__name__, self.name)


class Exercise(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "exercise"
        verbose_name_plural = "exercises"

    def __str__(self):
        return "%s(name=%s)" % (self.__class__.__name__, self.name)


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    file_id = models.IntegerField()
    date = models.DateField()
    repetitions = models.IntegerField()
    weight = models.FloatField()

    class Meta:
        unique_together = (("date", "file_id"),)

    def __str__(self):
        return "%s(exercise='%s', file_id=%d, date='%s', repetitions=%d, weight=%d)" % (
            self.__class__.__name__,
            self.exercise.name,
            self.file_id,
            self.date.isoformat(),
            self.repetitions,
            self.weight,
        )

