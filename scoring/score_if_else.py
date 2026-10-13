# AUTO-GENERATED FROM ORIGINAL XGBOOST JSON MODEL
# Exact 100-tree IF/ELSE scorer with XGBoost missing-value default branches.
import math
import numpy as np
import pandas as pd

FEATURE_NAMES = ['age', 'annual_income', 'tenure_months', 'credit_score', 'existing_products', 'monthly_spend', 'avg_monthly_balance', 'digital_txn_ratio', 'mobile_logins_30d', 'branch_visits_6m', 'web_visits_30d', 'credit_utilization', 'delinquency_12m', 'marketing_contacts_90d', 'days_since_last_txn', 'campaign_month', 'campaign_quarter', 'campaign_dayofweek', 'campaign_is_weekend', 'campaign_month_sin', 'campaign_month_cos', 'log_income', 'log_monthly_spend', 'log_avg_balance', 'log_web_visits', 'spend_to_income', 'balance_to_income', 'digital_engagement', 'channel_engagement', 'product_penetration', 'delinquency_rate', 'contact_pressure', 'high_value_customer', 'digital_customer', 'credit_risk_flag', 'income_x_credit_score', 'digital_x_spend', 'tenure_x_products']
BASE_SCORE = 0.4452
BASE_MARGIN = math.log(BASE_SCORE / (1.0 - BASE_SCORE))



