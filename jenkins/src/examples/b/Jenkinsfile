pipeline {
    agent none
    stages {
        stage('build') {
            agent { label 'master' }
            steps {
                echo 'build'
                sh 'pwd'      // /var/lib/jenkins/workspace/demo-for-pipeline_master-I4VIGTM6JE6TBFWUZBZBVPYDJGBTIK2KHOTD5XDPZN2VMFHSUCCQ
                sh 'id'       // uid=112(jenkins) gid=117(jenkins) groups=117(jenkins),118(docker)
                sh 'uname -a' // Linux s17 4.13.0-43-generic #48-Ubuntu SMP Wed May 16 12:18:48 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
            }
        }
        stage('test') {
            agent {
                docker {
                    image 'python'
                }
            }
            steps {
                echo 'test'
                sh 'pwd'      // /var/lib/jenkins/workspace/demo-for-pipeline_master-I4VIGTM6JE6TBFWUZBZBVPYDJGBTIK2KHOTD5XDPZN2VMFHSUCCQ
                sh 'id'       // uid=112 gid=117 groups=117
                sh 'uname -a' // Linux 8a88f60d26c1 4.13.0-43-generic #48-Ubuntu SMP Wed May 16 12:18:48 UTC 2018 x86_64 GNU/Linux
            }
        }
    }
}
