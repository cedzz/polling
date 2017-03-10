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
        team = team_store.create_team(**validated_data)
        team_store.create_members(team=team, member_data=member_data)
        return team

class MemberSerializer(serializers.Serializer):

    name = serializers.CharField(required=True, max_length=50)
    age = serializers.IntegerField()
    team = TeamInfo(required=True)

    def validate(self, data):

        self.team = data.get("team")
        if not Teams.objects.filter(team_name=self.team.get("team_name")).exists():
            raise serializers.ValidationError("Invalid Team")