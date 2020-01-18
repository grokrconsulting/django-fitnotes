import csv
import datetime
from collections import namedtuple
from pathlib import Path

from exercises.exceptions import FileImportError
from exercises.models import Category, Exercise, Set

EXERCISE_FILE_HEADERS = [
    "date",
    "exercise",
    "category",
    "weight_kg",
    "reps",
    "distance",
    "distance_unit",
    "time",
]

FitnotesRow = namedtuple("FitnotesRow", EXERCISE_FILE_HEADERS + ["file_id"])


def load_fitnotes_exercise_file(file_path: Path):

    if not file_path.exists():
        raise FileImportError("File '%s' does not exist." % file_path)

    with open(file_path, "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader, None)  # skip header

        # We make the assumption that the row position of an exercise never
        # changes.
        for row_id, data in enumerate(reader):
            if data[3] == "":
                continue
            row = FitnotesRow(*data + [row_id])
            save_row(row)


def save_row(row: FitnotesRow):
    category, created = Category.objects.get_or_create(name=row.category)
    exercise, created = Exercise.objects.get_or_create(
        name=row.exercise, category=category
    )
    set_, created = get_or_create_set(row, exercise.id)
    return set_


def get_or_create_set(row: FitnotesRow, exercise_id: int):
    weight = float(row.weight_kg)
    reps = int(row.reps)
    date = datetime.date.fromisoformat(row.date)
    return Set.objects.get_or_create(
        date=date,
        file_id=row.file_id,
        weight=weight,
        repetitions=reps,
        exercise_id=exercise_id,
    )

