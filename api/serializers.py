from rest_framework import serializers

from base.models import Course, SubjectArea, Building, Address, Location, MeetingTime, Campus, Session


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Building
        fields = '__all__'


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    building = BuildingSerializer(read_only=True)

    class Meta:
        model = Location
        fields = '__all__'


class SubjectAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubjectArea
        fields = '__all__'


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    subject_area = SubjectAreaSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class MeetingTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MeetingTime
        fields = '__all__'


class CampusSerializer(serializers.HyperlinkedModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Campus
        fields = '__all__'


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    course = CourseSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    campus = CampusSerializer(read_only=True)
    meeting_times = MeetingTimeSerializer(read_only=True, many=True)

    class Meta:
        model = Session
        fields = '__all__'
