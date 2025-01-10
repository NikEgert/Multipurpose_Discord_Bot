pipeline {
    agent any

    environment {
        MY_SECRET_CREDENTIAL = credentials('TOKEN')
    }

    stages {
        stage('build') {
            steps {
                script {
                    // Install dependencies from requirements.txt if available
                    if (fileExists('requirements.txt')) {
                        sh "pip install -r requirements.txt"
                    } else {
                        echo "No requirements.txt file found"
                    }
                }
            }
        }

        stage('deploy') {
            steps {
                script {
                    // Run the Python script with the secret as an argument
                    sh "python3 bot.py ${MY_SECRET_CREDENTIAL}"
                }
            }
        }
    }
}
