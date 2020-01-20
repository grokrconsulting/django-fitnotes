from rest_framework.routers import SimpleRouter

from exercises.views import (
    CategoryReadOnlyViewSet,
    ExerciseReadOnlyViewSet,
    SetReadOnlyViewSet,
)

router = SimpleRouter()
router.register("categories", CategoryReadOnlyViewSet)
router.register("exercises", ExerciseReadOnlyViewSet)
router.register("sets", SetReadOnlyViewSet)
