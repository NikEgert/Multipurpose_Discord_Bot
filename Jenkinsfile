pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        BOT_TOKEN = credentials('TOKEN')
    }

    stages {
        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Create and activate the virtual environment
                    sh '''
                    #!/bin/bash
                    if [ ! -d "$VENV_DIR" ]; then
                        python3 -m venv ${VENV_DIR}
                    fi
                    '''
                }
            }
        }
        stage('Install Requirements') {
            steps {
                script {
                    // Install dependencies inside the virtual environment
                    sh '''
                    #!/bin/bash
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Run bot script with the token as an argument
                    sh '''
                    #!/bin/bash
                    source ${VENV_DIR}/bin/activate
                    python3 bot.py ${BOT_TOKEN}
                    '''
                }
            }
        }
    }
}
