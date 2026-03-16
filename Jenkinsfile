pipeline {
    agent any

    environment {
        IMAGE_NAME = 'nive-todo-app:latest'
        DOCKERHUB_CREDENTIALS = 'dockerhubtoken'
        DOCKERHUB_REPO = 'nivedhajd/nive-todo-app'
        SONAR_TOKEN = credentials('sonartoken1')
        SCANNER_HOME = tool 'sonarscanner'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Nivedha6698/flask-todo-app.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar') {
                    sh """
                    $SCANNER_HOME/bin/sonar-scanner
                      -Dsonar.projectKey=nive-todo-app
                      -Dsonar.sources=.
                      -Dsonar.host.url=http://13.239.63.86:9000
                      -Dsonar.login=$SONAR_TOKEN
                    """
                }
            }
        }

        stage('Image Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Docker Login and Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhubtoken',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                    docker login -u $DOCKER_USER -p $DOCKER_PASS
                    docker tag $IMAGE_NAME $DOCKERHUB_REPO:latest
                    docker push $DOCKERHUB_REPO:latest
                    """
                }
            }
        }

        stage('Pull Docker Image') {
            steps {
                sh "docker pull $DOCKERHUB_REPO:latest"
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop nive-todo-container || true'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh 'docker rm nive-todo-container || true'
            }
        }

        stage('Deploy Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name nive-todo-container $DOCKERHUB_REPO:latest'
            }
        }
    }
}