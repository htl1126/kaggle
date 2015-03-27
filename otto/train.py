import pandas as pd
import numpy as np
from sklearn import ensemble, feature_extraction, preprocessing

def logloss_mc(y_true, y_prob, epsilon=1e-15):
    """ Multiclass logloss
    This function is not officially provided by Kaggle, so there is no
    guarantee for its correctness.
    """
    # normalize
    y_prob = y_prob / y_prob.sum(axis=1).reshape(-1, 1)
    y_prob = np.maximum(epsilon, y_prob)
    y_prob = np.minimum(1 - epsilon, y_prob)
    # get probabilities
    y = [y_prob[i, j] for (i, j) in enumerate(y_true)]
    ll = - np.mean(np.log(y))
    return ll

def main():
    # import data
    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')
    sample = pd.read_csv('sampleSubmission.csv')

    # drop ids and get labels
    labels = train.target.values
    train = train.drop('id', axis=1)
    train = train.drop('target', axis=1)
    test = test.drop('id', axis=1)

    # transform counts to TFIDF features
    tfidf = feature_extraction.text.TfidfTransformer()
    train = tfidf.fit_transform(train).toarray()
    test = tfidf.transform(test).toarray()

    # scale data
    train = preprocessing.scale(train)
    test = preprocessing.scale(test)

    # encode labels
    lbl_enc = preprocessing.LabelEncoder()
    labels = lbl_enc.fit_transform(labels)

    # train a random forest classifier
    clf = ensemble.RandomForestClassifier(n_jobs=-1, n_estimators=100)
    clf.fit(train, labels)

    # predict on test set
    preds = clf.predict_proba(test)

    # create submission file
    preds = pd.DataFrame(preds, index=sample.id.values, columns=sample.columns[1:])
    preds.to_csv('benchmark.csv', index_label='id')

if __name__ == "__main__":
    main()
