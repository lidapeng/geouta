'''
Created on Aug 20, 2016

@author: Dapeng Li
'''
import psycopg2
from shapely.geometry import Point
class PostgreSQLDBConn(object):
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
        pt = Point(lat,lon)
        curs.execute('CREATE TABLE IF NOT EXISTS uta_pts(geom geometry, name text)')
        conn.commit()  # save data

        curs.execute('INSERT INTO uta_pts(geom, name) VALUES (ST_SetSRID(ST_MakePoint(%(lon)s, %(lat)s), 4326), %(name)s)',
                     {'lon': str(lon), 'lat': str(lat), 'name': 'First point'})
        conn.commit()  # save data
        