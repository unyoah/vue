from rest_framework import serializers

from teacher.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
# class TeacherSerializer(serializers.Serializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    # name = serializers.CharField(max_length=100)
    # phone = serializers.CharField(max_length=11)
    # gender = serializers.SerializerMethodField()
    #
    # def get_gender(self, obj):
    #     return obj.get_gender_display()


class TeacherDeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=1)
    phone = serializers.CharField(min_length=11, max_length=11)
    gender = serializers.IntegerField(min_value=0, max_value=2)

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
