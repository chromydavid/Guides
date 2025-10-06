## FOR LINUX
1. Check if you already have SSH keys
`ls -al ~/.ssh`

2. Generate a new SSH key (replace with your GitHub email)
`ssh-keygen -t ed25519 -C "your_email@example.com"`

3. Start the SSH agent in the background
`eval "$(ssh-agent -s)"`

4. Add your SSH private key to the agent
`ssh-add ~/.ssh/id_ed25519`

5. Display your SSH public key so you can copy it
`cat ~/.ssh/id_ed25519.pub`

6. (Manual Step) Go to GitHub -> Settings -> SSH and GPG keys -> New SSH key, paste the key

7. Test your SSH connection to GitHub
`ssh -T git@github.com`

8. Clone a GitHub repository using SSH
`git clone git@github.com:username/repo.git`




## FOR WINDOWS POWERSHELL (i recomend using HTTP access to Git)
1. Check if you already have SSH keys
`ls -Path $HOME\.ssh`

2. Generate a new SSH key (replace with your GitHub email)
`ssh-keygen -t ed25519 -C "your_email@example.com"`

3. Start the SSH agent in the background
`Start-Service ssh-agent`
`Get-Service ssh-agent` optional, to check it's running

4. Add your SSH private key to the agent
`ssh-add -K $HOME\.ssh\id_ed25519`

5. Display your SSH public key so you can copy it
`Get-Content $HOME\.ssh\id_ed25519.pub`

6. (Manual Step) Go to GitHub -> Settings -> SSH and GPG keys -> New SSH key, paste the key

7. Test your SSH connection to GitHub
`ssh -T git@github.com`

8. Clone a GitHub repository using SSH
`git clone git@github.com:username/repo.git`