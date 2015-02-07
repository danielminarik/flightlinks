 #!/usr/bin/python
 # -*- coding: utf-8 -*-

## This file is part of ISS.

## ISS is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.

## ISS is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with ISS.  If not, see <http://www.gnu.org/licenses/>.


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_mainform import Ui_MainWindow
import os
import sys
import datetime
import configparser
from airportsmodel import AirportsModel, AirportsModelSort


APPDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
INIFILE = APPDIR + '\config.ini'

class Mainform(QMainWindow, Ui_MainWindow):
    """Class represents main window of application."""
    
    def __init__(self):
        super(Mainform, self).__init__()
        self.setupUi(self)
        self.config = configparser.ConfigParser()
        self.loadConfig()
        
        # Main configuration for flight search engines
        self.links_to_open = []
        self.config_dict = {'pelikan.sk':
                                {'roundtrip': 'https://www.pelikan.sk/sk/#/flights/list?dfc=C{frm}&dtc=C{to}&rfc=C{to}&rtc=C{frm}&dd={date_from}&rd={date_to}&px=1000&ns=0&prc=&rng=1&rbd=0&ct=0',
                                 'multicity': 'https://www.pelikan.sk/sk/#/flights/list?dfc=C{frm}&dtc=C{to}&rfc=C{to}&rtc=C{frm2}&dd={date_from}&rd={date_to}&px=1000&ns=0&prc=&rng=1&rbd=0&ct=0',
                                 'oneway': 'https://www.pelikan.sk/sk/#/flights/list?dfc=C{frm}&dtc=C{to}&rfc=&rtc=&dd={date_from}&rd=&px=1000&ns=0&prc=&rng=1&rbd=0&ct=0',
                                 'date_format': '%Y-%m-%d'},
                            'kayak.com':
                                {'roundtrip': 'http://www.kayak.com/flights/{frm}-{to}/{date_from}-flexible/{date_to}-flexible',
                                 'multicity': 'http://www.kayak.com/flights/{frm}-{to}/{date_from}/{to}-{frm2}/{date_to}',
                                 'oneway': 'http://www.kayak.com/flights/{frm}-{to}/{date_from}-flexible',
                                 'date_format': '%Y-%m-%d'},
                            'tripadvisor.com':
                                {'roundtrip': 'http://www.tripadvisor.sk/CheapFlights?geo=274714&pax0=a&travelers=1&cos=0&nonstop=no&airport0={frm}&nearby0=no&airport1={to}&nearby1=no&date0={date_from}&time0=0024&date1={date_to}&time1=0024&cr=0',
                                 'multicity': 'http://www.tripadvisor.sk/CheapFlights?geo=274714&pax0=a&travelers=1&cos=0&nonstop=no&airport0={frm}&nearby0=no&airport1={to}&nearby1=no&date0={date_from}&time0=anytime&airport2={to}&nearby2=no&airport3={frm2}&nearby3=no&date1={date_to}&time1=anytime',
                                 'oneway': 'http://www.tripadvisor.sk/CheapFlights?geo=274714&pax0=a&travelers=1&cos=0&nonstop=no&airport0={frm}&nearby0=no&airport1={to}&nearby1=no&date0={date_from}&time0=0024&cr=0',
                                 'date_format': '%Y%m%d'},
                            'momondo.com':
                                {'roundtrip': 'http://www.momondo.cz/flightsearch/?Search=true&TripType=2&SegNo=2&SO0={frm}&SD0={to}&SDP0={date_from}&SO1={to}&SD1={frm}&SDP1={date_to}&AD=1&TK=ECO&DO=false&NA=false#Search=true&TripType=2&SegNo=2&SO0={frm}&SD0={to}&SDP0={date_from}&SO1={to}&SD1={from}&SDP1={date_to}&AD=1&TK=ECO&DO=false&NA=false',
                                 'multicity': 'http://www.momondo.cz/flightsearch/?Search=true&TripType=4&SegNo=2&SO0={frm}&SD0={to}&SDP0={date_from}&SO1={to}&SD1={frm2}&SDP1={date_to}&AD=1&TK=ECO&NA=false#Search=true&TripType=4&SegNo=2&SO0={frm}&SD0={to}&SDP0={date_from}&SO1={to}&SD1={frm2}&SDP1={date_to}&AD=1&TK=ECO&NA=false',
                                 'oneway': 'http://www.momondo.cz/flightsearch/?Search=true&TripType=1&SegNo=1&SO0={frm}&SD0={to}&SDP0={date_from}&AD=1&TK=ECO&DO=false&NA=false#Search=true&TripType=1&SegNo=1&SO0={frm}&SD0={to}&SDP0={date_from}&AD=1&TK=ECO&DO=false&NA=false',
                                 'date_format': '%d-%m-%Y'},
                            'skyscanner.com':
                                {'roundtrip': 'http://www.skyscanner.cz/transport/flights/{frm}/{to}/{date_from}/{date_to}/',
                                 'multicity': None,
                                 'oneway': 'http://www.skyscanner.cz/transport/flights/{frm}/{to}/{date_from}/',
                                 'date_format': '%y%m%d'},
                            }
    def loadConfig(self):
        self.config.read(INIFILE)
        for section in self.config.sections():
            tab = QFrame()
            gl = QGridLayout(tab)

            tv_from = QTableView(tab)
            tv_from.setObjectName('tv_from')
            tv_from.verticalHeader().hide()
            model_from = AirportsModel()
            tv_from.setModel(AirportsModelSort(model_from))
            tv_from.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
            model_from.loadData(self.config.get(section, 'from'))
            date_from = QDateEdit()
            date_from.setObjectName('date_from')
            raw_date = self.config.get(section, 'date_from').split('-')
            date_from.setDate(datetime.datetime(int(raw_date[0]), int(raw_date[1]), int(raw_date[2])))
            date_from.setCalendarPopup(True)
            gl.addWidget(QLabel('Flights form'), 0, 0)
            gl.addWidget(tv_from, 1, 0)
            gl.addWidget(date_from, 2, 0)

            tv_to = QTableView(tab)
            tv_to.setObjectName('tv_to')
            tv_to.verticalHeader().hide()
            model_to = AirportsModel()
            tv_to.setModel(AirportsModelSort(model_to))
            tv_to.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
            model_to.loadData(self.config.get(section, 'to'))
            date_to = QDateEdit()
            date_to.setObjectName('date_to')
            raw_date = self.config.get(section, 'date_to').split('-')
            date_to.setDate(datetime.datetime(int(raw_date[0]), int(raw_date[1]), int(raw_date[2])))
            date_to.setCalendarPopup(True)
            gl.addWidget(QLabel('Flights to'), 0, 1)
            gl.addWidget(tv_to, 1, 1)
            gl.addWidget(date_to, 2, 1)

            self.tabWidget.addTab(tab, section)

    @pyqtSlot()
    def on_btn_combine_clicked(self):
        if self.rb_pelikansk.isChecked():
            engine = 'pelikan.sk'
        elif self.rb_kayakcom.isChecked():
            engine = 'kayak.com'
        elif self.rb_tripadvisorcom.isChecked():
            engine = 'tripadvisor.com'
        elif self.rb_momondocom.isChecked():
            engine = 'momondo.com'
        elif self.rb_skyscannercom.isChecked():
            engine = 'skyscanner.com'

        # Widgets
        w_tv_from = self.tabWidget.currentWidget().findChild(QTableView, 'tv_from')
        w_tv_to = self.tabWidget.currentWidget().findChild(QTableView, 'tv_to')
        w_date_from = self.tabWidget.currentWidget().findChild(QDateEdit, 'date_from')
        date_from = datetime.datetime(w_date_from.date().year(), w_date_from.date().month(), w_date_from.date().day())
        date_from = date_from.strftime(self.config_dict[engine]['date_format'])
        w_date_to = self.tabWidget.currentWidget().findChild(QDateEdit, 'date_to')
        date_to = datetime.datetime(w_date_to.date().year(), w_date_to.date().month(), w_date_to.date().day())
        date_to = date_to.strftime(self.config_dict[engine]['date_format'])
        airports_from = w_tv_from.model().sourceModel().getCheckedItems()
        airports_to = w_tv_to.model().sourceModel().getCheckedItems()

        # Creating combinations
        self.links_to_open = []
        if self.rb_roundtrip.isChecked():
            direction = 'roundtrip'
            # If not possible
            if self.config_dict[engine][direction] == None:
                return
            for f in airports_from:
                for t in airports_to:
                    self.links_to_open.append(self.config_dict[engine][direction].format(frm=f, to=t, date_from=date_from, date_to=date_to))
        elif self.rb_multicity.isChecked():
            direction = 'multicity'
            # If not possible
            if self.config_dict[engine][direction] == None:
                return
            for f in airports_from:
                for t in airports_to:
                    for f2 in airports_from:
                        if f != f2:
                            self.links_to_open.append(self.config_dict[engine][direction].format(frm=f, to=t, frm2=f2, date_from=date_from, date_to=date_to))
        elif self.rb_oneway.isChecked():
            direction = 'oneway'
            # If not possible
            if self.config_dict[engine][direction] == None:
                return
            for f in airports_from:
                for t in airports_to:
                    self.links_to_open.append(self.config_dict[engine][direction].format(frm=f, to=t, date_from=date_from, date_to=date_to))

        self.btn_open.setText("Open in browser ({})".format(len(self.links_to_open)))

    @pyqtSlot()
    def on_btn_open_clicked(self):
        links = str(self.links_to_open).replace('[', '').replace('[', '').replace('\'', '\"')
        os.system('start chrome --incognito {}'.format(links))

# End of mainform.py
