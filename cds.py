import cdsapi
import numpy as np
import os

start_year = 2000
end_year = 2010
years = list(range(start_year,end_year+1))
months = list(range(1,12+1))
variable = 'runoff'

c = cdsapi.Client()

for i in years:
    for j in months:

        c.retrieve(
            'reanalysis-era5-land',
            {
                'variable': variable,
                'year': i,
                'month': j,
                'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
                'time': [
                    '00:00', '01:00', '02:00',
                    '03:00', '04:00', '05:00',
                    '06:00', '07:00', '08:00',
                    '09:00', '10:00', '11:00',
                    '12:00', '13:00', '14:00',
                    '15:00', '16:00', '17:00',
                    '18:00', '19:00', '20:00',
                    '21:00', '22:00', '23:00',
                ],
                'area': [
                    42.5, 25, 35,
                    45,
                ],
                'format': 'netcdf',
            },
            'era5_year'+str(i)+'-'+str(j)+'.nc')
