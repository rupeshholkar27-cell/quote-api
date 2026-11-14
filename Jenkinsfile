pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest
                '''
            }
        }

        stage('Package') {
            steps {
                sh 'tar -czf quote-api-${BUILD_NUMBER}.tar.gz app.py requirements.txt'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: '*.tar.gz', fingerprint: true
        }
    }
}