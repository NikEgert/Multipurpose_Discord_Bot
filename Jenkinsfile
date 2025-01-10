pipeline {
    agent any

    environment {
        // This makes the Jenkins secret available as an environment variable
        MY_SECRET_CREDENTIAL = credentials('TOKEN')
    }

    stages {
        stage('build') {
            steps {
                script {
                    // Install dependencies if requirements.txt is present
                    if (fileExists('requirements.txt')) {
                        sh "bash -c 'pip install -r requirements.txt'"
                    }
                }
            }
        }

        stage('deploy') {
            steps {
                script {
                    // Run the Python script with the secret as an argument
                    sh "bash -c 'python3 bot.py ${MY_SECRET_CREDENTIAL}'"
                }
            }
        }
    }
}
