# Decision model function
def decision_model(input_data):
    if input_data['age'] >= 18:
        return 'Adult'
    else:
        return 'Minor'
