#!/bin/bash

if [ -z "$1" ]
then
  echo "Please provide a project name as the first argument."
  exit 1
fi

PROJECT_NAME=$1

# Create the project directories
mkdir -p "$PROJECT_NAME/app/use_cases"
mkdir -p "$PROJECT_NAME/app/serializers"
mkdir -p "$PROJECT_NAME/domain/entities"
mkdir -p "$PROJECT_NAME/domain/value_objects"
mkdir -p "$PROJECT_NAME/domain/repository_interfaces"
mkdir -p "$PROJECT_NAME/infrastructure/config"
mkdir -p "$PROJECT_NAME/infrastructure/persistence"
mkdir -p "$PROJECT_NAME/infrastructure/api"
mkdir -p "$PROJECT_NAME/infrastructure/utils"
mkdir -p "$PROJECT_NAME/presentation/cli"
mkdir -p "$PROJECT_NAME/presentation/web"
mkdir -p "$PROJECT_NAME/tests/unit"
mkdir -p "$PROJECT_NAME/tests/integration"

# Create the __init__.py files
touch "$PROJECT_NAME/app/__init__.py"
touch "$PROJECT_NAME/app/use_cases/__init__.py"
touch "$PROJECT_NAME/app/serializers/__init__.py"
touch "$PROJECT_NAME/domain/__init__.py"
touch "$PROJECT_NAME/domain/entities/__init__.py"
touch "$PROJECT_NAME/domain/value_objects/__init__.py"
touch "$PROJECT_NAME/domain/repository_interfaces/__init__.py"
touch "$PROJECT_NAME/infrastructure/__init__.py"
touch "$PROJECT_NAME/infrastructure/config/__init__.py"
touch "$PROJECT_NAME/infrastructure/persistence/__init__.py"
touch "$PROJECT_NAME/infrastructure/api/__init__.py"
touch "$PROJECT_NAME/infrastructure/utils/__init__.py"
touch "$PROJECT_NAME/presentation/__init__.py"
touch "$PROJECT_NAME/presentation/cli/__init__.py"
touch "$PROJECT_NAME/presentation/web/__init__.py"

# Create the main project files
#touch "$PROJECT_NAME/.gitignore"
#touch "$PROJECT_NAME/README.md"
#touch "$PROJECT_NAME/requirements.txt"
touch "$PROJECT_NAME/setup.py"

# Create the test configuration file
touch "$PROJECT_NAME/tests/conftest.py"

echo "Project $PROJECT_NAME has been created with the Clean Architecture structure."
