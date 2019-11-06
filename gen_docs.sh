cd docs
make html
cd build/html
git init
git checkout -b gh-pages
git add .
git -c user.name='Ir1d' -c user.email='sirius.caffrey@gmail.com' commit -m init
  
git push -f -q https://ir1d:$GITHUB_TOKEN@github.com/ir1d/fw.git gh-pages #&>/dev/null