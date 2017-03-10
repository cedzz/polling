from sprints.models import Sprints, Projects


class SprintsStore(object):

    def create_sprint(self, **kwargs):
        return Sprints.objects.create(**kwargs)

    def create_project(self, **kwargs):
        return Projects.objects.create(**kwargs)

    def get_project_object_or_none(self, **kwargs):
        try:
            project = Projects.objects.get(**kwargs)
        except Projects.DoesNotExist:
            return None
        return project

    def get_sprints_object_or_none(self, **kwargs):
        try:
            member = Sprints.objects.get(**kwargs)
        except Sprints.DoesNotExist:
            return None
        return member


    def deactivate_project(self, **kwargs):
        project = self.get_project_object_or_none(**kwargs)
        if project:
            project.is_active = False
            project.save()
            return True
        else:
            return False

    def deactivate_sprint(self, **kwargs):
        sprint = self.get_sprints_object_or_none(**kwargs)
        if sprint:
            sprint.is_active = False
            sprint.save()
            return True
        else:
            return False