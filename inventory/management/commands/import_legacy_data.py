import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from inventory.models import InventoryItem

class Command(BaseCommand):
    help = 'Imports legacy Tkinter IMS dat from a CSV file into the Django database'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help='The file path to inventory.csv')
    
    def handle(self, *args, **kwargs):
        file_path = kwargs['csv_path']
        self.stdout.write(self.style.WARNING(f'Starting import from {file_path}...'))

        success_count = 0
        error_count = 0

        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)

                for row in reader:
                    if not row or len(row) < 15:
                        continue

                    try:
                        def parse_date(date_str):
                            if not date_str or date_str.strip() == '':
                                return None
                            try:
                                return datetime.strptime(date_str.strip(), '%Y-%m-%d').date()
                            except ValueError:
                                return None
                        
                        item, created = InventoryItem.objects.get_or_create(
                            serial_number=row[2].strip(),
                            defaults={
                                'item_name': row[0].strip(),
                                'location': row[1].strip(),
                                'vendor_name': row[3].strip(),
                                'vendor_invoice_number': row[4].strip(),
                                'vendor_invoice_date': parse_date(row[5]),
                                'vendor_amount': float(row[6]) if row[6].strip() else None,
                                'install_date': parse_date(row[12]),
                                'work_order': row[13].strip(),
                                'status': row[14].strip(),
                                'notes': row[15].strip() if len(row) > 15 else '',
                            }
                        )

                        if created:
                            success_count += 1
                        else:
                            self.stdout.write(f"Item {row[2]} already exists. Skipped.")
                    except Exception as e:
                        error_count += 1
                        self.stdout.write(self.style.ERROR(f"Error importing row {row[0]}: {e}"))

            self.stdout.write(self.style.SUCCESS(f'Successfully imported {success_count} items! ({error_count} errors)'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Could not find file at {file_path}'))