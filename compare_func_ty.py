import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from io import StringIO
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from IPython.display import display, display_html 



def compare (model1, model2, X_df,y_df):
    '''
    Take in a X_df, y_df and model  and fit the model , make a prediction, calculate score (accuracy), 
    confusion matrix, rates, clasification report.
    X_df: train, validate or  test. Select one
    y_df: it has to be the same as X_df.
    model: name of your model that you prevously created 
    
    Example:
    mmodel_performs (X_train, y_train, model1)
    '''
    

    #prediction
    pred1 = model1.predict(X_df)
    pred2 = model2.predict(X_df)

    #score = accuracy
    acc1 = model1.score(X_df, y_df)
    acc2 = model2.score(X_df, y_df)


    #conf Matrix
    #model 1
    conf1 = confusion_matrix(y_df, pred1)
    mat1 =  pd.DataFrame ((confusion_matrix(y_df, pred1 )),index = ['actual_dead','actual_survived'], columns =['pred_dead','pred_survived' ])
    rubric_df = pd.DataFrame([['True Negative', 'False positive'], ['False Negative', 'True Positive']], columns=mat1.columns, index=mat1.index)
    cf1 = rubric_df + ': ' + mat1.values.astype(str)
    
    #model2
    conf2 = confusion_matrix(y_df, pred2)
    mat2 =  pd.DataFrame ((confusion_matrix(y_df, pred2 )),index = ['actual_dead','actual_survived'], columns =['pred_dead','pred_survived' ])
    cf2 = rubric_df + ': ' + mat2.values.astype(str)
    #model 1
    #assign the values
    tp = conf1[1,1]
    fp =conf1[0,1] 
    fn= conf1[1,0]
    tn =conf1[0,0]

    #calculate the rate
    tpr1 = tp/(tp+fn)
    fpr1 = fp/(fp+tn)
    tnr1 = tn/(tn+fp)
    fnr1 = fn/(fn+tp)

    #model 2
    #assign the values
    tp = conf2[1,1]
    fp =conf2[0,1] 
    fn= conf2[1,0]
    tn =conf2[0,0]

    #calculate the rate
    tpr2 = tp/(tp+fn)
    fpr2 = fp/(fp+tn)
    tnr2 = tn/(tn+fp)
    fnr2 = fn/(fn+tp)

    #classification report
    #model1
    clas_rep1 =pd.DataFrame(classification_report(y_df, pred1, output_dict=True)).T
    clas_rep1.rename(index={'0': "dead", '1': "survived"}, inplace = True)

    #model2
    clas_rep2 =pd.DataFrame(classification_report(y_df, pred2, output_dict=True)).T
    clas_rep2.rename(index={'0': "dead", '1': "survived"}, inplace = True)
    print(f'''
    ******       Model 1  ******                                ******     Model 2  ****** 
       Overall Accuracy:  {acc1:.2%}              |                Overall Accuracy:  {acc2:.2%}  
                                                
     True Positive Rate:  {tpr1:.2%}              |          The True Positive Rate:  {tpr2:.2%}  
    False Positive Rate:  {fpr1:.2%}              |         The False Positive Rate:  {fpr2:.2%} 
     True Negative Rate:  {tnr1:.2%}              |          The True Negative Rate:  {tnr2:.2%} 
    False Negative Rate:  {fnr1:.2%}              |         The False Negative Rate:  {fnr2:.2%}
    _____________________________________________________________________________________________________________
    ''')
    print('''
    Positive =  'survived'
    Confusion Matrix
    ''')
    conf_1_styler = cf1.style.set_table_attributes("style='display:inline'").set_caption('Model 1 Confusion Matrix')
    conf_2_styler = cf2.style.set_table_attributes("style='display:inline'").set_caption('Model 2 Confusion Matrix')
    space = "\xa0" * 10
    display_html(conf_1_styler._repr_html_()+ space  + conf_2_styler._repr_html_(), raw=True)
    print('''
    ________________________________________________________________________________
    
    Classification Report:
    ''')
    clas_rep1_styler = clas_rep1.style.set_table_attributes("style='display:inline'").set_caption('Model 1 Classification Report')
    clas_rep2_styler = clas_rep2.style.set_table_attributes("style='display:inline'").set_caption('Model 2 Classification Report')
    space = "\xa0" * 10
    display_html(clas_rep1_styler._repr_html_()+ space  + clas_rep2_styler._repr_html_(), raw=True)

############################################################################

