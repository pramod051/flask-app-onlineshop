pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-shop"
        CONTAINER_NAME = "flask-shop-container"
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    checkout([$class: 'GitSCM', 
                        branches: [[name: '*/master']],
                        userRemoteConfigs: [[
                            url: 'https://github.com/pramod051/flask-app-onlineshop.git',
                            credentialsId: 'github-creds'  // Use the credentials ID from Step 2
                        ]]
                    ])
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Stop & Remove Old Container') {
            steps {
                script {
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                }
            }
        }

        stage('Run New Docker Container') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
                }
            }
        }
    }
}
