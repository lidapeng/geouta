'''
Created on Aug 20, 2016

@author: Dapeng Li
'''
import urllib
from xml.dom import minidom
import string, os, sys, httplib, urllib2

class UTATracker(object):
    '''
    classdocs
    '''

    
    def __init__(self,usertoken):
        '''
        Constructor
        '''
        self. __usertoken = usertoken
    def getDataByRoute(self,routeID):
        url = "http://api.rideuta.com/SIRI/SIRI.svc/VehicleMonitor/ByRoute?route=%s&onwardcalls=true&usertoken=%s"%(routeID,self.__usertoken)
        print url
        
        s = urllib2.urlopen(url)
        print s
        xmldoc = minidom.parse(s)
        journeys = xmldoc.getElementsByTagName('MonitoredVehicleJourney')
        print journeys
	
        print len(journeys)
        for journey in journeys:
            vehicleLoc = journey.getElementsByTagName('VehicleLocation')[0]
    #         set the address value
            lat = vehicleLoc.getElementsByTagName('Latitude')[0].firstChild.nodeValue
            lon = vehicleLoc.getElementsByTagName('Longitude')[0].firstChild.nodeValue
            print lat,lon
	
        return 0  
