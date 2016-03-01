import ephem as ep
def sf_sun_moon(date):
    sf = ep.Observer()
#sf.pressure = 0
#sf.horizon = '-0:34'
    sf.lat, sf.lon = '37.46', '-122.26'
    sf.date = date + ' 20:00' # noon PST
    sun_rise = (sf.previous_rising(ep.Sun()))
    sun_set = (sf.next_setting(ep.Sun()))
    sf.date = date + ' 09:00' # 1am PST
    moon_rise = (sf.previous_rising(ep.Moon()))
#    print 'mrise', moon_rise
    moon_set = (sf.next_setting(ep.Moon()))
#    print 'mset', moon_set
    sun = ep.localtime(sun_set) - ep.localtime(sun_rise)
    sun_min = sun.total_seconds() / 60
    moon = ep.localtime(moon_set) - ep.localtime(moon_rise)
#    print 'moon', moon
    moon_min = moon.total_seconds() / 60
#    print 'moonmin', moon_min
    
    nnm = ep.next_new_moon(date)
    pnm = ep.previous_new_moon(nnm)
    lunation=(sf.date-pnm)/(nnm-pnm)
    return sun_min, lunation
#    return sun_min, moon_min, lunation

# tdata['sun_length'] = tdata['dstring'].map(sun_length)
#tdata['sun_length'], tdata['moon_length'] = zip(*tdata['dstring'].apply(sun_moon_time))
#sun_length('2003/02/21')
def wind_chill(temp,wind_speed):
    return temp * wind_speed
