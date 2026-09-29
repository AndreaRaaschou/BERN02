# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:14:34 2026
@author: andrearaaschou
"""
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
from pooch import retrieve

url_vac = "https://ourworldindata.org/grapher/global-vaccination-coverage.csv?v=1&csvType=full&useColumnShortNames=true"
url_life = "https://ourworldindata.org/grapher/life-expectancy.csv?v=1&csvType=full&useColumnShortNames=true"
file_path_vac = retrieve(url=url_vac,known_hash=None)
file_path_life = retrieve(url=url_life,known_hash=None)

df_vac = pd.read_csv(file_path_vac)
df_life = pd.read_csv(file_path_life)

print(df_life.head())

print(df_life.columns.tolist())

vaccination_columns = [
    'coverage__antigen_hepb3',
    'coverage__antigen_hib3',
    'coverage__antigen_ipv1',
    'coverage__antigen_mcv1',
    'coverage__antigen_pcv3',
    'coverage__antigen_pol3',
    'coverage__antigen_rcv1',
    'coverage__antigen_rotac',
    'coverage__antigen_dtpcv3'
]


df_vac["total_coverage"] = df_vac[vaccination_columns].mean(axis=1)

df_vac_who = df_vac[df_vac["entity"].str.endswith("(WHO)", na=False)] # Only keep larger regions
df_life_who = df_life[df_life["entity"].str.endswith("(WHO)", na=False)] # Only keep larger regions

#print(df_life["entity"].unique())
#print(df_vac_who["entity"].unique())

years = sorted(df_vac_who["year"].unique())
who_regions = [
    'Africa (WHO)',
    'Americas (WHO)',
    'Eastern Mediterranean (WHO)',
    'Europe (WHO)',
    'South-East Asia (WHO)',
    'Western Pacific (WHO)'
]

who_df = df_vac_who[df_vac_who["entity"].isin(who_regions)]


fig, ax = plt.subplots(figsize=(8, 5))


for region in who_regions:
    region_data = who_df[who_df["entity"] == region]
    
    ax.plot(
        region_data["year"],
        region_data["total_coverage"],
        label=region.replace(" (WHO)", "")
    )
ax.set_yticks(range(0, 101, 10))
#ax.set_xticks(years[::5])
ax.grid( axis="y",alpha=0.3)
plt.title("Vaccination coverage (%) over time by WHO region")
plt.legend()
plt.show()














