import json
import pickle
import numpy as np

def handler(event, context):
    body = event.get('body')

    if body is None or body == "":
        return "Body is empty", 422
    
    body = json.loads(body)
    input_values = body.get("inputText")

    print(f"Let's see what you sent: {input_values}")

    # Load model here
    with open("model.pkl", 'rb') as file:
        model = pickle.load(file)

    # Change the shape
    input_values = np.array([input_values])
    # Make predictions 
    predictions = model.predict(input_values)
    
    # Return predictions
    return {
        "statusCode": 200,
        "body": json.dumps({"predictions": float(predictions[0])}),
        "headers": {
            'Content-Type': 'application/json',
        },
    }