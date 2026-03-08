pipeline {
    agent any

    environment {
        APP_ENV = "production"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Nivedha6698/flask-todo-app.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application Test') {
            steps {
                sh '''
                . venv/bin/activate
                python app.py &
                sleep 5
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.log', fingerprint: true
            }
        }
    }

    post {

        success {
            mail to: 'nivedha6698@gmail.com',
            subject: "Jenkins Build Success",
            body: "The Flask Todo App build completed successfully."
        }

        failure {
            mail to: 'nivedha6698@gmail.com',
            subject: "Jenkins Build Failed",
            body: "The Flask Todo App build failed. Please check Jenkins logs."
        }
    }
}