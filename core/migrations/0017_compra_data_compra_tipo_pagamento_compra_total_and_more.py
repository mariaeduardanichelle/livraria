# Generated by Django 5.1.3 on 2024-12-19 01:10

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_itenscompra_preco"),
    ]

    operations = [
        migrations.AddField(
            model_name="compra",
            name="data",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="compra",
            name="tipo_pagamento",
            field=models.IntegerField(
                choices=[
                    (1, "Cartão de Crédito"),
                    (2, "Cartão de Débito"),
                    (3, "PIX"),
                    (4, "Boleto"),
                    (5, "Transferência Bancária"),
                    (6, "Dinheiro"),
                    (7, "Outro"),
                ],
                default=1,
            ),
        ),
        migrations.AddField(
            model_name="compra",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="compra",
            name="status",
            field=models.IntegerField(
                choices=[(1, "Carrinho"), (2, "Finalizado"), (3, "Pago"), (4, "Entregue")], default=1
            ),
        ),
        migrations.AlterField(
            model_name="itenscompra",
            name="livro",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="itenscompra", to="core.livro"
            ),
        ),
        migrations.AlterField(
            model_name="itenscompra",
            name="preco",
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
