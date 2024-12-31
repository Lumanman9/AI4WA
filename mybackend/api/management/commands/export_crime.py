import csv
from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import Crime  # Replace with your actual model


class Command(BaseCommand):
    help = 'Export crimes data to CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            default=f'crimes_export_{timezone.now().strftime("%Y%m%d_%H%M%S")}.csv',
            help='Output CSV file path'
        )
        parser.add_argument(
            '--start-date',
            help='Filter crimes from this date (YYYY-MM-DD)',
            required=False
        )
        parser.add_argument(
            '--end-date',
            help='Filter crimes until this date (YYYY-MM-DD)',
            required=False
        )

    def handle(self, *args, **options):
        output_file = options['output']
        start_date = options['start_date']
        end_date = options['end_date']

        # Get queryset
        queryset = Crime.objects.all()

        # Apply date filters if provided
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        # Define CSV headers based on model fields
        fields = [
            'id',
            'name',
            'description',
            'count',
            'created_at',
            'updated_at',
            # Add or remove fields based on your Crime model
        ]

        try:
            with open(output_file, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)

                # Write headers
                writer.writerow(fields)

                # Write data rows
                for crime in queryset.iterator():
                    row = [
                        getattr(crime, field, '') for field in fields
                    ]
                    writer.writerow(row)

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully exported {queryset.count()} crimes to {output_file}'
                    )
                )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error exporting crimes: {str(e)}')
            )