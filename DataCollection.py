from github import Github
g = Github("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") # my access token
repo = g.get_repo("joaomdmoura/crewAI") # my repo
# The data I get is pull requests of the repo.
open_rps = repo.get_pulls(state='open')
close_rps = repo.get_pulls(state='close')
print("Open Pull Requests:")
print("Number,Title,Created Date,Updated Date,Author,Commits,Changed Files,Additions,Deletions,Status")
for rp in open_rps:
    print(f"{rp.number},{rp.title},{rp.created_at},{rp.updated_at},{rp.user.login},{rp.commits},{rp.changed_files},{rp.additions},{rp.deletions},Open")
for rp in close_rps:
    print(f"{rp.number},{rp.title},{rp.created_at},{rp.updated_at},{rp.user.login},{rp.commits},{rp.changed_files},{rp.additions},{rp.deletions},Close")

