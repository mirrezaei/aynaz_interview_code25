import numpy as np
from sklearn import model_selection
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import sys

def pca_logistic_regression_nested_cross_validation(X, y):
    NUM_TRIALS = 10
    NUM_JOB = 4
    CV_INNER = 5
    CV_OUTER = 10
    # Arrays to store scores
    nested_scores_accuracy = np.zeros(NUM_TRIALS)
    nested_scores_precision = np.zeros(NUM_TRIALS)
    nested_scores_recall = np.zeros(NUM_TRIALS)
    nested_scores_f1 = np.zeros(NUM_TRIALS)

    scoring = ['accuracy', 'precision', 'recall', 'f1']

    for i in range(NUM_TRIALS):
        print(i)

        inner_cv = model_selection.KFold(n_splits=CV_INNER, shuffle=True, random_state=i)
        outer_cv = model_selection.KFold(n_splits=CV_OUTER, shuffle=True, random_state=i)

        pipe = Pipeline([
            ('classify', SVC())
        ])

        gamma_range = np.logspace(-9, 3, 13)
        C_range = [1,10,100]
        param_grid = [
            {
                 'classify__gamma': gamma_range, 'classify__C': C_range}
        ]
        clf = GridSearchCV(pipe , param_grid=param_grid, cv=inner_cv,n_jobs=NUM_JOB)

        # Nested CV with parameter optimization
        nested_score = model_selection.cross_validate(clf, X, y, cv=outer_cv, scoring=scoring, n_jobs=NUM_JOB)

        nested_scores_accuracy[i] = nested_score['test_' + scoring[0]].mean()
        nested_scores_precision[i] = nested_score['test_' + scoring[1]].mean()
        nested_scores_recall[i] = nested_score['test_' + scoring[2]].mean()
        nested_scores_f1[i] = nested_score['test_' + scoring[3]].mean()

    print ('Nested for SVM')
    print("Nested Accuracy: " + str(np.mean(nested_scores_accuracy)) + ", std: " + str(np.std(nested_scores_accuracy)))
    print("Nested Precision: " + str(np.mean(nested_scores_precision)) + ", std: " + str(np.std(nested_scores_precision)))
    print("Nested Recall: " + str(np.mean(nested_scores_recall)) + ", std: " + str(np.std(nested_scores_recall)))
    print("Nested f1: " + str(np.mean(nested_scores_f1)) + ", std: " + str(np.std(nested_scores_f1)))




def get__data_tarin_X_label_y(dir_path):
    train_X = []
    y =[]
    i = 0;
    try:
        for line in open(dir_path):
            if len(line.strip())>1 and line.strip() != '\n' and i >0:
                data_tokens = line.split("\t")
                # Convert all strings in a list to int
                data_tokens = list(map(int, data_tokens))
                train_X.append(data_tokens[1:])
                y.append(data_tokens[0])
            i+=1
    except:
        print ("*********************" + + str(sys.exc_info()[0]))
    return train_X, y


train_X, y = get__data_tarin_X_label_y('binary_classification.txt')

pca_logistic_regression_nested_cross_validation(train_X, y)