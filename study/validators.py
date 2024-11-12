from rest_framework.serializers import ValidationError


def validate_video_url(value):
    url = 'youtube.com'
    if url not in value.lower():
        raise ValidationError('Видео урока должно находиться на Youtube.')
