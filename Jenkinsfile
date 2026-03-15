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
                sh 'python3 -m venv venv'
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

        stage('Validate Python Code') {
            steps {
                sh '''
                . venv/bin/activate
                python -m py_compile app.py
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.py', fingerprint: true
            }
        }
        
        stage('Run Application') {
            steps {
                sh '''
                . venv/bin/activate
                gunicorn -w 4 -b 0.0.0.0:5000 app:app
                '''
            }
        }
    }

    post {

        success {
            emailext (
                to: 'nivedha6698@gmail.com',
                subject: "Build Success: ${env.JOB_NAME}",
                body: """
                Jenkins Build Completed Successfully.

                Job Name: ${env.JOB_NAME}
                Build Number: ${env.BUILD_NUMBER}
                Build URL: ${env.BUILD_URL}
                """
            )
        }

        failure {
            emailext (
                to: 'nivedha6698@gmail.com',
                subject: "Build Failed: ${env.JOB_NAME}",
                body: """
                Jenkins Build Failed.

                Job Name: ${env.JOB_NAME}
                Build Number: ${env.BUILD_NUMBER}
                Build URL: ${env.BUILD_URL}

                Please check Jenkins console output.
                """
            )
        }
    }
}