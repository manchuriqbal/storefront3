from django.core.exceptions import ValidationError

def validator_file_size(file):
    max_file_size = 100
    
    if file.size > max_file_size * 1024:
        raise ValidationError(f'file cannot be lager then {max_file_size} KB!')