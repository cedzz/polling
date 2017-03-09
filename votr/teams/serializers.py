from rest_framework import serializers

from teams.models import Teams, Members


class MemberInfo(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = '__all__'


class TeamInfo(serializers.ModelSerializer):

    class Meta:
        model = Teams
        fields = ('team_name', 'company')


class TeamSerializer(serializers.Serializer):

    company = serializers.CharField(required=True, max_length=50)
    team_name = serializers.CharField(required=True, max_length=50)
    member = MemberInfo(required=False)


class MemberSerializer(serializers.Serializer):

    name = serializers.CharField(required=True, max_length=50)
    age = serializers.IntegerField()
    team = TeamInfo(required=True)

    def validate(self, data):

        self.team = data.get("team")
        if not Teams.objects.filter(team_name=self.team.get("team_name")).exists():
            raise serializers.ValidationError("Invalid Team")