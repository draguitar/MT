# coding=utf-8



import pandas as pd 
# %%
'''
df = pd.read_csv('label.csv', header=None)
# ^ 開始
# $ 結束
df[df[1].str.contains('[A-Za-z]{2}\d{4}[A-Za-z]\d{2}[A-Za-z]', regex=True)]
#df[df[1].str.contains('^[A-Za-z]{2}\d{4}[A-Za-z]\d{2}[A-Za-z]$', regex=True)]
'''
# %%
df2 = pd.read_excel('彙整_20200914.xlsx')
#df2 = pd.read_csv('label.csv')
# %%

df2 = df2[df2['STATUS'].notnull()]
df3 = df2[df2['STATUS'].str.contains('P[A-Za-z]{1}\d{4}[A-Za-z]\d{2}[A-Za-z]{1}', regex=True)]
print(df3['STATUS'])

# %%
# 找出批號
df3['批號'] = df3['STATUS'].str.extract(r'(P[A-Za-z]{1}\d{4}[A-Za-z]\d{2}[A-Za-z]{1})', expand=False)
df3.to_excel('批號.xlsx', index=False)
# %%
# AO Rule-1
df_rule_1 = df2[df2['STATUS'].notnull()]
df_rule_1 = df_rule_1[df_rule_1['STATUS'].str.contains('XG[A-Za-z]{1}\d{2}[A-Ua-u]\d{2}00', regex=True)]
df_rule_1['批號'] = df_rule_1['STATUS'].str.extract(r'(XG[A-Za-z]{1}\d{2}[A-Ua-u]\d{2}00)', expand=False)

df_rule_1.to_excel('AO_Rule_1.xlsx', index=False)
# %%
# AO Normal-Rule
# Bump CSP1 CSP2
df_normal_rule = df2[df2['STATUS'].notnull()]
df_normal_rule = df_normal_rule[df_normal_rule['ROOTCAUSE']=='卡帳']
df_normal_rule = df_normal_rule[df_normal_rule['STATUS'].str.contains('Q[A-Za-z]{1}\d{2}\w{4}0[a-zA-Z]{1}', regex=True)]
df_normal_rule['批號'] = df_normal_rule['STATUS'].str.extract(r'(Q[A-Za-z]{1}\d{2}\w{4}0[a-zA-Z]{1})', expand=False)
df_normal_rule.to_excel('Q_AO_Normal_Rule_1.xlsx', index=False)
# %%
# SMT
# Test
# CP
# Assy
# Nulti-Die(Main Die)
df_normal_rule = df2[df2['STATUS'].notnull()]
df_normal_rule = df_normal_rule[df_normal_rule['ROOTCAUSE']=='卡帳']
df_normal_rule = df_normal_rule[df_normal_rule['STATUS'].str.contains('P[A-Za-z]{1}\d{2}\w{4}0[a-zA-Z]{1}', regex=True)]
df_normal_rule['批號'] = df_normal_rule['STATUS'].str.extract(r'(P[A-Za-z]{1}\d{2}\w{4}0[a-zA-Z]{1})', expand=False)
df_normal_rule.to_excel('P_AO_Normal_Rule_2.xlsx', index=False)
# %%



