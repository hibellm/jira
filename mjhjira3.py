# THIS SCRIPT SHOWS HOW TO USE THE CLIENT IN ANONYMOUS MODE
# AGAINST JIRA.ATLASSIAN.COM.
from jira import JIRA
import re

options = {
    'server': 'https://jira.atlassian.com'
    }

jira = JIRA(options)

# GET ALL PROJECTS VIEWABLE BY ANONYMOUS USERS.
projects = jira.projects()
print (projects)

# GET AN ISSUE
#issue = jira.issue('JRA-1330',fields='key')
issue = jira.issue(14311,fields='key,project,name')
print ('This is the issue JRA-1330')
print (issue)

# GET THE ISSUE FIELDS
fields = jira.issue('JRA-1330',fields='key')
print (fields)
