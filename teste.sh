terraform init /tmp/terraformLab/
terraform plan -var 'accessKey=$accessKey1' -var 'secretKey=$accessSecret1' /tmp/terraformLab/
terraform apply -auto-approve /tmp/terraformLab
