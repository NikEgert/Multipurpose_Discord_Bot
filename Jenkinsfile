pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                script {
                    // Install dependencies globally if requirements.txt is present
                    if (fileExists('requirements.txt')) {
                        sh "pip install -r requirements.txt"
                    }
                }
            }
        }

        stage('deploy') {
            steps {
                script {
                    // Load Token from Jenkins credentials
                    def secret = credentials('TOKEN')

                    // Run the Python script with the secret as a positional argument
                    sh "python3 bot.py ${secret}"
                }
            }
        }
    }
}
