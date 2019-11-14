
echo "Configuring user info."

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