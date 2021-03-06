from rest_framework import routers

from departments.views import DepartmentsViewSet
from speciality.views import SpecialityViewSet
from news.views import NewsViewSet
from disciplines.views import DisciplinesViewSet
from groups.views import GroupsViewSet
from timetable.views import TimetableViewSet
from gallery.views import GalleryViewSet

from profiles.views import PeoplesViewSet, CustomUserViewSet

departmentsRouter = routers.DefaultRouter()
departmentsRouter.register('', DepartmentsViewSet)

newsRouter = routers.DefaultRouter()
newsRouter.register('', NewsViewSet)

specialityRouter = routers.DefaultRouter()
specialityRouter.register('', SpecialityViewSet)

disciplinesRouter = routers.DefaultRouter()
disciplinesRouter.register('', DisciplinesViewSet)

groupsRouter = routers.DefaultRouter()
groupsRouter.register('', GroupsViewSet)

timetableRouter = routers.DefaultRouter()
timetableRouter.register('', TimetableViewSet)

galleryRouter = routers.DefaultRouter()
galleryRouter.register('', GalleryViewSet)

peoplesRouter = routers.DefaultRouter()
peoplesRouter.register('', PeoplesViewSet)

user_djoser_router = routers.DefaultRouter()
user_djoser_router.register('', CustomUserViewSet)
