pipeline {
    agent any
    
    stages {
        stage("Checkout from repo and build docker image") {
            steps {
                // Source repo url
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'GitHub', url: 'https://github.com/Biswajit1693/DeployWeatherApp']])
                // Build docker image
                sh 'sudo docker build -t appweather:latest .'
                
            }
        }
        
        stage("Push to dockerhub") {
            steps {
                // Login to Dockerhub
                withCredentials([string(credentialsId: 'docker-passwd', variable: 'dockerpssd')]) {
                sh 'sudo docker login -u jeetlinux -p ${dockerpssd}'
                    
                }
                
                // push the image to dockerhub
                sh 'sudo docker tag appweather:latest jeetlinux/docker-demo:appweather'
                sh 'sudo docker push jeetlinux/docker-demo:appweather'
                
            }
        }
        
        stage("Deploy") {
            steps {
                withCredentials([file(credentialsId: 'kubemini', variable: 'KUBECONFIG')]) {
                sh 'export KUBECONFIG=$KUBECONFIG'
                
                //deployment
                
                sh 'kubectl apply -f deployment.yaml --force'
                           
                }
            }
        }
        
    }

}