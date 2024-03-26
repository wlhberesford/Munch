'''

# my_app/cron.py
from django_cron import CronJobBase, Schedule

from .views import get_menu

class update_menu(CronJobBase):
    RUN_AT_TIMES = ['00:05']  # Run once a day at midnight

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'munchapp.cron.update_menu'    # a unique code

    def do(self):
        get_menu('https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15285&locationId=76929002&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall', 'sage')
        get_menu('https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15465&locationId=76929001&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall', 'commons')
        get_menu('https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15288&locationId=76929015&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall', 'blitman')
        get_menu('https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15286&locationId=76929003&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall', 'barh')

'''