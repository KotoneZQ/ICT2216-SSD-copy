pipeline {
    agent any
    triggers {
        githubPush()
    }

    environment {
        VIRTUAL_ENV = 'venv'
        ZAP_DOCKER_IMAGE = 'owasp/zap2docker-stable'
        ZAP_CONTAINER_NAME = 'zap'
        ZAP_WORK_DIR = '/zap/wrk'
        REPORT_NAME = 'dependency-check-report.xml'
    }

    stages {
        stage('Start') {
            steps {
                echo 'Starting the pipeline...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t reservespot .'
            }
        }

        stage('OWASP Dependency Check') {
            steps {
                dependencyCheck additionalArguments: '''
                    -o './'
                    -s './'
                    -f 'ALL'
                    --prettyPrint''', odcInstallation: 'OWASP Dependency Check'

                dependencyCheckPublisher pattern: 'dependency-check-report.xml'
            }
        }

        stage('SonarQube Code Analysis') {
            steps {
                dir("${WORKSPACE}") {
                    script {
                        def scannerHome = tool name: 'SSD SonarQube', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                        withSonarQubeEnv('SSD SonarQube') {
                            sh "echo $pwd"
                            sh "${scannerHome}/bin/sonar-scanner"
                        }
                    }
                }
            }
        }

        stage("SonarQube Quality Gate Check") {
            steps {
                script {
                    def qualityGate = waitForQualityGate()
                    if (qualityGate.status != 'OK') {
                        echo "${qualityGate.status}"
                        error "Quality Gate failed: ${qualityGate.status}"
                    } else {
                        echo "${qualityGate.status}"
                        echo "SonarQube Quality Gates Passed"
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                sh 'docker run -d --name django-container -p 8000:8000 reservespot'
                sleep 10
            }
        }

        stage('Django Tests') {
            steps {
                echo 'Running Django Tests...'
                sh 'docker exec django-container python manage.py test'
            }
            post {
                always {
                    junit 'reports/*.xml'
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying to production...'
                // Add deployment commands here
            }
        }

        stage('Post Actions') {
            steps {
                echo 'Performing post actions...'
            }
            post {
                always {
                    echo 'Stopping and removing Docker container...'
                    sh "docker stop django-container"
                    sh "docker rm django-container"
                    echo 'Cleaning up...'
                    cleanWs()
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
