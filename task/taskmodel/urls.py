from django.contrib import admin
from django.urls import path
from . import onUser,onSchedule,onNote,tests

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',onUser.register),   #User方面
    path('login/',onUser.login1),
    path('searchuser/',onUser.searchuser),
    path('updateuser/',onUser.updateuser),
    path('deleteuser/',onUser.deleteuser),
    path('updatepassword/',onUser.updatepassword),
    path('addschedule/',onSchedule.addschedule),    #Schedule方面
    path('deleteschedule/',onSchedule.deleteschedule),
    path('updateschedule1/',onSchedule.updateschedule1),
    path('updateschedule2/',onSchedule.updateschedule2),
    path('searchschedule/',onSchedule.searchschedule),
    path('set_done_schedule/',onSchedule.set_done_schedule),
    path('addnote/',onNote.addnote1), #Note方面
    path('deletenote/',onNote.deletenote),
    path('updatenote1/',onNote.updatenote1),
    path('updatenote2/',onNote.updatenote2),
    path('searchnote/',onNote.searchnote),
    path('registertest/',onUser.registertest),
    path('test/',tests.test),
]