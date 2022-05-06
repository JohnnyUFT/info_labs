def _filter(self):
	if self.ignition_on is not None:
        self.df = self.df.query("hardware_ignition" == int(self.ignition))
    if self.alert is not None:
        if self.alert == "gps_speed":
            self.df = self.df.query("speed" > self.speed)
        else:
            self.df = self.df.query(self.alert == 1)

def build(self):
    self._filter()
    return self.df
    
# e se o dataframe estiver vazio apos o primero slice???

# ------------------------------------ #

from django.test import TestCase
#from myapp.models import Reports
from pandas import Dataframe

class ReportTripCase(TestCase):
    def setUp(self):
        # definir os parametros
        # pass
        self.alert = None
        self.speed = 84
        self.ignition_on = True
        
        # a definir o Dataframe
        
    
    def test_report_trip_filter_alert_none(self):
        '''
        Testa filtro: caso alert None
        '''
        self.assertEqual(self.alert, None)
        
    def test_report_trip_filter_alert_gps_speed(self):
        '''
        Testa filtro: caso alert == gps_speed
        '''
        self.assertEqual(self.alert, self.gps_speed)
    
    def test_report_trip_filter_alert_other(self):
        '''
        Testa filtro: caso alert not None and alert != gps_speed
        Pode ser 1: 'anchor', 2: 'hardware_panic', 3: 'hardware_anti_theft_status'
        '''
        
        # refatorar
        self.df['columnn'] = 1 
        self.assertEqual(self.df['column'], self.alert)
        