def compare_train_validate (model, X_train, y_train, X_validate, y_validate):
    '''
    Take in a X_train, y_train, X_validate, y_validate and model  and fit the model , make a prediction, calculate score (accuracy), 
    confusion matrix, rates, clasification report.
    X_df: train, validate or  test. Select one
    y_df: it has to be the same as X_df.
    model: name of your model that you prevously created 
    
    Example:
    
    '''
    
    

    #prediction
    pred_train = model.predict(X_train)
    pred_validate = model.predict(X_validate)

    #score = accuracy
    acc_train = model.score(X_train, y_train)
    acc_validate = model.score(X_validate, y_validate)


    #conf Matrix
    #model 1
    conf_train = confusion_matrix(y_train, pred_train)
    mat_train =  pd.DataFrame ((confusion_matrix(y_train, pred_train )),index = ['actual_dead','actual_survived'], columns =['pred_dead','pred_survived' ])
    rubric_df = pd.DataFrame([['TN', 'FP'], ['FN', 'TP']], columns=mat_train.columns, index=mat_train.index)
    cf_train = rubric_df + ' : ' + mat_train.values.astype(str)
    
    #model2
    conf_validate = confusion_matrix(y_validate, pred_validate)
    mat_validate =  pd.DataFrame ((confusion_matrix(y_validate, pred_validate )),index = ['actual_dead','actual_survived'], columns =['pred_dead','pred_survived' ])
    cf_validate = rubric_df + ' : ' + mat_validate.values.astype(str)
    #model 1
    #assign the values
    tp = conf_train[1,1]
    fp = conf_train[0,1] 
    fn = conf_train[1,0]
    tn = conf_train[0,0]

    #calculate the rate
    tpr_train = tp/(tp+fn)
    fpr_train = fp/(fp+tn)
    tnr_train = tn/(tn+fp)
    fnr_train = fn/(fn+tp)

    #model 2
    #assign the values
    tp = conf_validate[1,1]
    fp = conf_validate[0,1] 
    fn = conf_validate[1,0]
    tn = conf_validate[0,0]

    #calculate the rate
    tpr_validate = tp/(tp+fn)
    fpr_validate = fp/(fp+tn)
    tnr_validate = tn/(tn+fp)
    fnr_validate = fn/(fn+tp)

    #classification report
    #model1
    clas_rep_train =pd.DataFrame(classification_report(y_train, pred_train, output_dict=True)).T
    clas_rep_train.rename(index={'0': "dead", '1': "survived"}, inplace = True)

    #model2
    clas_rep_validate =pd.DataFrame(classification_report(y_validate, pred_validate, output_dict=True)).T
    clas_rep_validate.rename(index={'0': "dead", '1': "survived"}, inplace = True)
    print(f'''
    ******       Train    ******                                ******     Validate    ****** 
       Overall Accuracy:  {acc_train:.2%}              |                Overall Accuracy:  {acc_validate:.2%}  
                                                
     True Positive Rate:  {tpr_train:.2%}              |          The True Positive Rate:  {tpr_validate:.2%}  
    False Positive Rate:  {fpr_train:.2%}              |         The False Positive Rate:  {fpr_validate:.2%} 
     True Negative Rate:  {tnr_train:.2%}              |          The True Negative Rate:  {tnr_validate:.2%} 
    False Negative Rate:  {fnr_train:.2%}              |         The False Negative Rate:  {fnr_validate:.2%}
    _________________________________________________________________________________
    ''')
    print('''
    Positive =  'survived'
    Confusion Matrix
    ''')
    cf_train_styler = cf_train.style.set_table_attributes("style='display:inline'").set_caption('Train Confusion Matrix')
    cf_validate_styler = cf_validate.style.set_table_attributes("style='display:inline'").set_caption('Validate Confusion Matrix')
    space = "\xa0" * 10
    display_html(cf_train_styler._repr_html_()+ space  + cf_validate_styler._repr_html_(), raw=True)
    print('''
    ________________________________________________________________________________
    
    Classification Report:
    ''')
    clas_rep_train_styler = clas_rep_train.style.set_table_attributes("style='display:inline'").set_caption('Train Classification Report')
    clas_rep_validate_styler = clas_rep_validate.style.set_table_attributes("style='display:inline'").set_caption('Validate Classification Report')
    space = "\xa0" * 10
    display_html(clas_rep_train_styler._repr_html_()+ space  + clas_rep_validate_styler._repr_html_(), raw=True)
