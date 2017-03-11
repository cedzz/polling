from rest_framework import serializers

from teams.models import Teams, Members
from teams.utils import TeamStore

team_store = TeamStore()


class MemberInfo(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = ('name', 'age',)


class TeamInfo(serializers.ModelSerializer):

    class Meta:
        model = Teams
        fields = ('team_name', 'company')


class TeamSerializer(serializers.Serializer):

    company = serializers.CharField(required=True, max_length=50)
    team_name = serializers.CharField(required=True, max_length=50)
    member = MemberInfo(required=False, many=True)

    def create(self, validated_data):
        member_data = validated_data.pop("member")
        try:
            team = team_store.create_team(**validated_data)
        except Exception as e:
            raise serializers.ValidationError(e.message)
        team_store.create_members(team=team, member_data=member_data)
        return team


class MemberSerializer(serializers.Serializer):

    name = serializers.CharField(required=True, max_length=50)
    age = serializers.IntegerField()
    team = serializers.CharField(required=True, max_length=50)

    def validate(self, data):
        data["team"] = team_store.get_team_object_or_none(team_name=data.get("team").lower())
        if not data["team"]:
            raise serializers.ValidationError("Invalid Team")
        return data

    def save(self):
        try:
            instance = team_store.create_member(member_data=self.validated_data)
        except Exception as e:
            raise serializers.ValidationError(e.message)
        return instance
