from django.db import models
from django.core import validators


class Item(models.Model):

    SEX_CHOICES = (
        (1, '業務'),
        (2, '業務以外'),
    )

    name = models.CharField(
        verbose_name='TODO名',
        max_length=200,
    )
    age = models.IntegerField(
        verbose_name='期限月',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    sex = models.IntegerField(
        verbose_name='TODO区分',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='内容',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'