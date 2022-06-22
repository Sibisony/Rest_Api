from accounts.viewsets import EmpViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('employee',EmpViewset)