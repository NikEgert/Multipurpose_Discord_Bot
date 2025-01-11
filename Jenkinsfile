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
                    sh '''
                    #!/bin/bash
                    ${VENV_DIR}/bin/pip install --upgrade pip
                    ${VENV_DIR}/bin/pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh '''
                    #!/bin/bash
                    ${VENV_DIR}/bin/python3 bot.py ${BOT_TOKEN}
                    '''
                }
            }
        }
    }
}
