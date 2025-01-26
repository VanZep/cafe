from django.db import models
from django.core.validators import MinValueValidator

from .constants import (
    MIN_NUM_TABLE, MIN_TOTAL_PRICE, CHARFIELD_MAX_LENGTH, STATUSES
)


class Item(models.Model):
    """Модель блюд."""

    title = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        verbose_name='Название блюда'
    )
    price = models.PositiveSmallIntegerField(
        verbose_name='Стоимость блюда'
    )

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.title


class Order(models.Model):
    """Модель заказов."""

    table_number = models.PositiveSmallIntegerField(
        verbose_name='Номер столика',
        validators=(
            MinValueValidator(
                MIN_NUM_TABLE,
                message=f'Номер столика не может быть меньше, чем {MIN_NUM_TABLE}'
            ),
        )
    )
    items = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Блюдо'
    )
    total_price = models.PositiveIntegerField(
        verbose_name='Общая стоимость заказа',
        null=True,
        blank=True,
        validators=(
            MinValueValidator(
                MIN_TOTAL_PRICE,
                message='Общая стоимость заказа не может быть отрицательной'
            ),
        )
    )
    status = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        choices=STATUSES,
        verbose_name='Статус заказа'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ стола номер - {self.table_number}'
