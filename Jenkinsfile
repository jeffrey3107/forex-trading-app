pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/jeffrey3107/forex-trading-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t forex-app:latest .'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner -Dsonar.projectKey=forex-app -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=<VhGZaNJ3Bhn64qP@>'
                }
            }
        }
        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s-deployment.yaml'
            }
        }
    }
    post {
        failure {
            echo 'Pipeline failed - check SonarQube for security issues'
        }
        success {
            echo 'Pipeline completed successfully with secure deployment'
        }
    }
}
