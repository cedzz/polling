from teams.models import Teams, Members


class TeamStore(object):

    def create_team(self, **kwargs):
        return Teams.objects.create(**kwargs)

    def create_members(self, team, member_data):
        member_list = []
        for member in member_data:
            member_list.append(
                Members(team=team, **member)
            )
        return Members.objects.bulk_create(member_list)