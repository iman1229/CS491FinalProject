pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile tictactoe.py'
		stash(name: 'compiled-results', includes: '*.py*')
            }
        }
	stage('Test') {
            agent {
                docker {
                    image 'django'
                }
            }
            steps {
                sh 'python square_marker.py test'
                sh 'python win_checker.py test'
                sh 'python integration_tests.py'
                sh 'python square_marker_test.py'
                sh 'python win_checker_test.py'
            }
        }
        stage('Deliver') { 
            agent any
            environment { 
                VOLUME = '$(pwd)/:/src'
                IMAGE = 'cdrx/pyinstaller-linux:python2'
            }
            steps {
                dir(path: env.BUILD_ID) { 
                    unstash(name: 'compiled-results') 
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F tictactoe.py'" 
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/dist/tictactoe" 
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}