pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv' // virtual environment
    }

    stages {
        stage('build') {
            steps {
                script {
                    // Create a virtual environment if it doesn't exist
                    if (!fileExists("${WORKSPACE}/${PYTHON_ENV}")) {
                        sh "python3 -m venv ${PYTHON_ENV}"
                    }
                    // Install dependencies if requirements.txt is present
                    if (fileExists('requirements.txt')) {
                        sh """
                            source ${PYTHON_ENV}/bin/activate
                            pip install -r requirements.txt
                        """
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
                    sh """
                        source ${PYTHON_ENV}/bin/activate
                        python3 bot.py ${secret}
                    """
                }
            }
        }
    }
}
