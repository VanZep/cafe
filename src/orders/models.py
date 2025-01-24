from django.db import models
from django.core.validators import MinValueValidator

from src.orders.constants import(
    MIN_NUM_TABLE, MIN_TOTAL_PRICE, CHARFIELD_MAX_LENGTH, STATUSES
)


class Item(models.Model):
    """Модель блюд."""

    title = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        verbose_name='Название блюда'
    )
    price = models.IntegerField(
        verbose_name='Стоимость блюда'
    )

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.title


class Order(models.Model):
    """Модель заказов."""

    table_number = models.IntegerField(
        verbose_name='Номер столика',
        validators=(
            MinValueValidator(
                MIN_NUM_TABLE,
                message='Номер стола не может быть отрицательным'
            ),
        )
    )
    items = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        related_name='orders',
        verbose_name='Блюдо'
    )
    total_price = models.IntegerField(
        verbose_name='Общая стоимость заказа',
        validators=(
            MinValueValidator(
                MIN_TOTAL_PRICE,
                message='Общая стоимость заказа не может быть отрицательной'
            ),
        )
    )
    status = models.IntegerChoices(
        choices=STATUSES,
        verbose_name='Статус заказа'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ стола номер - {self.table_number}'
