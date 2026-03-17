pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonarscanner'
    }

    stages {

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar') {
                    sh """
                    ${SCANNER_HOME}/bin/sonar-scanner \
                    -Dsonar.projectKey=nive-todo-app \
                    -Dsonar.projectName=NiveTodoApp \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=$SONAR_HOST_URL \
                    -Dsonar.login=$SONAR_AUTH_TOKEN
                    """
                }
            }
        }

    }
}