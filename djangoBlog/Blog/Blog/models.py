import time

from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class BlogModel(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(max_length=15000, null=False, blank=False)
    posted = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=50, null=False, blank=False)
    main_pic = models.ImageField(
        upload_to=f"blogArticles/{time.strftime('%Y-%m-%d')}",
        null=True, blank=True
    )
    tag_one = models.CharField(max_length=20, default='',
                               blank=True, null=True
                               )
    tag_two = models.CharField(max_length=20, default='',
                               blank=True, null=True
                               )
    tag_three = models.CharField(max_length=20, default='',
                                 blank=True, null=True
                                 )

    second_header = models.CharField(max_length=100, null=True, blank=True)
    second_paragraph = models.TextField(max_length=15000, null=True, blank=True)

    def __str__(self) -> str:
        return f'Blog id: ' \
               f'{self.id}, posted: {self.posted} {self.title[:20]}..'

    @property
    def when_posted(self) -> str:

        if not self.author:

            user_name = self.owner.author if self.owner.first_name else ''
            last_name = self.owner.last_name if self.owner.last_name else ''

            owner = f'{user_name} {last_name}' \
                if user_name and last_name else 'Unknown'

        else:

            owner = f'{self.author}'

        return f'Posted on {self.posted.strftime("%B")} ' \
               f'{self.posted.day}, {self.posted.year} by {owner}'

    @property
    def return_tags(self) -> list:
        listed = []
        if self.tag_one:
            listed.append(self.tag_one)
        if self.tag_two:
            listed.append(self.tag_two)
        if self.tag_three:
            listed.append(self.tag_three)

        return listed

    class Meta:
        ordering = ['-posted']
