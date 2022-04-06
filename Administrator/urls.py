from django.urls import re_path
from . import views

urlpatterns = [
    #admin dashboard
    re_path('adminDash/', views.adminDash, name='adminDash'),
    re_path('abc/', views.abc, name='abc'),

    #admin login
    re_path('admin_login/', views.admin_login, name='admin_login'),
    re_path('adminDash/deleteprofile/<int:id>/', views.deleteprofile,name='deleteprofile'),

    #intership
    re_path('intership/', views.intership, name='intership'),
    #platform 

    #add platform 
    re_path('platform/', views.platform, name='platform'),

    #display platform
    re_path('mainplatform/', views.mainplatform, name='mainplatform'),

    #edit platform
    re_path('mainplatform/editplatform/<int:id>/', views.editplatform, name='editplatform'),


    #update platform 
    re_path('mainplatform/editplatform/updateplatform/<int:id>/', views.updateplatform, name='updateplatform'),

    #delete platform
    re_path('mainplatform/deleteplatform/<int:id>/', views.deleteplatform,name='deleteplatform'),

    #profile
    re_path('myprofile/', views.myprofile, name='myprofile'),

    #update profile
    re_path('profileshow/<int:id>/', views.profileshow, name='profileshow'),

     
    #projects

    #projects mainpage 
    re_path('projects/', views.projects, name='projects'),

    # display requested projects on admin side
    re_path('reqprojectss/', views.reqprojectss, name='reqprojectss'),
    # re_path('adminDashboard/reqprojects/', views.reqprojects, name='reqprojects'),

    #not working
    re_path('viewprojects/', views.viewprojects, name='viewprojects'),

    #display platform 
    re_path('viewprojectdetail/', views.viewprojectdetail, name='viewprojectdetail'),

    #Home Page
    re_path('userdashboard/',views.userdashboard, name='userdashboard'),

    #add project
    re_path('addproject/', views.addproject, name='addproject'),

    #request project to admin 
    re_path('userreqprojects/', views.userreqprojects, name='userreqprojects'),

    #display projects based on platform
    re_path('userprojects/<int:id>', views.userpythonprojects, name='userpythonprojects'),

    re_path('adminprojectsview/<int:id>', views.adminprojectsview, name='adminprojectsview'),

    #not working
    re_path('userandroidprojects/', views.userandroidprojects, name='userandroidprojects'),
    re_path('usermlprojects/', views.usermlprojects, name='usermlprojects'),

    #display project details
    re_path('userviewpython/<int:id>', views.userviewpython, name='userviewpython'),
    
    #save user request project
    re_path('userreqprojects/userreqprojectdb/', views.userreqprojectdb, name='userreqprojectdb'),
    
    #delete projects
    re_path('viewprojectdetail/deleteprojects/<int:id>/', views.deleteprojects,name='deleteprojects'),

    #save project details
    re_path('addproject/addnewprojectdb/', views.addnewprojectdb, name='addnewprojectdb'),

    #save platform details
    re_path('platform/addnewplatformdb/', views.addnewplatformdb, name='addnewplatformdb'),

    #not working
    re_path('viewmlproject/<int:id>', views.viewmlproject, name='viewmlproject'),
    re_path('viewandroidproject/<int:id>', views.viewandroidproject, name='viewandroidproject'),
    re_path('takeDiversion/<str:name>', views.ProjectDiverter, name='takeDiversion'),
    re_path('viewmlprojects/', views.viewmlprojects, name='viewmlprojects'),
    re_path('viewandroidprojects/', views.viewandroidprojects, name='viewandroidprojects'),

    #update profile
    re_path('myprofile/profilecreate/<int:id>/', views.profilecreate, name='profilecreate'),

    # create a profile
    re_path('myprofile/newprofilecreate/', views.newprofilecreate, name='newprofilecreate'),

    #not working
    re_path('result/', views.result, name='result'),

    re_path('getproject/<int:id>', views.getproject, name='getproject'),
    re_path('show_inbuiltproject_requests/', views.show_inbuiltproject_requests, name='show_inbuiltproject_requests'),

    #search projects
    re_path('search/',views.search,name='search'),

    re_path('main_ieee', views.main_ieee, name='main_ieee'),

    re_path('main_ieee/deletepaper/<int:id>/', views.deletepaper,name='deletepaper'),

    re_path('add_ieee', views.add_ieee, name='add_ieee'),

    re_path('add_ieee_db', views.add_ieee_db, name='add_ieee_db'),

    re_path('view_ieee_papers/<int:id>', views.view_ieee_papers, name='view_ieee_papers'),

    re_path('ieee_search/',views.ieee_search,name='ieee_search'),

    re_path('user_req_ieee_projects/<int:id>', views.user_req_ieee_projects, name='user_req_ieee_projects'),

    re_path('user_req_ieee_projects/user_req_ieeeprojectdb/', views.user_req_ieeeprojectdb, name='user_req_ieeeprojectdb'),

    re_path('req_ieee/', views.req_ieee, name='req_ieee'),
    
    re_path('userviewpy/', views.userviewpy, name='userviewpy'),


    re_path('user_req_inbuilt_projects/<int:id>', views.user_req_inbuilt_projects, name='user_req_inbuilt_projects'),

    re_path('user_req_inbuilt_projectdb/', views.user_req_inbuilt_projectdb, name='user_req_inbuilt_projectdb'),
    
    re_path('userintership/', views.userintership, name='userintership'),

    re_path('interview_q_a/', views.interview_q_a, name='interview_q_a'),

    re_path('interview/', views.interview, name='interview'),

    re_path('deleteq/<int:id>', views.deleteq, name='deleteq'),

    re_path('interview_Q_A/', views.interview_Q_A, name='interview_Q_A'),

    re_path('admin_logout', views.admin_logout, name='admin_logout'),

    re_path('activate', views.activate, name='activate'),

    re_path('quiz/', views.quiz, name='quiz'),


    re_path('savemockq/', views.savemockq, name='savemockq'),

    re_path('usermockexam/', views.usermockexam, name='usermockexam'),

    re_path('takemocktest/', views.takemocktest, name='takemocktest'),


    re_path('deletequestion/<int:id>', views.deletequestion, name='deletequestion'),

    re_path('mailmeresult/', views.mailmeresult, name='mailmeresult'),

    re_path('home/', views.home, name='home'),

    re_path('viewtutorial/', views.viewtutorial, name='viewtutorial'),

    re_path('addvediotutorial/', views.addvediotutorial, name='addvediotutorial'),

    re_path('uploadtutorial/', views.uploadtutorial, name='uploadtutorial'),


    re_path('delvediotutorial/<int:id>', views.delvediotutorial, name='delvediotutorial'),


    re_path('userviewtutorial', views.userviewtutorial, name='userviewtutorial'),
    #courses module
    re_path('courses/', views.courses, name='courses'),
    #Platform
    re_path('platforms/', views.platforms, name='platforms'),
    re_path('addplatform/', views.addplatform, name='addplatform'),
    re_path('addplatforms/', views.addplatforms, name='addplatforms'),
    re_path('editplatform/<int:platformid>', views.editplatform, name='editplatform'),
    re_path('updateplatform/<int:platformid>', views.updateplatform, name='updateplatform'),
    re_path('deleteplatform/<int:platformid>', views.deleteplatform, name='deleteplatform'),
    #Courses
    re_path('course/', views.course, name='course'),
    re_path('addcoursepage/', views.addcoursepage, name='addcoursepage'),
    re_path('addcourse/', views.addcourse, name='addcourse'),
    re_path('editcourse/<int:courseid>', views.editcourse, name='editcourse'),
    re_path('updatecourse/<int:courseid>', views.updatecourse, name='updatecourse'),
    re_path('deletecourse/<int:courseid>', views.deletecourse, name='deletecourse'),

    re_path('lectures/', views.lectures, name='lectures'),
    re_path('addlecturepage/', views.addlecturepage, name='addlecturepage'),
    re_path('addlecture/', views.addlecture, name='addlecture'),
    re_path('editlecture/<int:lectureid>/', views.editlecture, name='editlecture'),
    re_path('updatelecture/<int:lectureid>', views.updatelecture, name='updatelecture'),
    re_path('deletelecture/<int:lectureid>', views.deletelecture, name='deletelecture'),

    re_path('questions/', views.questions, name='questions'),
    re_path('addquestionpage/', views.addquestionpage, name='addquestionpage'),
    re_path('addquestion/', views.addquestion, name='addquestion'),
    re_path('editquestionpage/<int:qandaid>', views.editquestionpage, name='editquestionpage'),
    re_path('updatequestion/<int:qandaid>', views.updatequestion, name='updatequestion'),
    re_path('deletequestionanswer/<int:qandaid>', views.deletequestionanswer, name='deletequestionanswer'),

    re_path('usercreate', views.usercreate, name='usercreate'),


    re_path('gologin/', views.gologin, name='gologin'),


    re_path('gosignup/', views.gosignup, name='gosignup'),

    re_path('userlogin', views.userlogin, name='userlogin'),
    re_path('userdash', views.userdash, name='userdash'),

    re_path('userprofile', views.userprofile, name='userprofile'),
    re_path('tutorials', views.tutorials, name='tutorials'),
   
    re_path('tutorialview/<int:lectureid>', views.tutorialview, name='tutorialview'),
    re_path('userlogout', views.userlogout, name='userlogout'),
    re_path('edituserprofile',views.edituserprofile, name='edituserprofile'),
    re_path('updateuserprofile',views.updateuserprofile, name='updateuserprofile'),
    re_path('certificate',views.certificate, name='certificate'),
    re_path('test',views.test, name='test'),
    re_path('score1', views.score1, name='score1'),
    re_path('gocertificate', views.gocertificate, name='gocertificate'),
    re_path('gonocertificate', views.gonocertificate, name='gonocertificate'),
    
    
    
]
