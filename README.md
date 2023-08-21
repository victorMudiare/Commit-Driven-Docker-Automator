# Git Commit Triggered Docker Image Builder

Automate the building of Docker images when new Git commits are detected.

![GitHub](https://img.shields.io/github/license/your-username/your-repo-name)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)

## Table of Contents

- [Introduction](#introduction)
- [How it Works](#how-it-works)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Requirements](#requirements)

## Introduction

This Python script automates the building of a Docker image when a new Git commit is detected since the last build. It helps streamline the process of keeping your Docker images up-to-date with your codebase.

## How it Works

The script checks for new commits in your Git repository. If a new commit is detected since the last build, it triggers the building of a Docker image using the latest commit hash as the image tag. The last commit hash is stored in a JSON file to keep track of the previous build.

## Getting Started

1. *Clone this repository:*

    bash
    git clone https://github.com/victorMudiare/Commit-Driven-Docker-Automator.git
    cd Commit-Driven-Docker-Automator
    

2. *Install the required Python packages using `requirements.txt`:*

    bash
    pip install -r requirements.txt
    

3. *Run the script with Docker image name:*

    - Using command-line argument:
    
        bash
        python build_docker_on_commit.py --image-name your-image-name
        
      
    - Using environment variable:
    
        bash
        DOCKER_IMAGE_NAME=your-image-name python build_docker_on_commit.py
        

## Configuration

In the `build_docker_on_commit.py` script, you'll find the following configurable variables:

- `commit_data_file`: Adjust this to specify the path for the JSON file storing the last commit hash.

## Requirements

- Python (>=3.6)
- Docker
