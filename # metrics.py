# metrics.py

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_curve,
    auc,
    confusion_matrix
)


class AuthenticationMetrics:
    """
    Standard authentication evaluation metrics.
    """

    @staticmethod
    def accuracy(y_true, y_pred):
        return accuracy_score(y_true, y_pred)

    @staticmethod
    def precision(y_true, y_pred):
        return precision_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        )

    @staticmethod
    def recall(y_true, y_pred):
        return recall_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        )

    @staticmethod
    def f1(y_true, y_pred):
        return f1_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        )

    @staticmethod
    def confusion(y_true, y_pred):
        return confusion_matrix(y_true, y_pred)


class BiometricMetrics:
    """
    Standard biometric verification metrics.

    genuine_scores :
        similarity scores from genuine pairs

    impostor_scores :
        similarity scores from impostor pairs
    """

    @staticmethod
    def compute_eer(
        genuine_scores,
        impostor_scores
    ):

        genuine_scores = np.asarray(genuine_scores)
        impostor_scores = np.asarray(impostor_scores)

        labels = np.concatenate([
            np.ones(len(genuine_scores)),
            np.zeros(len(impostor_scores))
        ])

        scores = np.concatenate([
            genuine_scores,
            impostor_scores
        ])

        fpr, tpr, thresholds = roc_curve(
            labels,
            scores
        )

        fnr = 1.0 - tpr

        idx = np.nanargmin(
            np.abs(fpr - fnr)
        )

        eer = (fpr[idx] + fnr[idx]) / 2.0

        threshold = thresholds[idx]

        return eer, threshold

    @staticmethod
    def compute_auc(
        genuine_scores,
        impostor_scores
    ):

        genuine_scores = np.asarray(genuine_scores)
        impostor_scores = np.asarray(impostor_scores)

        labels = np.concatenate([
            np.ones(len(genuine_scores)),
            np.zeros(len(impostor_scores))
        ])

        scores = np.concatenate([
            genuine_scores,
            impostor_scores
        ])

        fpr, tpr, _ = roc_curve(
            labels,
            scores
        )

        return auc(fpr, tpr)

    @staticmethod
    def roc(
        genuine_scores,
        impostor_scores
    ):

        labels = np.concatenate([
            np.ones(len(genuine_scores)),
            np.zeros(len(impostor_scores))
        ])

        scores = np.concatenate([
            genuine_scores,
            impostor_scores
        ])

        return roc_curve(
            labels,
            scores
        )


def evaluate_classification(
    y_true,
    y_pred
):

    return {
        "Accuracy":
            AuthenticationMetrics.accuracy(
                y_true,
                y_pred
            ),

        "Precision":
            AuthenticationMetrics.precision(
                y_true,
                y_pred
            ),

        "Recall":
            AuthenticationMetrics.recall(
                y_true,
                y_pred
            ),

        "F1":
            AuthenticationMetrics.f1(
                y_true,
                y_pred
            )
    }


def evaluate_verification(
    genuine_scores,
    impostor_scores
):

    eer, thr = BiometricMetrics.compute_eer(
        genuine_scores,
        impostor_scores
    )

    auc_score = BiometricMetrics.compute_auc(
        genuine_scores,
        impostor_scores
    )

    return {
        "EER": eer,
        "Threshold": thr,
        "AUC": auc_score
    }
