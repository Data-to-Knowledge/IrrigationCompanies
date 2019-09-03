# -*- coding: utf-8 -*-


"""
Hey Katie

I’d be keen to know the percentage of data, as well as days of data (>90%), available for each WAP that should be reported (>5l/s) for all consents associated with Irrigation schemes?

Thanks, Eila
"""

"""
Created on Wed Sep  4 10:00:52 2019

@author: KatieSi
"""
import numpy as np
import pandas as pd
import pdsql
from datetime import datetime, timedelta


TelemetryFromDate = '2018-07-01'
TelemetryToDate = '2019-06-30'

Baseline = pd.read_csv(r"D:\\Implementation Support\\Python Scripts\\scripts\\Segmentation2019\\Baseline.csv")

Irrigation = pd.read_csv(r"D:\\Implementation Support\\Python Scripts\\scripts\\Import\\IrrigationSchemes.csv")
Irrigation['Activity'] = Irrigation['Activity'].str.strip().str.lower()

Irrigation = pd.merge(Irrigation, Baseline, on = ['ConsentNo','WAP', 'Activity'], how = 'left')


Irrigation = Irrigation[[
                'Organisation',
                'ConsentNo',
                'Activity',
                'WAP',
                'WellStatus', 
                'Waiver',                
                'WAPsOnConsent',
                'ConsentsOnWAP',
                'WAPRate',             
                'T_DaysOfData'
                ]]

Irrigation = Irrigation.drop_duplicates()
Irrigation[['T_DaysOfData']] = Irrigation[['T_DaysOfData']].fillna(value=0)
Irrigation = Irrigation[Irrigation['WAPRate'] >= 5]

Irrigation['PercentOfData'] = Irrigation['T_DaysOfData']/365 *100
Irrigation['PercentOfData'] = Irrigation['PercentOfData'].round(0).astype(int)

Irrigation.rename(columns={'T_DaysOfData': 'DaysOfData'}, inplace=True)


Irrigation.to_csv('Irrigation.csv')
