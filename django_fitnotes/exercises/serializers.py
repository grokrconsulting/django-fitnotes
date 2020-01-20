from rest_framework.serializers import ModelSerializer

from exercises.models import Category, Exercise, Set


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class SetSerializer(ModelSerializer):
    class Meta:
        model = Set
        fields = "__all__"
