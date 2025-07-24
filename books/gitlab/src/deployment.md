# Deployment

```
mkdir ~/.ssh/deploy-demo-gitlab
ssh-keygen -N '' -f ~/.ssh/deploy-demo-gitlab/gitlab_rsa
ssh-keygen -N '' -f ~/.ssh/deploy-demo-gitlab/gitlab_rsa -p
copy the content of gitlab_rsa_pub to ~/.ssh/authorized_keys on the server
```


