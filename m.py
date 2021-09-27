import  time 
from datetime import datetime
from github import Github
import os


end_time = time.time()
start_time = end_time-86400


ACCESS_TOKEN = open("token.txt","r").read()
g = Github(ACCESS_TOKEN)
print(g.get_user())

for i in range(3):  
     start_time_str = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
     end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')
     query = f"language:python created:{start_time_str}..{end_time_str}"
     print(query)
     end_time -= 86400
     start_time -= 86400

     result = g.search_repositories(query)
     print(result.totalCount)

for repository in result:
      print(f"{repository._clone_url}")
      print(f"{repository.clone_url}")
      print(f"{repository.tags_url}")

      print(repository.owner.login)


      os.system(f"git clone {repository.clone_url} repos/{repository.owner.login}/{repository.name}")
     
      
