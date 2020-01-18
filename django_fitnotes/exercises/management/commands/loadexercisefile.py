from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from exercises.exceptions import FileImportError
from exercises.utils import load_fitnotes_exercise_file


class Command(BaseCommand):
    help = "Loads a Fitnotes exercise file into the database."

    def add_arguments(self, parser):
        parser.add_argument("exercise_file", type=str)

    def handle(self, *args, **options):
        file_path = Path(options["exercise_file"])
        try:
            load_fitnotes_exercise_file(file_path)
        except FileImportError as err:
            raise CommandError("{0}".format(err))

        self.stdout.write(
            self.style.SUCCESS("File '%s' successfully loaded." % file_path)
        )
