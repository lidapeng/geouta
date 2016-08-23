'''
Created on Aug 20, 2016

@author: Dapeng Li
'''
import psycopg2
from shapely.geometry import Point
class PostgreSQLDB(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def connect(self):
        conn =  psycopg2.connect(database="uta", user="postgres", password="dapeng")
        curs = conn.cursor()
        print curs
        # Send it to PostGIS
        lat, lon = 40.66531,-111.83917
        strTime = "2016-08-21T08:02:38.5588042-06:00"
        pt = Point(lat,lon)
        curs.execute('CREATE TABLE IF NOT EXISTS uta_pts(geom GEOMETRY, name TEXT, time TIMESTAMP WITH TIME ZONE)')
        conn.commit()  # save data
        #ST_MakePoint(longitude,latitude)
        curs.execute('INSERT INTO uta_pts(geom, name,time) VALUES (ST_SetSRID(ST_MakePoint(%(lon)s, %(lat)s), 4326), %(name)s,%(time)s)',
                     {'lon': str(lon), 'lat': str(lat), 'name': 'First point', 'time': strTime})
        conn.commit()  # save data
        