# Create project structure
mkdir -p project_name/{backend,frontend}

# Backend setup
cd project_name/backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn sqlalchemy python-dotenv
pip freeze > requirements.txt
mkdir -p src/{config,api,core,models,schemas,services,utils}  

# Example 
mkdir -p src/{config,api, core, models, utils} tests static/{css,js,images} templates docs scripts
touch src/__init__.py src/main.py README.md requirements.txt .gitignore .env.example


# Frontend setup 
mkdir -p {public,src}  
mkdir -p src/{assets,components,hooks,...} # For Vite.js
touch .env .env.example .gitignore README.md

# Root level setup
cd ..
touch docker-compose.yml Makefile README.md .gitignore


