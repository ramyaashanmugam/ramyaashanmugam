pipeline {

    agent { docker { image 'python:3.10.1-alpine' } }

    stages {

        stage('build') {

            steps {

                sh 'python --version'
                sh 'ls -l'
                sh 'python flask_pjt/weather.py'

            }

        }

    }
}
