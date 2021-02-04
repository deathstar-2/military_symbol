#date of release: 2021 01 15
#version 4 variables import file

unit_val=['Blank Type','Infantry','Mech Infantry',
          'Cavalry','Mech Cav','Armored','Artillery',
          'Aviation','Cmbnd Arms','CBRNE',
          'Engineer','Medical','Mil Int',
          'Maintenance','Mil Pol','Mortar',
          'Signal','Space','Support',
          'Sustainment','Transporation','UAV']

mod_one=['Coming Soon',]#for future use

mod_two=['Coming Soon',]#for future use

bd_amp=['Blank','Team','Squad','Section',
        'Platoon','Company','Battalion',
        'Brigade','Division','Corps',
        'Army']

#PhotoImage lists.  MUST match above list indices!
#For UNIT icon variable
#imagery_10 is underlying read/write icon list
imagery_10=['img/icon_blank.png','img/icon_product.png','img/icon_cleared.png']

imagery_11=[
    'unit_blank.png',
    'unit_inf.png',
    'unit_minf.png',
    'unit_cav.png',
    'unit_mcav.png',
    'unit_arm.png',
    'unit_art.png',
    'unit_avn1.png',
    'unit_carms.png',
    'unit_cbrne.png',
    'unit_eng.png',
    'unit_med.png',
    'unit_mint.png',
    'unit_mntc.png',
    'unit_mp.png',
    'unit_mtr.png',
    'unit_sig.png',
    'unit_spc.png',
    'unit_spt.png',
    'unit_sust.png',
    'unit_trnsp.png',
    'unit_uav.png'
    ]

for x in range(len(imagery_11)):
    imagery_11[x]='img/'+imagery_11[x]

#imagery_12= for future use

#imagery_13= for future use

imagery_14=[
    'icon_blank.png',
    'bd_amp_tm.png',
    'bd_amp_sqd.png',
    'bd_amp_sctn.png',
    'bd_amp_plt.png',
    'bd_amp_co.png',
    'bd_amp_bn.png',
    'bd_amp_bde.png',
    'bd_amp_div.png',
    'bd_amp_crps.png',
    'bd_amp_army.png'
    ]

for x in range(len(imagery_14)):
    imagery_14[x]='img/'+imagery_14[x]


'''
Notes:

I had another copy of these above variables to have a copy of lists
not associated with PhotoImage but don't need it for now.

'''
