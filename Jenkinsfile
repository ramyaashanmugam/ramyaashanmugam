pipeline { 

    environment { 

        registry = "ramyaashanmugam/flask_app" 
        name="flask_app"

        registryCredential = 'docker_hub' 

        dockerImage = '' 

    }

    agent any 

    stages { 

        stage('Cloning our Git') { 

        steps { 

            git branch: 'main', credentialsId: 'github_access', url: 'https://github.com/ramyaashanmugam/ramyaashanmugam.git'
            

         }
        } 

        stage('Build Docker Image with new code') { 

            steps { 

                script { 

                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 

                }

            } 

        }

        stage('Push Image to Dockerhub') { 

            steps { 

                script { 

                    docker.withRegistry( '', registryCredential ) { 

                        dockerImage.push() 

                    }

                } 

            }
        } 
        
        stage('Remove running container with old code'){
            steps{
                script{
                    //remove the container which is already running, when running 1st time named container will not be available so we are usign 'True'
	                //added -a option to remove stopped container also
	                sh "docker rm -f \$(docker ps -a -f name=flask_app -q) || true"  
                }
            }
	    
            
     }
       
        stage("Run docker image with new code"){
            steps{
                script {
                    sh "docker run -p 5001:5001 --name ${name} -d ${registry}:$BUILD_NUMBER "
                }
            }
        }

    stage('Remove old docker image') {
        steps{
            script{
                try{
                    // remove docker old images
		         sh("docker rmi \$(docker images ${registry} -a -q)")
                }
                catch (err){
                    echo "Caught: ${err}"
                }
                
            }
        }
		
   }

   

    }

}
