# Seu arquivo 0008_...py

import datetime
import django.db.models.deletion
from django.db import migrations, models

# ... (a classe Migration e dependencies permanecem as mesmas)

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_emprestimo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='emprestimo',
            name='status',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='colaborador',
            field=models.ForeignKey(
                # CORREÇÃO: Deve ser um NÚMERO INTEIRO (ID)
                default=1, 
                on_delete=django.db.models.deletion.CASCADE, 
                to='app.colaborador'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='data_emprestimo',
            # Este campo pode ter 'null=True' adicionado para evitar erros em SQLite
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='equipamento',
            field=models.ForeignKey(
                # CORREÇÃO: Deve ser um NÚMERO INTEIRO (ID)
                default=1, 
                on_delete=django.db.models.deletion.CASCADE, 
                to='app.equipamento'
            ),
            preserve_default=False,
        ),
    ]