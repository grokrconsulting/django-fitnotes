from rest_framework.serializers import ModelSerializer

from exercises.models import Category, Exercise, Set


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category


class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise


class SetSerializer(ModelSerializer):
    class Meta:
        model = Set
