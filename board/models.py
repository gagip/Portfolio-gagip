from django.db import models
from django.utils import timezone
from django.urls import reverse

class Board(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("board:board_detail", kwargs={"pk": self.pk})

    def get_previous(self):
        return self.get_previous_by_pub_date()

    def get_next(self):
        return self.get_next_by_pub_date()


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comments')
    writer = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse("board:detail", kwargs={"pk": self.pk})
    

    