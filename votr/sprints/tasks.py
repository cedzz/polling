# Create your tasks here
from celery.task import periodic_task
from datetime import timedelta

from jira import JIRA

from votr import settings
from sprints.models import Sprints, SprintSummary
from votr import celeryconfig
from celery import Celery

app = Celery('tasks')
app.config_from_object(celeryconfig)


@periodic_task(run_every=timedelta(seconds=20))
def update_active_sprint_summary():
    if Sprints.objects.filter(is_active=True).exists():
        SprintSummary.objects.filter().delete()
        jira_instance = JIRA(server=settings.JIRA_HOST, basic_auth=(settings.JIRA_USER, settings.JIRA_PASSWORD))
        boards = jira_instance.boards()
        sprint_info_dict = {}
        sprints = []
        for board in boards:
            if 'mPulse' in board.name:
                sprint_info_dict['board'] = board.name
                sprints = jira_instance.sprints(board.id, state='ACTIVE')

        active_sprints_obj = filter(lambda sprint: sprint.state == 'ACTIVE', sprints)

        if active_sprints_obj:
            for active_sprint in active_sprints_obj:
                sprint_info_dict['active_sprint'] = active_sprint.name
                sprint_info_dict['active_sprint_id'] = active_sprint.id
        issues_list = jira_instance.search_issues('sprint=%s'%sprint_info_dict['active_sprint_id'])
        update_summary = []
        for issue in issues_list:
            sprint_instance = {}
            sprint_instance['ticket'] = issue.key or ''
            issue_ob = jira_instance.issue(issue.key)
            sprint_instance['ticket_desc'] = issue_ob.fields.summary or ''
            sprint_instance['member'] = issue_ob.fields.assignee or ''
            sprint_instance['due_date'] = issue_ob.fields.duedate or ''
            sprint_instance['status'] = issue_ob.fields.status.name or ''
            if hasattr(issue_ob.fields, 'customfield_10013'):
                sprint_instance['points'] = int(issue_ob.fields.customfield_10013 or 0)
            sprint_instance['sprint_name'] = sprint_info_dict['active_sprint']
            update_summary.append(SprintSummary(**sprint_instance))
        SprintSummary.objects.bulk_create(update_summary)