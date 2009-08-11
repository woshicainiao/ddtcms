from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from ddtcms.member.views import *
from django.conf import settings


from ddtcms.member.models import Profile,Resume


    
    
info_dict = {
'queryset': Profile.objects.all(),
'template_name':'member/index.html',
}


pages_dict = {
'queryset': Profile.objects.all(),
'paginate_by':1,
}

urlpatterns = patterns('',
    # Private profile
    
    url(r'^profile/$', overview, name='profile_overview'),

    url(r'^profile/edit/location/$', location, name='profile_edit_location'),

    url(r'^profile/edit/location/done/$', direct_to_template,
        {'extra_context': {'section': 'location'},
        'template': 'member/profile/location_done.html'},
        name='profile_edit_location_done'),

    url(r'^profile/edit/personal/$', personal, name='profile_edit_personal'),

    url(r'^profile/edit/personal/done/$', direct_to_template,
        {'extra_context': {'section': 'personal'},
        'template': 'member/profile/personal_done.html'},
        name='profile_edit_personal_done'),

    url(r'^profile/delete/$', delete, name='profile_delete'),

    url(r'^profile/delete/done/$', direct_to_template,
        {'extra_context': {'section': 'delete'},
        'template': 'member/profile/delete_done.html'},
        name='profile_delete_done'),

    url(r'^profile/getcountry_info/(?P<lat>[0-9\.\-]+)/(?P<lng>[0-9\.\-]+)/$',
        fetch_geodata,
        name='profile_geocountry_info'),

    # Avatars
    url(r'^profile/edit/avatar/delete/$', avatardelete,
        name='profile_avatar_delete'),

    url(r'^profile/edit/avatar/$', avatarchoose, name='profile_edit_avatar'),

    url(r'^profile/edit/avatar/search/$', searchimages,
        name='profile_avatar_search'),

    url(r'^profile/edit/avatar/crop/$', avatarcrop,
        name='profile_avatar_crop'),

    url(r'^profile/edit/avatar/crop/done/$', direct_to_template,
        { 'extra_context': {'section': 'avatar'},
        'template': 'member/avatar/done.html'},
        name='profile_avatar_crop_done'),

    # Account utilities
    url(r'^email/validation/$', email_validation, name='email_validation'),

    url(r'^email/validation/processed/$', direct_to_template,
        {'template': 'member/account/email_validation_processed.html'},
        name='email_validation_processed'),

    url(r'^email/validation/(?P<key>.{70})/$', email_validation_process,
        name='email_validation_process'),

    url(r'^email/validation/reset/$', email_validation_reset,
        name='email_validation_reset'),

    url(r'^email/validation/reset/(?P<action>done|failed)/$',
        direct_to_template,
        {'template' : 'member/account/email_validation_reset_response.html'},
        name='email_validation_reset_response'),

    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset',
        {'template_name': 'member/account/password_reset.html',
         'email_template_name': 'member/email/password_reset_email.txt' },
        name='password_reset'),

    url(r'^password/reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'member/account/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^password/change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'member/account/password_change.html'},
        name='password_change'),

    url(r'^password/change/done/$', 
        'django.contrib.auth.views.password_change_done',
        {'template_name': 'member/account/password_change_done.html'},
        name='password_change_done'),

    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'member/account/password_reset_confirm.html'},
        name="password_reset_confirm"),

    url(r'^reset/done/$',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'member/account/password_reset_complete.html'},
        name="password_reset_complete"),

    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'member/account/login.html'},
        name='login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'member/account/logout.html'},
        name='logout'),
    
    #2009-5-23 15:53:09 add
    url(r'^redirect_to_login/$', 'django.contrib.auth.views.redirect_to_login',
        name='redirect_to_login'),
    #2009-5-23 15:53:15addend


    # Registration
    url(r'^register/$', register, name='signup'),

    url(r'^register/validate/$', direct_to_template,
        {'template' : 'member/account/validate.html'},
        name='signup_validate'),

    #url(r'^register/complete/$', direct_to_template,
    #    {'template': 'member/account/registration_done.html'},
    #    name='signup_complete'),
    
    url(r'^register/complete/(?P<username>.+)/$', register_complete,name='signup_complete'),

    # Users public profile
    url(r'^profile/(?P<username>.+)/$', public, name='profile_public'),

)

urlpatterns += patterns('',
	url(r'^ajax_loginsta/$', ajax_loginsta,  name="ajax_loginsta"),
)