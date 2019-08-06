# -*- coding: utf-8 -*-
import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# don't share this with anybody.
SECRET_KEY = '{{ ;fxlbyea  }}'

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'ECU'
USE_POINTS = True


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'ko'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

SENTRY_DSN = 'http://27aac549e20541819058886d708d97c0:70b605ee46314e27b7f69c25289810a0@sentry.otree.org/74'


ROOMS = [
    # {
    #     'name': 'evo2016khu',
    #     'display_name': '진화게임협력 2016 가을 경희대',
    #         'participant_label_file': '_rooms/evo2016khu.txt',
    # },
    # {
    #     'name': '2017f',
    #     'display_name': '진화게임협력 2017 가을 경희대 (최종)',
    #     'participant_label_file': '_rooms/evokhu_2017f_final.txt',
    # },
	{
	    'name': '2018f',
		'display_name': '진화게임협력 2018 가을 경희대',
		'participant_label_file': '_rooms/stuList_evokhu_2018f_final.txt',
	},
	{
	    'name': 'ECON151_2018f',
		'display_name': '세한경 2018 가을 고려대',
		'participant_label_file': '_rooms/StdList_ECON151.txt',
	},
	# {
	#     'name': 'WjShin_2018f',
	# 	'display_name': '신우진 2018 가을',
	# 	'participant_label_file': '_rooms/wjshin_2018f.txt',
	# },
	{
	    'name': 'WjShin_201908',
		'display_name': '신우진 2019 여름',
		'participant_label_file': '_rooms/wjshin_201908.txt',
	},
] 

# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1,
    'participation_fee': 1.00,
    'num_bots': 6,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}


SESSION_CONFIGS = [
	{
		'name': 'ult_1R',
		'display_name': "최후통첩게임(1R)",
		'num_demo_participants': 2,
        'use_strategy': False,
		'app_sequence': ['ult'],
	},
	{
		'name': 'pd_1R',
		'display_name': "죄수의 딜레마(1R)",
		'num_demo_participants': 2,
		'app_sequence': ['pd_1r'],
	},
	{
		'name': 'oligopoly',
		'display_name': "복점 게임 (1R)",
		'num_demo_participants':2,
		'app_sequence': ['oligopoly'],
	},
	{
		'name': 'hd_1R',
		'display_name': "겁쟁이게임(1R)",
		'num_demo_participants': 2,
		'app_sequence': ['hd_1r'],
	},
	{
		'name': 'ult_0922',
		'display_name': "최후통첩게임(직접제안버젼4R+전략버젼4R, 풀랜덤)",
		'num_demo_participants': 2,
        'use_strategy': False,
		'app_sequence': ['ult1','ult2'],
	},
	{
		'name': 'ult_strategic',
		'display_name': "최후통첩게임(직접제안버젼1R+전략버젼1R)",
		'num_demo_participants': 2,
        'use_strategy': False,
		'app_sequence': ['ult1_1r','ult2_1r'],
	},
	{
		'name': 'volunteer',
		'display_name': "Volunteer Dilemma (전체그룹, 10R)",
		'num_demo_participants':3,
		'app_sequence': ['volunteer'],
	},
	{
		'name': 'ult_strategy',
		'display_name': "최후통첩게임(전략버젼), 4R 랜덤",
		'num_demo_participants':2,
        'use_strategy': True,
		'app_sequence': ['ult2'],
	},
	{
		'name': 'pd',
		'display_name': "죄수의 딜레마 (고정파트너,10R)",
		'num_demo_participants':2,
		'app_sequence': ['pd'],
	},
	{
		'name': 'battleSex_0929',
		'display_name': "성대결게임",
		'num_demo_participants':2,
		'app_sequence': ['battleSex'],
	},
    {
        'name': 'pd_indirect',
        'display_name': "죄수의 딜레마 평판버젼 (랜덤파트너,5R,상대의 협조횟수표시)",
        'num_demo_participants':2,
        'app_sequence': ['pd_indirect']
    },
	{
        'name': 'composite_wjshin',
        'display_name': "최후통첩 -> 죄수의딜레마(1R) -> 죄수의딜레마(10R)",
        'num_demo_participants':2,
        'app_sequence': ['ult', 'pd_1r', 'pd']
    },
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
