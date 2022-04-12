pipeline {

    agent { docker { image 'python:3.10.1-alpine' } }

    stages {

        stage('build') {

            steps {

                sh 'python --version'
                sh 'ls -l'
                sh 'sudo pip install flask'
                sh 'sudo python flask_pjt/weather.py'

            }

        }

    }
}