def tree_001(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 747.0:
        if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.649719:
                return 0.030416852
            else:
                return -0.019314833
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 622.0:
                return -0.035439108
            else:
                return -0.012229119
    else:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 21.01223:
                return 0.055267133
            else:
                return -0.025042856
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 576.0:
                return 0.027556142
            else:
                return -0.0372587

def tree_002(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 747.0:
        if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.649719:
                return 0.031070087
            else:
                return -0.01546482
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 622.0:
                return -0.03322768
            else:
                return -0.010284933
    else:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['annual_income']) and x['annual_income'] < 126681.43:
                return 0.03641594
            else:
                return 0.06475489
        else:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.14506714:
                return -0.019149465
            else:
                return 0.024754703

def tree_003(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 747.0:
        if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.37858593:
                return 0.041287236
            else:
                return -0.0028985979
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 523.0:
                return -0.051306993
            else:
                return -0.020732382
    else:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.78976053:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
                return 0.05117326
            else:
                return 0.024527358
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 774.0:
                return -0.042342182
            else:
                return 0.024808507

def tree_004(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 747.0:
        if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.37858593:
                return 0.037858304
            else:
                return -0.00043362656
        else:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 701.6727:
                return -0.033351544
            else:
                return -0.012804912
    else:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.78976053:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 966.62946:
                return 0.02490117
            else:
                return 0.054446843
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 774.0:
                return -0.04054498
            else:
                return 0.021039225

def tree_005(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 648.0:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.8357259:
                return -0.018432425
            else:
                return 0.035066944
        else:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 492.58432:
                return -0.05323242
            else:
                return -0.025822053
    else:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 800.0:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
                return 0.017615931
            else:
                return -0.009228754
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
                return 0.06365391
            else:
                return 0.029834876

def tree_006(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 747.0:
        if not pd.isna(x['delinquency_rate']) and x['delinquency_rate'] < 0.16666667:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1088.6907:
                return -0.005692688
            else:
                return 0.031627692
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 614.0:
                return -0.038950235
            else:
                return -0.012786319
    else:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1751.9232:
            if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 0.52795935:
                return 0.024687385
            else:
                return -0.01981742
        else:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 640.0272:
                return 0.024068741
            else:
                return 0.050127205

def tree_007(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 715.0:
        if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.41746658:
                return 0.03602263
            else:
                return -0.007857977
        else:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 120.0:
                return -0.030637285
            else:
                return -0.0067676413
    else:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['channel_engagement']) and x['channel_engagement'] < 36.0:
                return -0.013355218
            else:
                return 0.03830736
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 798.0:
                return -0.0064536566
            else:
                return 0.027714867

def tree_008(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 622.0:
        if not pd.isna(x['delinquency_rate']) and x['delinquency_rate'] < 0.25:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.18931621:
                return 0.019876016
            else:
                return -0.020583771
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.3:
                return -0.023633704
            else:
                return -0.054366805
    else:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 771.0:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1032.593:
                return -0.008788763
            else:
                return 0.024206217
        else:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 2362.9646:
                return 0.015194245
            else:
                return 0.04329754

def tree_009(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 715.0:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 551.0:
                return -0.030173993
            else:
                return 0.008164042
        else:
            if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 7.2296267:
                return -0.015896192
            else:
                return -0.03952573
    else:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1032.593:
                return 0.019066488
            else:
                return 0.04596388
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 576.0:
                return 0.011647719
            else:
                return -0.04453218

def tree_010(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 747.0:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1088.6907:
                return -0.006813489
            else:
                return 0.024603752
        else:
            if not pd.isna(x['age']) and x['age'] < 28.0:
                return 0.0065908954
            else:
                return -0.029655278
    else:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1702.1538:
            if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 0.52795935:
                return 0.023241725
            else:
                return -0.01968382
        else:
            if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 16343.396:
                return 0.03760293
            else:
                return -0.004766831

def tree_011(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 614.0:
        if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 30.0:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1483.121:
                return -0.028965235
            else:
                return 0.0069528627
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 384.0:
                return -0.038348373
            else:
                return 0.00038909478
    else:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 747.0:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1028.5687:
                return -0.0059186122
            else:
                return 0.017599406
        else:
            if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.4941142:
                return 0.014973476
            else:
                return 0.039884925

def tree_012(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 645.0:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.086653225:
            if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.44335848:
                return 0.072614625
            else:
                return -0.0009866382
        else:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 28.0:
                return -0.0040473593
            else:
                return -0.027047426
    else:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 807.0:
                return 0.018032512
            else:
                return 0.060564257
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.3528378:
                return 0.019978613
            else:
                return -0.0060560703

def tree_013(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 622.0:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 124.0:
                return -0.019907262
            else:
                return 0.022237197
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.3409091:
                return -0.01994139
            else:
                return -0.045141686
    else:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 966.62946:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 806.0:
                return -0.0053842817
            else:
                return 0.033024512
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
                return 0.035664503
            else:
                return 0.0068455064

def tree_014(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 614.0:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 384.0:
                return -0.017921919
            else:
                return 0.013629689
        else:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 50.0:
                return -0.050052773
            else:
                return -0.022963334
    else:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1032.593:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 771.0:
                return -0.006007528
            else:
                return 0.021121684
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
                return 0.033607956
            else:
                return 0.0073837624

def tree_015(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 760.0:
        if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 270.82376:
                return -0.038978364
            else:
                return 0.017078793
        else:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 4126.148:
                return -0.025404254
            else:
                return -0.00323017
    else:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1702.1538:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 818.0:
                return -0.010274517
            else:
                return 0.039668288
        else:
            if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 16343.396:
                return 0.037887625
            else:
                return -0.0029754224

def tree_016(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 760.0:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 602.0:
                return -0.008535857
            else:
                return 0.01518581
        else:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 32.0:
                return -0.037248738
            else:
                return -0.012154605
    else:
        if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 21.01223:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
                return 0.036064856
            else:
                return 0.014478244
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.16551724:
                return 0.004658169
            else:
                return -0.05676216

def tree_017(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 614.0:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 524.0:
                return -0.03747837
            else:
                return 0.0010462921
        else:
            if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 1.0044461:
                return 0.008572685
            else:
                return -0.034748297
    else:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 800.0:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
                return -0.013292312
            else:
                return 0.010296802
        else:
            if not pd.isna(x['log_web_visits']) and x['log_web_visits'] < 4.1743875:
                return 0.038985457
            else:
                return 0.0049818032

def tree_018(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 614.0:
        if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 2.719297:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
                return -0.006698228
            else:
                return -0.03027668
        else:
            if not pd.isna(x['campaign_dayofweek']) and x['campaign_dayofweek'] < 7.0:
                return -0.060971137
            else:
                return 0.0052226083
    else:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 966.62946:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.43076736:
                return 0.016108876
            else:
                return -0.011653986
        else:
            if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 212.0:
                return 0.011180803
            else:
                return 0.03425192

def tree_019(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 677.0:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1088.6907:
                return -0.009938493
            else:
                return 0.024661805
        else:
            if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 3.1957495:
                return -0.009436573
            else:
                return -0.035782024
    else:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
            if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 0.5190139:
                return 0.0057639345
            else:
                return -0.026493309
        else:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 6.0:
                return -0.018000238
            else:
                return 0.021045735

def tree_020(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 614.0:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.086653225:
            if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.43505678:
                return 0.067799576
            else:
                return -0.0011707961
        else:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 119.0:
                return -0.025735646
            else:
                return -0.0054646772
    else:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 798.0:
            if not pd.isna(x['annual_income']) and x['annual_income'] < 126069.336:
                return -0.006804866
            else:
                return 0.01397678
        else:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 53.0:
                return 0.038847532
            else:
                return 0.011190902

def tree_021(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 760.0:
        if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.649719:
                return 0.018657854
            else:
                return -0.018999789
        else:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
                return -0.026180709
            else:
                return -0.006180333
    else:
        if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 534.0:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.78976053:
                return 0.030290378
            else:
                return -0.009720467
        else:
            if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.47684544:
                return -0.03366174
            else:
                return 0.032364637

def tree_022(x):
    if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
        if not pd.isna(x['annual_income']) and x['annual_income'] < 94264.84:
            if not pd.isna(x['age']) and x['age'] < 26.0:
                return 0.051199254
            else:
                return -0.008341722
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 18.0:
                return 0.044819366
            else:
                return 0.017229242
    else:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
            if not pd.isna(x['annual_income']) and x['annual_income'] < 216682.5:
                return -0.021010464
            else:
                return 0.041857366
        else:
            if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 4.7473035:
                return 0.008475099
            else:
                return -0.008553301

def tree_023(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 771.0:
        if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.22029553:
                return 0.039407708
            else:
                return 0.0031972423
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.08347976:
                return 0.034571465
            else:
                return -0.011015312
    else:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 6561.482:
                return 0.00881862
            else:
                return 0.039883643
        else:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 54.0:
                return 0.020647215
            else:
                return -0.014819351

def tree_024(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 798.0:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1138.6368:
                return -0.0040733623
            else:
                return 0.022938682
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.23076923:
                return -0.00043859944
            else:
                return -0.026326165
    else:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.94356674:
            if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 19.575317:
                return 0.028266842
            else:
                return -0.031883135
        else:
            return -0.047824662

def tree_025(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 715.0:
        if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 3.937091:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
                return -0.018298125
            else:
                return 0.0088133225
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
                return -0.009393873
            else:
                return -0.029725462
    else:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['campaign_month_sin']) and x['campaign_month_sin'] < -0.5:
                return 0.039430615
            else:
                return 0.015023871
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 576.0:
                return 0.0051558367
            else:
                return -0.049442664

def tree_026(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 747.0:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 523.0:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 5805.3584:
                return -0.049741644
            else:
                return -0.002197078
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
                return 0.0030011816
            else:
                return -0.013861246
    else:
        if not pd.isna(x['product_penetration']) and x['product_penetration'] < 1.0:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1577.4497:
                return 0.0039477223
            else:
                return 0.028473828
        else:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 3466.6257:
                return 0.019154368
            else:
                return -0.028472979

def tree_027(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 715.0:
        if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 3.937091:
            if not pd.isna(x['age']) and x['age'] < 40.0:
                return 0.02210863
            else:
                return -0.00918625
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.37582847:
                return -0.0030045751
            else:
                return -0.025391951
    else:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.48584464:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 4.0:
                return 0.030849738
            else:
                return -0.0049509807
        else:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 928.9288:
                return -0.020206576
            else:
                return 0.016993614

def tree_028(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 798.0:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.6921335:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 648.8121:
                return -0.0088441605
            else:
                return 0.00754598
        else:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 5893.357:
                return -0.025559414
            else:
                return 0.0023260245
    else:
        if not pd.isna(x['tenure_months']) and x['tenure_months'] < 71.0:
            if not pd.isna(x['channel_engagement']) and x['channel_engagement'] < 63.0:
                return 0.06434212
            else:
                return 0.019649908
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
                return 0.030393556
            else:
                return -0.008290506

def tree_029(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 614.0:
        if not pd.isna(x['tenure_months']) and x['tenure_months'] < 120.0:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 30.0:
                return -0.0011028124
            else:
                return -0.028708324
        else:
            if not pd.isna(x['age']) and x['age'] < 25.0:
                return 0.059746988
            else:
                return -0.005573082
    else:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.40005282:
            if not pd.isna(x['age']) and x['age'] < 27.0:
                return 0.047057375
            else:
                return 0.01010214
        else:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1008.9357:
                return -0.00859478
            else:
                return 0.012547105

def tree_030(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 614.0:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.086653225:
            if not pd.isna(x['annual_income']) and x['annual_income'] < 156458.14:
                return -0.014701021
            else:
                return 0.06577002
        else:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1843.6571:
                return -0.029339567
            else:
                return -0.009197505
    else:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 4.0:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1032.593:
                return 0.0026929972
            else:
                return 0.021423543
        else:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 7081.7144:
                return -0.017648283
            else:
                return 0.016204823

def tree_031(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 523.0:
        if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 12579.7295:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 504.0:
                return -0.05593244
            else:
                return 0.017952524
        else:
            if not pd.isna(x['campaign_month_cos']) and x['campaign_month_cos'] < -1.8369701e-16:
                return 0.050123192
            else:
                return -0.014299579
    else:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 705.9994:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.24324325:
                return 0.007155704
            else:
                return -0.017796662
        else:
            if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
                return 0.02346795
            else:
                return 0.004026609

def tree_032(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 544.0:
        if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 376.0:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 74.0:
                return -0.036924377
            else:
                return 0.024701294
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 425.0:
                return 0.05923778
            else:
                return -0.012004626
    else:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 705.9994:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.24324325:
                return 0.004924996
            else:
                return -0.014999986
        else:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.07676515:
                return -0.018446123
            else:
                return 0.0110950945

def tree_033(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 760.0:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.08347976:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.06946272:
                return 0.0077950633
            else:
                return 0.061746825
        else:
            if not pd.isna(x['delinquency_rate']) and x['delinquency_rate'] < 0.16666667:
                return 0.0041710506
            else:
                return -0.013085586
    else:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.78976053:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 534.0:
                return 0.02478433
            else:
                return -0.015124573
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 774.0:
                return -0.06289854
            else:
                return 0.0076613873

def tree_034(x):
    if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
        if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
            if not pd.isna(x['age']) and x['age'] < 27.0:
                return 0.055442333
            else:
                return 0.0001275467
        else:
            if not pd.isna(x['annual_income']) and x['annual_income'] < 216682.5:
                return -0.02048392
            else:
                return 0.03457821
    else:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1150.3887:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 54987.812:
                return 0.0070252568
            else:
                return -0.011011603
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 2.4:
                return 0.01863113
            else:
                return -0.057202876

def tree_035(x):
    if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.47790554:
            if not pd.isna(x['campaign_month_cos']) and x['campaign_month_cos'] < -0.8660254:
                return -0.04544859
            else:
                return 0.0070222216
        else:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1427.0878:
                return -0.027047584
            else:
                return 0.03421978
    else:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.9280563:
                return 0.013729304
            else:
                return -0.044076465
        else:
            if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 1.117448:
                return 0.02876143
            else:
                return -0.008629251

def tree_036(x):
    if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 705.9994:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.48875147:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 658.0:
                return -0.010107967
            else:
                return 0.01362896
        else:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1380.0634:
                return -0.04405546
            else:
                return -0.0104121985
    else:
        if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.031040723:
            if not pd.isna(x['campaign_dayofweek']) and x['campaign_dayofweek'] < 3.0:
                return 0.016954979
            else:
                return -0.058351804
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
                return 0.017247312
            else:
                return -0.0004025395

def tree_037(x):
    if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1052.976:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.40949926:
                return 0.011118707
            else:
                return -0.009828735
        else:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.03496127:
                return -0.054144632
            else:
                return 0.022139706
    else:
        if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.23076923:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 518.38635:
                return -0.019069478
            else:
                return 0.012156396
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.077999935:
                return 0.039166868
            else:
                return -0.019535653

def tree_038(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 614.0:
        if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 384.0:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 29.0:
                return 0.00194488
            else:
                return -0.025140718
        else:
            if not pd.isna(x['campaign_dayofweek']) and x['campaign_dayofweek'] < 6.0:
                return -0.004952364
            else:
                return 0.044988666
    else:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 807.0:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.09511719:
                return -0.024551092
            else:
                return 0.0049765804
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
                return 0.040420223
            else:
                return 0.009165415

def tree_039(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 527.0:
        if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 11339.474:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.08347976:
                return 0.009419358
            else:
                return -0.05083547
        else:
            if not pd.isna(x['campaign_quarter']) and x['campaign_quarter'] < 3.0:
                return 0.045663435
            else:
                return -0.017400302
    else:
        if not pd.isna(x['log_web_visits']) and x['log_web_visits'] < 4.1743875:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 800.0:
                return 0.0038132947
            else:
                return 0.026987493
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 4.0:
                return -0.00049019547
            else:
                return -0.023680266

def tree_040(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 523.0:
        if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 44.0:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 507.0:
                return -0.035865664
            else:
                return 0.057560887
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 595.0:
                return -0.039151665
            else:
                return 0.023333646
    else:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 87.0:
                return 0.0035418037
            else:
                return 0.027600376
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 565.0:
                return -0.0026435663
            else:
                return -0.04569093

def tree_041(x):
    if not pd.isna(x['delinquency_rate']) and x['delinquency_rate'] < 0.25:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1032.593:
            if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 1.1779431:
                return -0.011552738
            else:
                return 0.008322979
        else:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.03496127:
                return -0.05052944
            else:
                return 0.021426266
    else:
        if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 534.0:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 26.0:
                return -0.025746766
            else:
                return -0.0015706801
        else:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 37.0:
                return 0.0020665412
            else:
                return -0.0537513

def tree_042(x):
    if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
        if not pd.isna(x['marketing_contacts_90d']) and x['marketing_contacts_90d'] < 13.0:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 268.1282:
                return -0.026448369
            else:
                return 0.021588821
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.08:
                return 0.038999256
            else:
                return -0.042446088
    else:
        if not pd.isna(x['campaign_month_sin']) and x['campaign_month_sin'] < -0.8660254:
            if not pd.isna(x['campaign_quarter']) and x['campaign_quarter'] < 4.0:
                return -0.043728743
            else:
                return 0.024146978
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 747.0:
                return -0.0051603145
            else:
                return 0.010765446

def tree_043(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 715.0:
        if not pd.isna(x['channel_engagement']) and x['channel_engagement'] < 110.0:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.27480915:
                return 0.01105273
            else:
                return -0.009509016
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.07439441:
                return 0.051610447
            else:
                return -0.019162875
    else:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.48584464:
            if not pd.isna(x['age']) and x['age'] < 47.0:
                return 0.030769283
            else:
                return 0.005906258
        else:
            if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 6531.0825:
                return -0.023105491
            else:
                return 0.009514718

def tree_044(x):
    if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 705.9994:
        if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.24324325:
            if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 31.0:
                return 0.046809223
            else:
                return -0.0010632377
        else:
            if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 567.67535:
                return 0.041889306
            else:
                return -0.018829444
    else:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 535.0:
            if not pd.isna(x['campaign_is_weekend']) and x['campaign_is_weekend'] < 1.0:
                return 0.009172721
            else:
                return -0.042428803
        else:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 778.94836:
                return 0.031347707
            else:
                return 0.0039005727

def tree_045(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 800.0:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 13693.356:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
                return -0.013705701
            else:
                return 0.00020246113
        else:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 22358.947:
                return -0.008297899
            else:
                return 0.054109897
    else:
        if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 64.0:
            if not pd.isna(x['channel_engagement']) and x['channel_engagement'] < 36.0:
                return -0.009554877
            else:
                return 0.03496226
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 4.0:
                return 0.012426471
            else:
                return -0.047163706

def tree_046(x):
    if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
        if not pd.isna(x['tenure_months']) and x['tenure_months'] < 61.0:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 44087.945:
                return -0.0131012965
            else:
                return 0.022596143
        else:
            if not pd.isna(x['marketing_contacts_90d']) and x['marketing_contacts_90d'] < 9.0:
                return -0.03262679
            else:
                return 9.875267e-06
    else:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 943.16644:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.24324325:
                return 0.009874835
            else:
                return -0.009280589
        else:
            if not pd.isna(x['marketing_contacts_90d']) and x['marketing_contacts_90d'] < 14.0:
                return 0.015018015
            else:
                return -0.027674243

def tree_047(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 622.0:
        if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 27.0:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 3.0:
                return 0.046012834
            else:
                return -0.002881037
        else:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 126.0:
                return -0.02420841
            else:
                return 0.0015041422
    else:
        if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.10022004:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 430.92398:
                return -0.053127695
            else:
                return -0.0054673213
        else:
            if not pd.isna(x['marketing_contacts_90d']) and x['marketing_contacts_90d'] < 13.0:
                return 0.008795073
            else:
                return -0.012742909

def tree_048(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 798.0:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 13901.135:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.26086956:
                return 0.0028209276
            else:
                return -0.00993005
        else:
            if not pd.isna(x['campaign_quarter']) and x['campaign_quarter'] < 4.0:
                return 0.059821635
            else:
                return -0.020921852
    else:
        if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 19.575317:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 71.0:
                return 0.032492623
            else:
                return 0.0071765366
        else:
            return -0.04387328

def tree_049(x):
    if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 648.8121:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.39059874:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 64.0:
                return 0.014677184
            else:
                return -0.010651909
        else:
            if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 1.1868211:
                return -0.031839956
            else:
                return -0.005721107
    else:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 535.0:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.7989059:
                return -0.032611456
            else:
                return 0.020483596
        else:
            if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 335.0:
                return 0.0052755205
            else:
                return 0.03163659

def tree_050(x):
    if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.09511719:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.10730007:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 168.39728:
                return 0.06981303
            else:
                return -0.04166192
        else:
            if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.19830467:
                return -0.009596137
            else:
                return -0.040216725
    else:
        if not pd.isna(x['age']) and x['age'] < 39.0:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.3528378:
                return 0.025564939
            else:
                return 0.0023941637
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 747.0:
                return -0.00829078
            else:
                return 0.011509341

def tree_051(x):
    if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
        if not pd.isna(x['campaign_dayofweek']) and x['campaign_dayofweek'] < 3.0:
            if not pd.isna(x['campaign_quarter']) and x['campaign_quarter'] < 2.0:
                return 0.01833725
            else:
                return -0.01677352
        else:
            if not pd.isna(x['annual_income']) and x['annual_income'] < 170679.78:
                return 0.0056941095
            else:
                return 0.028538153
    else:
        if not pd.isna(x['campaign_month_sin']) and x['campaign_month_sin'] < -0.8660254:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.1333845:
                return 0.025122508
            else:
                return -0.039528
        else:
            if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 220.0:
                return -0.007678225
            else:
                return 0.0083056195

def tree_052(x):
    if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 523.0:
            if not pd.isna(x['log_income']) and x['log_income'] < 12.104585:
                return -0.04248345
            else:
                return 0.023808492
        else:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.03496127:
                return -0.03604716
            else:
                return 0.00821299
    else:
        if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 1.117448:
            if not pd.isna(x['log_income']) and x['log_income'] < 11.548673:
                return -0.0360509
            else:
                return 0.034508258
        else:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 26.0:
                return -0.03249156
            else:
                return -0.007056631

def tree_053(x):
    if not pd.isna(x['annual_income']) and x['annual_income'] < 217872.92:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 523.0:
            if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 13379.818:
                return -0.036468048
            else:
                return 0.019748086
        else:
            if not pd.isna(x['delinquency_rate']) and x['delinquency_rate'] < 0.25:
                return 0.0049267667
            else:
                return -0.005583505
    else:
        if not pd.isna(x['tenure_months']) and x['tenure_months'] < 100.0:
            return 0.072643794
        else:
            return -0.018167024

def tree_054(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 807.0:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 13693.356:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 52.0:
                return 0.00037426277
            else:
                return -0.011050794
        else:
            if not pd.isna(x['campaign_quarter']) and x['campaign_quarter'] < 3.0:
                return 0.055508435
            else:
                return 0.0018184498
    else:
        if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 53.0:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.9090001:
                return 0.03813082
            else:
                return -0.016928917
        else:
            if not pd.isna(x['campaign_dayofweek']) and x['campaign_dayofweek'] < 3.0:
                return 0.036612324
            else:
                return -0.011161066

def tree_055(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 787.0:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.64386106:
            if not pd.isna(x['annual_income']) and x['annual_income'] < 46188.137:
                return -0.018328486
            else:
                return 0.0038029612
        else:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 5893.357:
                return -0.017822403
            else:
                return 0.0036359366
    else:
        if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 21.01223:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 71.0:
                return 0.02801145
            else:
                return 0.004136245
        else:
            if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 224.0:
                return 0.0011949006
            else:
                return -0.06540971

def tree_056(x):
    if not pd.isna(x['age']) and x['age'] < 42.0:
        if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 0.06488886:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.8887353:
                return 0.06656301
            else:
                return -0.0016746864
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.40005282:
                return 0.015964754
            else:
                return -0.00477353
    else:
        if not pd.isna(x['log_avg_balance']) and x['log_avg_balance'] < 11.397515:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 34.0:
                return -0.022841204
            else:
                return -0.0034874033
        else:
            if not pd.isna(x['credit_risk_flag']) and x['credit_risk_flag'] < 1.0:
                return -0.004105959
            else:
                return 0.07589843

def tree_057(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 598.0:
        if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 384.0:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 30.0:
                return 0.0015048281
            else:
                return -0.022388652
        else:
            if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 0.54413205:
                return -0.018559001
            else:
                return 0.030657902
    else:
        if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.17777778:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 628.0:
                return 0.042801008
            else:
                return 0.0061631235
        else:
            if not pd.isna(x['age']) and x['age'] < 59.0:
                return 0.003128398
            else:
                return -0.015635926

def tree_058(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 714.0:
        if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 3.8116834:
            if not pd.isna(x['age']) and x['age'] < 35.0:
                return 0.025148336
            else:
                return -0.0041549853
        else:
            if not pd.isna(x['campaign_month']) and x['campaign_month'] < 11.0:
                return -0.014878953
            else:
                return 0.009586027
    else:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.48584464:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 9.0:
                return -0.0095480895
            else:
                return 0.020188877
        else:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 928.9288:
                return -0.014789182
            else:
                return 0.012159367

def tree_059(x):
    if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 492.58432:
        if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 44.0:
            if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 0.6625782:
                return -0.055265624
            else:
                return 0.033259157
        else:
            if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 567.67535:
                return 0.045138095
            else:
                return -0.016232623
    else:
        if not pd.isna(x['age']) and x['age'] < 32.0:
            if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 144.0:
                return -0.0055393744
            else:
                return 0.028374914
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 800.0:
                return -0.0033877348
            else:
                return 0.016614063

def tree_060(x):
    if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1035.5182:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.40949926:
                return 0.009608909
            else:
                return -0.0064808093
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 2.5263157:
                return 0.01713567
            else:
                return -0.07127163
    else:
        if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 21684.385:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.39539102:
                return -0.0155101465
            else:
                return 0.029874025
        else:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 90.0:
                return -0.005619702
            else:
                return -0.033357102

def tree_061(x):
    if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 782.0:
            if not pd.isna(x['channel_engagement']) and x['channel_engagement'] < 104.0:
                return 0.008391435
            else:
                return -0.011280835
        else:
            if not pd.isna(x['age']) and x['age'] < 45.0:
                return 0.03520819
            else:
                return 0.0055569443
    else:
        if not pd.isna(x['campaign_month_sin']) and x['campaign_month_sin'] < -0.8660254:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 43487.88:
                return -0.011161601
            else:
                return -0.065884106
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.23076923:
                return 0.007555429
            else:
                return -0.011188114

def tree_062(x):
    if not pd.isna(x['age']) and x['age'] < 39.0:
        if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 0.09487649:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.8887353:
                return 0.05942989
            else:
                return -0.020146815
        else:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 465.90213:
                return -0.011020622
            else:
                return 0.00973457
    else:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 13693.356:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 766.0:
                return -0.009100155
            else:
                return 0.0073151314
        else:
            if not pd.isna(x['campaign_is_weekend']) and x['campaign_is_weekend'] < 1.0:
                return 0.053541433
            else:
                return -0.0046857814

def tree_063(x):
    if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.32166463:
        if not pd.isna(x['age']) and x['age'] < 26.0:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 180.0:
                return 0.065024845
            else:
                return 0.011357614
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 766.0:
                return -0.004076097
            else:
                return 0.022095693
    else:
        if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 4.6606517:
            if not pd.isna(x['annual_income']) and x['annual_income'] < 51649.348:
                return -0.05404482
            else:
                return 0.0038373345
        else:
            if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 5.45816:
                return -0.032408193
            else:
                return -0.007274727

def tree_064(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 800.0:
        if not pd.isna(x['channel_engagement']) and x['channel_engagement'] < 104.0:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 11.0:
                return -0.014625381
            else:
                return 0.00594813
        else:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1523.0391:
                return -0.012046735
            else:
                return 0.046173077
    else:
        if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 16800.373:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 94.0:
                return 0.012356948
            else:
                return 0.06002931
        else:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 51.0:
                return -0.06084624
            else:
                return 0.01836983

def tree_065(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 527.0:
        if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 11339.474:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.1098251:
                return 0.0022362638
            else:
                return -0.044427086
        else:
            if not pd.isna(x['campaign_month']) and x['campaign_month'] < 9.0:
                return 0.028336162
            else:
                return -0.03430237
    else:
        if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 27.0:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 276.0:
                return 0.018912522
            else:
                return -0.008372349
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 380.0:
                return -0.0050399336
            else:
                return 0.009285325

def tree_066(x):
    if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
        if not pd.isna(x['log_avg_balance']) and x['log_avg_balance'] < 8.811784:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.08497565:
                return -0.0016120905
            else:
                return -0.057691526
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.4:
                return -0.014965683
            else:
                return 0.01053933
    else:
        if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.25452515:
            if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 25.0:
                return -0.03731462
            else:
                return 0.031457614
        else:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 10.0:
                return -0.019557275
            else:
                return 0.0044245454

def tree_067(x):
    if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.08347976:
        if not pd.isna(x['annual_income']) and x['annual_income'] < 54275.26:
            if not pd.isna(x['annual_income']) and x['annual_income'] < 34500.875:
                return 0.015840998
            else:
                return -0.049435362
        else:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.36891842:
                return 0.07207765
            else:
                return 0.012199162
    else:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 798.0:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.26086956:
                return 0.0011186075
            else:
                return -0.010323947
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.4979228:
                return 0.026771644
            else:
                return 0.0006455653

def tree_068(x):
    if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 807.0:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1540.1316:
                return 0.0010854665
            else:
                return 0.0503465
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.11862449:
                return -0.044725366
            else:
                return 0.03747424
    else:
        if not pd.isna(x['campaign_month_sin']) and x['campaign_month_sin'] < -0.8660254:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.1333845:
                return 0.024293644
            else:
                return -0.031544697
        else:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 760.0:
                return -0.007370276
            else:
                return 0.0071762796

def tree_069(x):
    if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
        if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 0.52795935:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.64386106:
                return 0.01091396
            else:
                return -0.018087976
        else:
            if not pd.isna(x['campaign_dayofweek']) and x['campaign_dayofweek'] < 6.0:
                return -0.032329414
            else:
                return 0.01250125
    else:
        if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 380.0:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.21176471:
                return 0.010063791
            else:
                return -0.007139509
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.225:
                return -0.028410712
            else:
                return 0.02048986

def tree_070(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 523.0:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 5805.3584:
            if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.24793467:
                return 0.0074390406
            else:
                return -0.047375154
        else:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 50.0:
                return 0.047294874
            else:
                return -0.04243056
    else:
        if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.09511719:
            if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 676.9991:
                return 0.057561316
            else:
                return -0.019483734
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.26086956:
                return 0.009210508
            else:
                return -0.0015819678

def tree_071(x):
    if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 943.16644:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.48584464:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 6940.8394:
                return 0.010448964
            else:
                return -0.015261672
        else:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 28.0:
                return 0.0077118143
            else:
                return -0.018171934
    else:
        if not pd.isna(x['product_penetration']) and x['product_penetration'] < 2.5263157:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.3314917:
                return -1.0661528e-05
            else:
                return 0.014751743
        else:
            if not pd.isna(x['annual_income']) and x['annual_income'] < 167235.05:
                return -0.0007719499
            else:
                return -0.06283626

def tree_072(x):
    if not pd.isna(x['age']) and x['age'] < 39.0:
        if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 20.0:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 5626.4014:
                return -0.059871376
            else:
                return 0.021092793
        else:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.9448864:
                return 0.012229617
            else:
                return -0.030581376
    else:
        if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.7786996:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 9547.88:
                return -0.0055382247
            else:
                return -0.036391325
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
                return 0.027124658
            else:
                return -0.0011162012

def tree_073(x):
    if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.40005282:
        if not pd.isna(x['annual_income']) and x['annual_income'] < 189018.4:
            if not pd.isna(x['campaign_month_cos']) and x['campaign_month_cos'] < -0.5:
                return -0.0069958605
            else:
                return 0.016039077
        else:
            if not pd.isna(x['channel_engagement']) and x['channel_engagement'] < 82.0:
                return 0.0074512386
            else:
                return -0.031522643
    else:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 4126.148:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 3466.6257:
                return -0.0071056127
            else:
                return -0.04545085
        else:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 3.0:
                return 0.050627794
            else:
                return 0.00039839474

def tree_074(x):
    if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
        if not pd.isna(x['marketing_contacts_90d']) and x['marketing_contacts_90d'] < 11.0:
            if not pd.isna(x['age']) and x['age'] < 27.0:
                return 0.016248314
            else:
                return -0.020174429
        else:
            if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.5662237:
                return 0.01728359
            else:
                return -0.0457514
    else:
        if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.2714188:
            if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 53.0:
                return -0.02545968
            else:
                return 0.028775612
        else:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 10.0:
                return -0.024388367
            else:
                return 0.0036177412

def tree_075(x):
    if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.08347976:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.06946272:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 7.0:
                return -0.051658776
            else:
                return 0.017722322
        else:
            if not pd.isna(x['campaign_month_sin']) and x['campaign_month_sin'] < -0.5:
                return -0.007897689
            else:
                return 0.06734838
    else:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 1531.1241:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 42697.883:
                return -0.02143834
            else:
                return 0.0014427055
        else:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 54987.812:
                return 0.0064139897
            else:
                return -0.0064509944

def tree_076(x):
    if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.32166463:
        if not pd.isna(x['log_avg_balance']) and x['log_avg_balance'] < 9.997393:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 11797.176:
                return 0.00032862969
            else:
                return 0.053188052
        else:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 69417.945:
                return -0.0050133164
            else:
                return 0.019113665
    else:
        if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 6471.467:
            if not pd.isna(x['marketing_contacts_90d']) and x['marketing_contacts_90d'] < 11.0:
                return -0.020696608
            else:
                return 0.0043131574
        else:
            if not pd.isna(x['campaign_dayofweek']) and x['campaign_dayofweek'] < 4.0:
                return -0.008711796
            else:
                return 0.010449744

def tree_077(x):
    if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
        if not pd.isna(x['campaign_dayofweek']) and x['campaign_dayofweek'] < 4.0:
            if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.7819763:
                return -0.008299018
            else:
                return 0.050800413
        else:
            if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 0.87055564:
                return 0.003930336
            else:
                return 0.023822226
    else:
        if not pd.isna(x['campaign_month_sin']) and x['campaign_month_sin'] < -0.8660254:
            if not pd.isna(x['branch_visits_6m']) and x['branch_visits_6m'] < 13.0:
                return -0.035096403
            else:
                return 0.013616793
        else:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 21988.064:
                return 0.010190091
            else:
                return -0.006870524

def tree_078(x):
    if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.71624726:
        if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 3.0:
            if not pd.isna(x['campaign_month']) and x['campaign_month'] < 7.0:
                return -0.005823639
            else:
                return 0.009958869
        else:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.900443:
                return -0.00577583
            else:
                return -0.044511944
    else:
        if not pd.isna(x['tenure_months']) and x['tenure_months'] < 114.0:
            if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 138.0:
                return -0.02249348
            else:
                return 0.016447628
        else:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 177.0:
                return 0.043911785
            else:
                return -0.034458317

def tree_079(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 798.0:
        if not pd.isna(x['channel_engagement']) and x['channel_engagement'] < 104.0:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 792.0:
                return 0.0037371349
            else:
                return -0.048479978
        else:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1523.0391:
                return -0.011159698
            else:
                return 0.045954835
    else:
        if not pd.isna(x['tenure_months']) and x['tenure_months'] < 71.0:
            if not pd.isna(x['channel_engagement']) and x['channel_engagement'] < 63.0:
                return 0.056799877
            else:
                return 0.012524339
        else:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 21.0:
                return -0.03941248
            else:
                return 0.010721978

def tree_080(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 798.0:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1540.1316:
            if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.8078215:
                return -0.0035647575
            else:
                return 0.024454754
        else:
            if not pd.isna(x['branch_visits_6m']) and x['branch_visits_6m'] < 3.0:
                return -0.021361172
            else:
                return 0.043012004
    else:
        if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 19.575317:
            if not pd.isna(x['age']) and x['age'] < 67.0:
                return 0.016914515
            else:
                return -0.026034122
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
                return 0.02023067
            else:
                return -0.06452299

def tree_081(x):
    if not pd.isna(x['age']) and x['age'] < 39.0:
        if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 20.0:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 5626.4014:
                return -0.051647346
            else:
                return 0.028784057
        else:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 73.0:
                return 0.0050933966
            else:
                return 0.034363322
    else:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 13901.135:
            if not pd.isna(x['channel_engagement']) and x['channel_engagement'] < 96.0:
                return 0.00021149975
            else:
                return -0.013838655
        else:
            if not pd.isna(x['age']) and x['age'] < 65.0:
                return 0.05044985
            else:
                return -0.031044424

def tree_082(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 523.0:
        if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 13379.818:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 595.0:
                return -0.040801626
            else:
                return 0.039157387
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 500.0:
                return 0.034642514
            else:
                return -0.041624885
    else:
        if not pd.isna(x['delinquency_rate']) and x['delinquency_rate'] < 0.25:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 12130.172:
                return -0.013553442
            else:
                return 0.008839546
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 576.0:
                return -0.0012688499
            else:
                return -0.03679968

def tree_083(x):
    if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.94356674:
        if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 6.0:
            if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 8.419848:
                return -0.022445995
            else:
                return 0.024658186
        else:
            if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 151.0:
                return -0.0036757097
            else:
                return 0.005352313
    else:
        if not pd.isna(x['campaign_dayofweek']) and x['campaign_dayofweek'] < 5.0:
            return -0.06476992
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 94.0:
                return -0.047775354
            else:
                return 0.030512664

def tree_084(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 544.0:
        if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 376.0:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 73.0:
                return -0.02839765
            else:
                return 0.02706716
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 1.0:
                return -0.045178827
            else:
                return 0.030900622
    else:
        if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 112.0:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.08759124:
                return 0.014658466
            else:
                return -0.011278457
        else:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 28.0:
                return 0.014945047
            else:
                return -0.00053277984

def tree_085(x):
    if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 11.0:
        if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.25266793:
            if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 3037.2014:
                return -0.0016462425
            else:
                return 0.049155805
        else:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.7702978:
                return -0.03776969
            else:
                return 0.0031771695
    else:
        if not pd.isna(x['age']) and x['age'] < 62.0:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 53.0:
                return 0.0092379395
            else:
                return -0.0033394848
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.26373628:
                return 0.007785186
            else:
                return -0.025057713

def tree_086(x):
    if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 2.0:
        if not pd.isna(x['campaign_dayofweek']) and x['campaign_dayofweek'] < 3.0:
            if not pd.isna(x['campaign_quarter']) and x['campaign_quarter'] < 2.0:
                return 0.017474407
            else:
                return -0.018025072
        else:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 51.0:
                return 0.01831396
            else:
                return -0.0032223535
    else:
        if not pd.isna(x['campaign_month_sin']) and x['campaign_month_sin'] < -0.8660254:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.061215114:
                return 0.032094613
            else:
                return -0.03554002
        else:
            if not pd.isna(x['existing_products']) and x['existing_products'] < 2.0:
                return 0.0073101306
            else:
                return -0.0063256845

def tree_087(x):
    if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 220.0:
        if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 12482.361:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 8321.197:
                return -0.024548579
            else:
                return 0.0035634437
        else:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.09721651:
                return -0.050143808
            else:
                return -0.009953057
    else:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.7835465:
            if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 4.6606517:
                return 0.018416977
            else:
                return 0.0007906835
        else:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 88.0:
                return -0.038551304
            else:
                return 0.014317661

def tree_088(x):
    if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.39505023:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1444.6698:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.43076736:
                return 0.0011153178
            else:
                return -0.016670484
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.2650413:
                return -0.031635273
            else:
                return 0.034918014
    else:
        if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 7.0:
            if not pd.isna(x['channel_engagement']) and x['channel_engagement'] < 5.0:
                return 0.04243954
            else:
                return -0.038779903
        else:
            if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.5074342:
                return 0.014646473
            else:
                return -0.000371973

def tree_089(x):
    if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.09511719:
        if not pd.isna(x['digital_x_spend']) and x['digital_x_spend'] < 33.257744:
            if not pd.isna(x['campaign_month_sin']) and x['campaign_month_sin'] < -0.5:
                return -0.015018803
            else:
                return 0.05091783
        else:
            if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 1.0308659:
                return 0.03151395
            else:
                return -0.02694695
    else:
        if not pd.isna(x['branch_visits_6m']) and x['branch_visits_6m'] < 13.0:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.11383498:
                return 0.03286318
            else:
                return -0.0017106781
        else:
            if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 18.0:
                return 0.05660907
            else:
                return 0.0034095391

def tree_090(x):
    if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.8078215:
        if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 648.8121:
            if not pd.isna(x['channel_engagement']) and x['channel_engagement'] < 10.0:
                return 0.06337778
            else:
                return -0.007434202
        else:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 45.0:
                return 0.0067707705
            else:
                return -0.004908498
    else:
        if not pd.isna(x['annual_income']) and x['annual_income'] < 160302.56:
            if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 6855.3125:
                return -0.039415
            else:
                return 0.022336468
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 256.0:
                return 0.074618146
            else:
                return -0.004691858

def tree_091(x):
    if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.08347976:
        if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 9.0:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 134.0:
                return -0.06553422
            else:
                return 0.015862426
        else:
            if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 5889.995:
                return 0.058475282
            else:
                return 0.007246719
    else:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 614.0:
            if not pd.isna(x['campaign_dayofweek']) and x['campaign_dayofweek'] < 3.0:
                return -0.023133613
            else:
                return -0.00259478
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.94356674:
                return 0.0025019106
            else:
                return -0.05465749

def tree_092(x):
    if not pd.isna(x['campaign_dayofweek']) and x['campaign_dayofweek'] < 5.0:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.3954734:
            if not pd.isna(x['campaign_month_cos']) and x['campaign_month_cos'] < -0.5:
                return -0.01554468
            else:
                return 0.0133246975
        else:
            if not pd.isna(x['age']) and x['age'] < 26.0:
                return -0.04473946
            else:
                return -0.0058678025
    else:
        if not pd.isna(x['age']) and x['age'] < 26.0:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 61.0:
                return -0.005179429
            else:
                return 0.051113825
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.403247:
                return -0.010039072
            else:
                return 0.008848517

def tree_093(x):
    if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 417.86227:
        if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 335.0:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 1.0285715:
                return -0.0018873692
            else:
                return -0.04846483
        else:
            if not pd.isna(x['annual_income']) and x['annual_income'] < 42583.535:
                return -0.006980132
            else:
                return -0.06710383
    else:
        if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 335.0:
            if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 0.030899163:
                return -0.04506552
            else:
                return 0.0010110661
        else:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 124.0:
                return 0.0076441667
            else:
                return 0.05197015

def tree_094(x):
    if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.9406734:
        if not pd.isna(x['annual_income']) and x['annual_income'] < 28950.92:
            if not pd.isna(x['age']) and x['age'] < 26.0:
                return 0.03147337
            else:
                return -0.041757878
        else:
            if not pd.isna(x['delinquency_12m']) and x['delinquency_12m'] < 4.0:
                return 0.0027376662
            else:
                return -0.006354151
    else:
        if not pd.isna(x['web_visits_30d']) and x['web_visits_30d'] < 39.0:
            if not pd.isna(x['branch_visits_6m']) and x['branch_visits_6m'] < 9.0:
                return 0.034495343
            else:
                return -0.020914411
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.9474315:
                return -0.060176015
            else:
                return 0.01276387

def tree_095(x):
    if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.09511719:
        if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.78976053:
            if not pd.isna(x['branch_visits_6m']) and x['branch_visits_6m'] < 14.0:
                return 0.0029850544
            else:
                return -0.05722484
        else:
            if not pd.isna(x['monthly_spend']) and x['monthly_spend'] < 2217.4558:
                return 0.009758856
            else:
                return -0.054954708
    else:
        if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.11383498:
            if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 122.0:
                return -0.009836238
            else:
                return 0.047563028
        else:
            if not pd.isna(x['log_income']) and x['log_income'] < 10.30122:
                return -0.025930513
            else:
                return 0.0006120585

def tree_096(x):
    if not pd.isna(x['days_since_last_txn']) and x['days_since_last_txn'] < 150.0:
        if not pd.isna(x['branch_visits_6m']) and x['branch_visits_6m'] < 12.0:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.12765957:
                return 0.005345875
            else:
                return -0.015064771
        else:
            if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 0.27215493:
                return -0.028056538
            else:
                return 0.01712886
    else:
        if not pd.isna(x['age']) and x['age'] < 35.0:
            if not pd.isna(x['balance_to_income']) and x['balance_to_income'] < 4.526876:
                return 0.030182077
            else:
                return -0.0031920248
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 1.6216216:
                return 0.00027375316
            else:
                return -0.03173315

def tree_097(x):
    if not pd.isna(x['delinquency_rate']) and x['delinquency_rate'] < 0.16666667:
        if not pd.isna(x['credit_score']) and x['credit_score'] < 807.0:
            if not pd.isna(x['income_x_credit_score']) and x['income_x_credit_score'] < 1540.1316:
                return 0.0024439506
            else:
                return 0.04689317
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.11862449:
                return -0.043640338
            else:
                return 0.037847485
    else:
        if not pd.isna(x['campaign_month_sin']) and x['campaign_month_sin'] < -0.8660254:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 43487.88:
                return -0.0018962178
            else:
                return -0.045779865
        else:
            if not pd.isna(x['tenure_x_products']) and x['tenure_x_products'] < 456.0:
                return -0.002887633
            else:
                return 0.012861607

def tree_098(x):
    if not pd.isna(x['digital_engagement']) and x['digital_engagement'] < 0.71624726:
        if not pd.isna(x['tenure_months']) and x['tenure_months'] < 176.0:
            if not pd.isna(x['tenure_months']) and x['tenure_months'] < 170.0:
                return -0.00022600083
            else:
                return -0.034538794
        else:
            if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 60.0:
                return 0.045782737
            else:
                return -0.030426854
    else:
        if not pd.isna(x['tenure_months']) and x['tenure_months'] < 112.0:
            if not pd.isna(x['campaign_quarter']) and x['campaign_quarter'] < 4.0:
                return 0.011778206
            else:
                return -0.04186239
        else:
            if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 1.6896356:
                return 0.042754363
            else:
                return -0.01704249

def tree_099(x):
    if not pd.isna(x['credit_score']) and x['credit_score'] < 507.0:
        if not pd.isna(x['branch_visits_6m']) and x['branch_visits_6m'] < 2.0:
            return 0.012203177
        else:
            if not pd.isna(x['existing_products']) and x['existing_products'] < 5.0:
                return -0.052423757
            else:
                return -0.008375941
    else:
        if not pd.isna(x['mobile_logins_30d']) and x['mobile_logins_30d'] < 6.0:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.41600105:
                return 0.015013433
            else:
                return -0.038773373
        else:
            if not pd.isna(x['avg_monthly_balance']) and x['avg_monthly_balance'] < 59839.598:
                return 0.0046665
            else:
                return -0.005392836

def tree_100(x):
    if not pd.isna(x['age']) and x['age'] < 39.0:
        if not pd.isna(x['spend_to_income']) and x['spend_to_income'] < 0.09487649:
            if not pd.isna(x['digital_txn_ratio']) and x['digital_txn_ratio'] < 0.8887353:
                return 0.05930517
            else:
                return -0.020026764
        else:
            if not pd.isna(x['credit_utilization']) and x['credit_utilization'] < 0.45493105:
                return 0.015455713
            else:
                return -0.0030930883
    else:
        if not pd.isna(x['log_avg_balance']) and x['log_avg_balance'] < 11.397515:
            if not pd.isna(x['credit_score']) and x['credit_score'] < 747.0:
                return -0.0068616443
            else:
                return 0.0055984654
        else:
            if not pd.isna(x['product_penetration']) and x['product_penetration'] < 0.121212125:
                return 0.00143511
            else:
                return 0.063873574

TREE_FUNCTIONS = [tree_001, tree_002, tree_003, tree_004, tree_005, tree_006, tree_007, tree_008, tree_009, tree_010, tree_011, tree_012, tree_013, tree_014, tree_015, tree_016, tree_017, tree_018, tree_019, tree_020, tree_021, tree_022, tree_023, tree_024, tree_025, tree_026, tree_027, tree_028, tree_029, tree_030, tree_031, tree_032, tree_033, tree_034, tree_035, tree_036, tree_037, tree_038, tree_039, tree_040, tree_041, tree_042, tree_043, tree_044, tree_045, tree_046, tree_047, tree_048, tree_049, tree_050, tree_051, tree_052, tree_053, tree_054, tree_055, tree_056, tree_057, tree_058, tree_059, tree_060, tree_061, tree_062, tree_063, tree_064, tree_065, tree_066, tree_067, tree_068, tree_069, tree_070, tree_071, tree_072, tree_073, tree_074, tree_075, tree_076, tree_077, tree_078, tree_079, tree_080, tree_081, tree_082, tree_083, tree_084, tree_085, tree_086, tree_087, tree_088, tree_089, tree_090, tree_091, tree_092, tree_093, tree_094, tree_095, tree_096, tree_097, tree_098, tree_099, tree_100]

def sigmoid(v):
    if v >= 0:
        z = math.exp(-v)
        return 1.0 / (1.0 + z)
    z = math.exp(v)
    return z / (1.0 + z)

def probability_to_score(probability):
    # POC score mapping. Replace with modeling-team-approved mapping for production.
    return int(np.clip(np.rint(100.0 + 899.0 * probability), 100, 999))

def score_one_row(row):
    margin = BASE_MARGIN
    for fn in TREE_FUNCTIONS:
        margin += fn(row)
    probability = sigmoid(margin)
    prediction = int(probability >= 0.5)
    score = probability_to_score(probability)
    return margin, probability, prediction, score

def score_dataframe(df):
    missing = [c for c in FEATURE_NAMES if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required model features: {missing}")
    work = df.copy()
    for c in FEATURE_NAMES:
        work[c] = pd.to_numeric(work[c], errors="coerce")
    results = [score_one_row(row) for row in work[FEATURE_NAMES].to_dict(orient="records")]
    out = df.copy()
    out["prediction_margin"] = [r[0] for r in results]
    out["probability"] = [r[1] for r in results]
    out["prediction"] = [r[2] for r in results]
    out["score"] = [r[3] for r in results]
    return out

