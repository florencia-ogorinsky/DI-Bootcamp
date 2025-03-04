# 🌟 Exercise 1 : Defining the Problem and Data Collection for Loan Default Prediction
# Instructions
# •	Write a clear problem statement for predicting loan defaults.
# The problem is to predict whether the person is going to pay or not based on other features and previous experience.
# •	Identify and list the types of data you would need for this project (e.g., personal details of applicants, credit scores, loan amounts, repayment history).
# We will need name, id, salary, employment details( years in the current role, job stability), credit score, loan amounts, repayment history, bank statement with expenses from the last X years, 
# history of credit judgments. 
# The data types are going to be mostly numerical columns (years of job, income, expenses, etc.) and some Booleans (did he pay in the past, judgment yes or no). 
# There are going to be a few categorical columns such as current job, and more of his/her personal details. 
# •	Discuss the sources where you can collect this data (e.g., financial institution’s internal records, credit bureaus).
# We can obtain this from the bank, financial entities, the applicant can provide a contract and bank extract with his/her income, expenses, etc. , and more depending on the country we are operating. 

# Expected Output: A document detailing the problem statement and a comprehensive plan for data collection, including data types and sources.


# 🌟 Exercise 2 : Feature Selection and Model Choice for Loan Default Prediction
# Instructions
# •	From this dataset, identify which features might be most relevant for predicting loan defaults.
# •	Justify your choice of features.


# The features selected are:
# •	Dependents: More dependents might mean higher financial pressure, making it harder to repay the loan.
# •	Self_Employed: Self-employed people often have unpredictable incomes, which can affect their ability to repay consistently.
# •	CoapplicantIncome: A coapplicant’s income can help with repayment by adding extra financial support.
# •	LoanAmount: The larger the loan, the bigger the risk and the harder it might be to repay.
# •	Loan_Amount_Term: Longer loan terms usually mean smaller payments, but they also come with higher long-term risks.
# •	Credit_History: A good credit history suggests the person is more likely to repay, while a poor or no history means higher default risk.
# •	Loan_Status: This is the outcome (paid or defaulted) and is what the model will learn to predict.

# 🌟 Exercise 3 : Training, Evaluating, and Optimizing the Model
# Instructions
# •	Which model(s) would you pick for a Loan Prediction ?
# •	Outline the steps to evaluate the model’s performance, mentioning specific metrics that would be relevant to evaluate the model.

# The model we would choose is Supervised Learning, labeled dataset, because we would like to classify between loan defaults or not. 

# I would choose the Precision method, where I prefer to reject someone that might pay the credit, but I’m not taking the risk of accepting someone that might not pay the loan. 
# The metrics that we would use is True positives/(true positives + False Positives). False positive would be the cost of not approving a credit to a person that could pay, 
# but we prefer to avoid the risk of accepting someone that wouldn’t pay. 




# 🌟 Exercise 4 : Designing Machine Learning Solutions for Specific Problems
# Instructions
# For each of these scenario, decide which type of machine learning would be most suitable. Explain.
# •	Predicting Stock Prices : predict future prices
# •	Organizing a Library of Books : group books into genres or categories based on similarities.
# •	Program a robot to navigate and find the shortest path in a maze.

# For predicting Stock prices I would use Supervised Learning, regression, because the goal is to predict a numerical value. 
# For organizing a library of books I would use Unsupervised Learning clustering grouping similar data. If the books are already labeled with genres or categories then I would use Supervised Learning. 
# For programming a robot I would use Reinforcement Learning to make the robot make actions and receive feedback.


# 🌟 Exercise 5 : Designing an Evaluation Strategy for Different ML Models
# Instructions
# •	Select three types of machine learning models: one from supervised learning (e.g., a classification model), one from unsupervised learning (e.g., a clustering model), and one from reinforcement learning. 
# For the supervised model, outline a strategy to evaluate its performance, including the choice of metrics (like accuracy, precision, recall, F1-score) and methods (like cross-validation, ROC curves).
# •	For the unsupervised model, describe how you would assess the effectiveness of the model, considering techniques like silhouette score, elbow method, or cluster validation metrics.
# •	For the reinforcement learning model, discuss how you would measure its success, considering aspects like cumulative reward, convergence, and exploration vs. exploitation balance.
# •	Address the challenges and limitations of evaluating models in each category.
# 1. Supervised Learning Model: Random Forest Classifier
# Evaluation Strategy:
# •	Metrics:
# -Accuracy: Overall correct predictions, but can be misleading in unbalanced datasets.
# -Precision & Recall: Precision helps avoid false positives (e.g., approving risky loans), and recall ensures we catch all possible defaulters.
# -F1-Score: Balances precision and recall, especially with imbalanced classes.
# -ROC Curve/AUC: Shows the trade-off between sensitivity and specificity. AUC closer to 1 is better.
# •	Methods:
# -Cross-validation: Split data into K parts to train and test multiple times, ensuring the model generalizes well.
# -Confusion Matrix: Gives a detailed view of true positives, false positives, etc.
# •	Challenges:
# -Accuracy may not be reliable in imbalanced datasets. Use precision, recall, and F1-Score instead.
# 2. Unsupervised Learning Model: K-means Clustering
# Evaluation Strategy:
# •	Metrics:
# -Silhouette Score: Measures how well clusters are separated. A higher score is better.
# -Elbow Method: Helps find the optimal number of clusters by looking for the "elbow" in the plot of inertia vs. K.
# -Davies-Bouldin Index: A lower score means better clustering.
# •	Methods:
# -Visualization: Plot clusters to check if they are distinct.
# -Cluster Validation: If labels are available, use metrics like NMI to see how well clusters match the actual labels.
# •	Challenges:
# -Choosing the right number of clusters can be tricky, and K-means is sensitive to initial centroids.

# 3. Reinforcement Learning Model: Q-learning (Maze Navigation)
# Evaluation Strategy:
# •	Metrics:
# -Cumulative Reward: The total reward the agent accumulates over time. Higher is better.
# -Convergence: Check if the model is stabilizing after many episodes.
# -Exploration vs. Exploitation: Balance how much the agent explores new actions vs. using known good actions.
# •	Methods:
# -Learning Curves: Plot rewards over episodes to see if the agent is improving.
# -Testing on Unseen Environments: Test the agent on new mazes to check if the model generalizes well.
# •	Challenges:
# -Balancing exploration and exploitation is hard, and RL can be computationally expensive.
