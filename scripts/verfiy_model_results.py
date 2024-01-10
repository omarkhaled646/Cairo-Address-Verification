import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, roc_curve, precision_score, recall_score, roc_auc_score, auc
from tensorflow.keras.models import load_model 
from sklearn.model_selection import train_test_split

def plot_roc_curve_with_target_point(fpr, tpr, thresholds, target_sensitivity=0.7, target_specificity=0.8):
    """
    Plots ROC curve with a target point specified by sensitivity and specificity.

    Parameters:
    - fpr (numpy.ndarray): Array of false positive rates.
    - tpr (numpy.ndarray): Array of true positive rates.
    - thresholds (numpy.ndarray): Array of threshold values.
    - target_sensitivity (float): Target sensitivity for the point on the ROC curve.
    - target_specificity (float): Target specificity for the point on the ROC curve.
    """
    roc_auc = auc(fpr, tpr)

    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = {:.2f})'.format(roc_auc))

    target_thresholds = thresholds[(tpr >= target_sensitivity) & (1 - fpr >= target_specificity)]

    if target_thresholds.size > 0:
        target_threshold = target_thresholds[0]
        index = np.argmax(tpr >= target_sensitivity)
        plt.scatter(fpr[index], tpr[index], c='red', marker='o', label=f'Target Point (Sensitivity={target_sensitivity}, Specificity={target_specificity})')

        plt.axhline(tpr[index], color='gray', linestyle='--')
        plt.axvline(fpr[index], color='gray', linestyle='--')

    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='lower right')


def plot_precision_recall_vs_threshold(precisions, recalls, thresholds):
    """
    Plots precision and recall curves against different thresholds and highlights a point with specified precision and recall.

    Parameters:
    - precisions (numpy.ndarray): Array of precision values.
    - recalls (numpy.ndarray): Array of recall values.
    - thresholds (numpy.ndarray): Array of threshold values.
    """
    plt.plot(thresholds, precisions[:-1], "b--", label="Precision")
    plt.plot(thresholds, recalls[:-1], "g-", label="Recall")

    matching_thresholds = thresholds[(precisions[:-1] >= 0.7) & (recalls[:-1] >= 0.7)]

    if matching_thresholds.size > 0:
        threshold = matching_thresholds[0]
        index = np.argmax(precisions >= 0.7)
        plt.scatter([threshold], [precisions[index]], c='red', marker='o', label='Threshold for Precision and Recall >= 0.7')
        plt.axvline(threshold, color='gray', linestyle='--')
        plt.axhline(precisions[index], color='gray', linestyle='--')

    plt.legend()
    plt.xlabel('Threshold')
    plt.ylabel('Score')
    plt.title('Precision-Recall vs Threshold')
    plt.grid(True)

def evaluate_and_plot_metrics(model_path, data_path):
    """
    Loads a pre-trained model, evaluates it, and plots precision-recall and ROC curves.

    Parameters:
    - model_path (str): Path to the pre-trained model.
    - data_path (str): Path to the data folder containing X.npy and y.npy.
    """
    # Load the pre-trained model
    model = load_model(model_path)

    # Load the data
    X = np.load(f"{data_path}/X.npy")
    y = np.load(f"{data_path}/y.npy")
        
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Predictions on testing set
    y_train_pred = model.predict(X_train) >= 0.5
    y_test_pred = model.predict(X_test) >= 0.5

    # Print precision and recall scores
    print("Training Precision:", precision_score(y_train, y_train_pred))
    print("Training Recall:", recall_score(y_train, y_train_pred))
    print("Testing Precision:", precision_score(y_test, y_test_pred))
    print("Testing Recall:", recall_score(y_test, y_test_pred))
    print("Roc score:", roc_auc_score(y_train, y_train_pred))

    # Precision-Recall curve
    precision, recall, thresholds = precision_recall_curve(y_train, y_train_pred)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plot_precision_recall_vs_threshold(precision, recall, thresholds)
    plt.title("Precision-Recall Curve")

    # ROC curve
    fpr, tpr, thresholds = roc_curve(y_train, y_train_pred)
    plt.subplot(1, 2, 2)
    plot_roc_curve_with_target_point(fpr, tpr, thresholds, target_sensitivity=0.7, target_specificity=0.8)
    plt.title("ROC Curve")

    plt.show()

# Example usage
if __name__ == "__main__":
    model_path = "./model/lstm_model.h5"
    data_path = "./scripts/data"
    evaluate_and_plot_metrics(model_path, data_path)
