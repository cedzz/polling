from rest_framework import serializers

from teams.models import Teams


class TeamSerializer(serializers.Serializer):

    company = serializers.CharField(required=True, max_length=50)
    team_name = serializers.CharField(required=True, max_length=50)


class MemberSerializer(serializers.Serializer):

    name = serializers.CharField(required=True, max_length=50)
    age = serializers.IntegerField()
    team_name = serializers.CharField(required=True, max_length=50)
    company = serializers.CharField(required=True, max_length=50)

    def validate(self, data):

        if not Teams.objects.filter(team_name=data.get("team_name")).exists():
            raise serializers.ValidationError("Invalid Team")