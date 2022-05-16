from django.core.exceptions import ValidationError

def validate_transaction(value):
    if value > 9 or value < 1:
        raise ValidationError(('%(value)s is not a valid transaction type'), params={'value': value},)