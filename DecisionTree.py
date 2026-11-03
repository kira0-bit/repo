import math 
from collections import Counter 
# Sample dataset 
# [Weather, Temperature, Play] 
 
data = [ 
    ["Sunny", "Hot", "No"], 
    ["Sunny", "Hot", "No"], 
    ["Overcast", "Hot", "Yes"], 
    ["Rain", "Mild", "Yes"], 
    ["Rain", "Cool", "Yes"], 
    ["Rain", "Cool", "No"], 
    ["Overcast", "Cool", "Yes"], 
    ["Sunny", "Mild", "No"], 
    ["Sunny", "Cool", "Yes"], 
    ["Rain", "Mild", "Yes"], 
    ["Sunny", "Mild", "Yes"], 
    ["Overcast", "Mild", "Yes"], 
    ["Overcast", "Hot", "Yes"], 
    ["Rain", "Mild", "No"] 
] 
 
features = ["Weather", "Temperature"] 
target = "Play" 
 
# Calculate Entropy 
def entropy(rows): 
    labels = [row[-1] for row in rows] 
    counts = Counter(labels) 
 
    total = len(labels) 
    ent = 0 
 
    for count in counts.values(): 
        probability = count / total 
        ent -= probability * math.log2(probability) 
 
    return ent 
 
# Split dataset according to a feature 
def split_dataset(rows, feature_index, value): 
    return [row for row in rows if row[feature_index] == value] 
 
# Calculate Information Gain 
def information_gain(rows, feature_index): 
    total_entropy = entropy(rows) 
 
    values = set(row[feature_index] for row in rows) 
    weighted_entropy = 0 
 
    for value in values: 
        subset = split_dataset(rows, feature_index, value) 
 
        weight = len(subset) / len(rows) 
        weighted_entropy += weight * entropy(subset) 
 
    return total_entropy - weighted_entropy 
 
# Find feature with highest Information Gain 
def best_feature(rows, feature_indices): 
    gains = [] 
 
    for index in feature_indices: 
        gains.append(information_gain(rows, index)) 
 
    best_index = feature_indices[gains.index(max(gains))] 
    return best_index 
 
# Build Decision Tree recursively 
def build_tree(rows, feature_indices): 
    labels = [row[-1] for row in rows] 
 
    # If all rows belong to one class 
    if len(set(labels)) == 1: 
        return labels[0] 
 
    # If no features are left 
    if not feature_indices: 
        return Counter(labels).most_common(1)[0][0] 
 
    # Select feature with highest Information Gain 
    best_index = best_feature(rows, feature_indices) 
 
    tree = { 
        features[best_index]: {} 
    } 
 
    values = set(row[best_index] for row in rows) 
 
    remaining_features = [ 
        index for index in feature_indices 
        if index != best_index 
    ] 
 
    for value in values: 
        subset = split_dataset(rows, best_index, value) 
 
        tree[features[best_index]][value] = build_tree( 
            subset, 
            remaining_features 
        ) 
 
 
    return tree 
 
# Predict a new sample 
def predict(tree, sample): 
    if not isinstance(tree, dict): 
        return tree 
 
    feature = next(iter(tree)) 
    feature_index = features.index(feature) 
 
    value = sample[feature_index] 
 
    if value in tree[feature]: 
        return predict(tree[feature][value], sample) 
    else: 
        return "Unknown" 
 
# Build the tree 
feature_indices = list(range(len(features))) 
decision_tree = build_tree(data, feature_indices) 
 
print("Decision Tree:") 
print(decision_tree) 
 
# Test prediction 
sample = ["Sunny", "Cool"] 
prediction = predict(decision_tree, sample) 
 
print("\nSample:", sample) 
print("Predicted Class:", prediction)