import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

# Load the data
file_path = '/Users/karan.sauravs/Documents/Code/Python3/TalentBox/kepler_data.csv'
data = pd.read_csv(file_path)

# Display the initial shape of the data
print("Initial data shape:", data.shape)

# Select relevant features
features = [
    'koi_score', 'koi_fpflag_nt', 'koi_fpflag_ss', 'koi_fpflag_co', 'koi_fpflag_ec',
    'koi_period', 'koi_period_err1', 'koi_period_err2', 'koi_time0bk', 'koi_time0bk_err1',
    'koi_time0bk_err2', 'koi_impact', 'koi_impact_err1', 'koi_impact_err2', 'koi_duration',
    'koi_duration_err1', 'koi_duration_err2', 'koi_depth', 'koi_depth_err1', 'koi_depth_err2',
    'koi_prad', 'koi_prad_err1', 'koi_prad_err2', 'koi_teq', 'koi_insol', 'koi_insol_err1',
    'koi_insol_err2', 'koi_model_snr', 'koi_steff', 'koi_steff_err1', 'koi_steff_err2',
    'koi_slogg', 'koi_slogg_err1', 'koi_slogg_err2', 'koi_srad', 'koi_srad_err1',
    'koi_srad_err2', 'ra', 'dec', 'koi_kepmag'
]

# Target variable
target = 'koi_disposition'

# Check for missing values in the relevant columns
missing_values = data[features + [target]].isnull().sum()
print("Missing values before imputation:")
print(missing_values[missing_values > 0])

# Remove columns without any observed values
features = [feat for feat in features if feat not in ['koi_teq_err1', 'koi_teq_err2']]

# Impute missing values
imputer = SimpleImputer(strategy='mean')
data[features] = imputer.fit_transform(data[features])

# Display the shape of the data after imputation
print("Data shape after imputation:", data.shape)

# Encode the target variable
label_encoder = LabelEncoder()
data[target] = label_encoder.fit_transform(data[target])

# Split the data into features and target
X = data[features]
y = data[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))


