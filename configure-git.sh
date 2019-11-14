# This file is used to configure your git instance with your user name and
# you email. It is useful if you do not have a global git configuration, or
# if you need to create your commits with a dedicated user for a specific
# repository.

echo "Configuring user info. Ctrl+C to cancel."

read -p "Your name: " name
git config user.name "$name"

read -p "Your email: " email
git config user.email "$email"

echo "Configuring standard aliases: co, br, ci, st"

git config alias.co checkout
git config alias.br branch
git config alias.ci commit
git config alias.st status

echo "Configuration complete."