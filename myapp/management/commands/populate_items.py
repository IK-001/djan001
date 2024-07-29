# myapp/management/commands/populate_items.py

from django.core.management.base import BaseCommand
from myapp.models import Item

class Command(BaseCommand):
    help = 'Populate the database with food items'

    def handle(self, *args, **kwargs):
        items = [
            {'name': 'Pizza Margherita', 'description': 'Classic pizza with tomato and mozzarella', 'price': 8.99},
            {'name': 'Spaghetti Carbonara', 'description': 'Spaghetti with a creamy pancetta sauce', 'price': 10.99},
            {'name': 'Caesar Salad', 'description': 'Salad with romaine lettuce, croutons, and Caesar dressing', 'price': 7.49},
            {'name': 'Margherita Pizza', 'description': 'Tomato, mozzarella, and basil pizza', 'price': 9.99},
            {'name': 'Chicken Alfredo', 'description': 'Pasta with a creamy Alfredo sauce and grilled chicken', 'price': 12.99},
            {'name': 'Tiramisu', 'description': 'Coffee-flavored Italian dessert', 'price': 5.99},
            {'name': 'Lasagna', 'description': 'Layered pasta with meat sauce and cheese', 'price': 11.99},
            {'name': 'Greek Salad', 'description': 'Salad with cucumbers, olives, feta cheese, and tomatoes', 'price': 6.99},
            {'name': 'BBQ Ribs', 'description': 'Slow-cooked ribs with barbecue sauce', 'price': 14.99},
            {'name': 'Pancakes', 'description': 'Fluffy pancakes served with syrup and butter', 'price': 4.99},
        ]
        
        for item_data in items:
            item, created = Item.objects.get_or_create(**item_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created item: {item.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Item already exists: {item.name}'))
