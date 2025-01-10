pipeline {
    agent any

    environment {
        MY_SECRET_CREDENTIAL = credentials('TOKEN')
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
