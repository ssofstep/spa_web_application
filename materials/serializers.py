from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True)
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializers(serializers.ModelSerializer):
    many_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)
    
    def get_many_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'many_lessons')



