from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    RecordingViewSet,
    EventViewSet,
    SubscriptionViewSet,
    CourseViewSet,
    GroupViewSet,
    ModuleViewSet,
    PaymentMethodViewSet,
    SubscriptionTypeViewSet,
    EnrollmentViewSet,
    LessonViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register("enrollment", EnrollmentViewSet)
router.register("module", ModuleViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("recording", RecordingViewSet)
router.register("group", GroupViewSet)
router.register("course", CourseViewSet)
router.register("event", EventViewSet)
router.register("category", CategoryViewSet)
router.register("lesson", LessonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
