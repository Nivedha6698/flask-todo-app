pipeline {
    agent any
    
    environment{
        IMAGE_NAME ='nive-todo-app:latest'
        DOCKERHUB_CREDENTIALS = 'dockerhubtoken'
        DOCKERHUB_REPO ='nivedhajd/nive-todo-app'
    }

    stages {

        stage('Code Checkout') {
            steps {
                git branch:'main', url:"https://github.com/YOUR_GITHUB_USERNAME/flask-devops-app.git"
            }
        }

        stage('Build & Test') {
            steps{
                bat '''
                python --version
                pip install -r requirements.txt
                python -m py_compile app.py
                '''
            }
        }

        stage('Image Build'){
            steps{
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Docker Login and Push'){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhubtoken',
                    usernameVariable:'DOCKER_USER',
                    passwordVariable:'DOCKER_PASS'
                )]) {

                    bat """
                    docker login -u %DOCKER_USER% -p %DOCKER_PASS%
                    docker tag %IMAGE_NAME% %DOCKERHUB_REPO%:latest
                    docker push %DOCKERHUB_REPO%:latest
                    """
                }
            }
        }

        stage('Pull Docker Image'){
            steps{
                bat "docker pull %DOCKERHUB_REPO%:latest"
            }
        }

        stage('Deploy Docker Container'){
            steps{
                bat '''
                docker stop nive-todo-container || exit 0
                docker rm nive-todo-container || exit 0
                docker run -d -p 5000:5000 --name nive-todo-container %DOCKERHUB_REPO%:latest
                '''
            }
        }
    }
}