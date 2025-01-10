pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                script {
                    // Install dependencies globally if requirements.txt is present
                    if (fileExists('requirements.txt')) {
                        sh "bash -c 'pip install -r requirements.txt'"
                    }
                }
            }
        }

        stage('deploy') {
            steps {
                script {
                    // Load secret from Jenkins credentials
                    def secret = credentials('TOKEN')

                    // Run the Python script with the secret as a positional argument
                    sh "bash -c 'python3 bot.py ${secret}'"
                }
            }
        }
    }
}
