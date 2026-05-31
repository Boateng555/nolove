from django.db import migrations


def add_missing_dateproposal_columns(apps, schema_editor):
    connection = schema_editor.connection
    if connection.vendor != 'sqlite':
        return

    with connection.cursor() as cursor:
        cursor.execute('PRAGMA table_info(proposal_dateproposal)')
        existing = {row[1] for row in cursor.fetchall()}

        columns = [
            ('completed', 'INTEGER NOT NULL DEFAULT 0'),
            ('food_chosen_at', 'datetime NULL'),
            ('said_yes', 'INTEGER NOT NULL DEFAULT 0'),
            ('said_yes_at', 'datetime NULL'),
            ('scheduled_at', 'datetime NULL'),
            ('session_key', 'varchar(40) NOT NULL DEFAULT \'\'' ),
            ('updated_at', 'datetime NULL'),
        ]

        for name, col_type in columns:
            if name not in existing:
                cursor.execute(
                    f'ALTER TABLE proposal_dateproposal ADD COLUMN {name} {col_type}'
                )


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0006_alter_dateproposal_options_dateproposal_completed_and_more'),
    ]

    operations = [
        migrations.RunPython(add_missing_dateproposal_columns, migrations.RunPython.noop),
    ]
