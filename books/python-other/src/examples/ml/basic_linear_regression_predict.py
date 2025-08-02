from joblib import load
import sys

if len(sys.argv) < 2:
    exit(f"Usage: {sys.argv[0]} Xes")

input_values = []
for val in sys.argv[1:]:
    input_values.append([float(val)])

model = load('linear.joblib')
print(model.predict(input_values))
