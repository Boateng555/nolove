import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from proposal.models import FoodOption, SiteContent, TimeSlot

DEFAULT_FOODS = [
    ('pizza', 'Pizza', '🍕', 0),
    ('sushi', 'Sushi', '🍣', 1),
    ('burgers', 'Burgers', '🍔', 2),
    ('pasta', 'Pasta', '🍝', 3),
    ('tacos', 'Tacos', '🌮', 4),
    ('ramen', 'Ramen', '🍜', 5),
]

DEFAULT_TIMES = [
    '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM',
    '5:00 PM', '6:00 PM', '7:00 PM', '8:00 PM',
]


class Command(BaseCommand):
    help = 'Create admin user and seed default site content'

    def add_arguments(self, parser):
        parser.add_argument('--username', default=os.environ.get('ADMIN_USERNAME', 'admin'))
        parser.add_argument('--password', default=os.environ.get('ADMIN_PASSWORD', 'nolove123'))
        parser.add_argument('--email', default=os.environ.get('ADMIN_EMAIL', 'admin@local.dev'))

    def handle(self, *args, **options):
        User = get_user_model()
        username = options['username']
        password = options['password']
        email = options['email']

        SiteContent.load()

        if not FoodOption.objects.exists():
            for slug, label, emoji, order in DEFAULT_FOODS:
                FoodOption.objects.create(slug=slug, label=label, emoji=emoji, order=order)
            self.stdout.write(self.style.SUCCESS('Seeded food options'))

        if not TimeSlot.objects.exists():
            for i, label in enumerate(DEFAULT_TIMES):
                TimeSlot.objects.create(label=label, order=i)
            self.stdout.write(self.style.SUCCESS('Seeded time slots'))

        user, created = User.objects.get_or_create(username=username, defaults={'email': email})
        user.is_staff = True
        user.is_superuser = True
        if created:
            user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f'Created admin user: {username}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Updated admin user: {username}'))

        self.stdout.write('')
        self.stdout.write('Dashboard login:')
        self.stdout.write(f'  URL:      http://127.0.0.1:8000/dashboard/login/')
        self.stdout.write(f'  Username: {username}')
        self.stdout.write(f'  Password: {password}')
        self.stdout.write('')
        self.stdout.write(self.style.WARNING('Change your password after first login!'))
