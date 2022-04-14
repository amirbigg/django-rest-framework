from rest_framework import serializers
from .models import Question, Answer


class PersonSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	name = serializers.CharField()
	age = serializers.IntegerField()
	email = serializers.EmailField()


class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = '__all__'
