from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, QuizViewSet, AnswerViewSet


router = DefaultRouter()

router.register('quiz', QuizViewSet)
router.register('question', QuestionViewSet)
router.register('answer', AnswerViewSet)

urlpatterns = router.urls