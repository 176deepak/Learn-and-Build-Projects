import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

# dataset
df1 = pd.read_csv("E:/Datasets/student_scores.csv")

# independent & dependent data
X = df1.iloc[:, :-1].values

y = df1.iloc[:, 1].values

# splitting data into trainig & testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# creating object of linear regression class
score_model = LinearRegression()

# fitting data into model
score_model.fit(X_train, y_train)


# predicting score using test data
def score(hrs):
    data = pd.DataFrame([hrs])
    predict_score = score_model.predict(data)
    return round(predict_score[0],2)


# dataset
df2 = pd.read_csv("E:/Datasets/iris.csv")

# dropping unneccesary data column
df2.drop('Id', axis=1, inplace=True)

# 25 and 75 percentile
q1 = df2['SepalWidthCm'].quantile(0.25)
q3 = df2['SepalWidthCm'].quantile(0.75)

# inter quartile range
iqr = q3 - q1

# removing outliers
df2 = df2[(df2['SepalWidthCm'] >= q1 - 1.5 * iqr) & (df2['SepalWidthCm'] <= q3 + 1.5 * iqr)]

# train dataset
X = df2.iloc[:, 0:4]

# scaling dataset in proper scale
scale = StandardScaler()
norm_df = scale.fit_transform(X)

# finding clusters number
cluster_range = range(1, 20)
# ( Within-Cluster Sum of Square ).
WCSS = []
for n_cluster in cluster_range:
    clusters = KMeans(n_cluster, n_init=10)
    clusters.fit(X)
    labels = clusters.labels_
    center = clusters.cluster_centers_
    WCSS.append(clusters.inertia_)

# model trainig
species_model = KMeans(n_clusters=3, max_iter=300)
species_model.fit(X)


# prediction
def species(sl, sw, pl, pw):
    data = pd.DataFrame([[sl, sw, pl, pw]])
    predict_spe = species_model.predict(data)
    if predict_spe == 0:
        return "Species: Iris-versicolor"
    elif predict_spe == 1:
        return "Species: Iris-setosa"
    elif predict_spe == 2:
        return "Species: Iris-verginica"


# dataset
df3 = pd.read_csv("E:/Datasets/Breast_Cancer_Database.csv")

# independent & dependent dataset
X = df3.drop(['id', 'Class'], axis=1).values
y = df3['Class']
X = pd.DataFrame(X)

# splitting data into train & test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# logistic regression object
model = LogisticRegression()

# fitting data into model
model.fit(X_train, y_train)


# predict cancer
def cancer(CT, U_size, U_shape, madhesion, se_cell_size, bnuclei, bchromatin, nnucleoli, mitoses):
    data = pd.DataFrame(
        [[CT, U_size, U_shape, madhesion, se_cell_size, bnuclei, bchromatin, nnucleoli, mitoses]])
    predict_cancer = model.predict(data)
    if predict_cancer == 2:
        return "Bengin, Don't Worry"
    elif predict_cancer == 4:
        return 'Malignant'
